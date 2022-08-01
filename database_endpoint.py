from flask import Flask, request, g
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import jsonify
import json
import eth_account
import algosdk
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import load_only
from datetime import datetime
import sys

from models import Base, Order, Log
engine = create_engine('sqlite:///orders.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

app = Flask(__name__)

@app.before_request
def create_session():
    g.session = scoped_session(DBSession)

@app.teardown_appcontext
def shutdown_session(response_or_exc):
    sys.stdout.flush()
    g.session.commit()
    g.session.remove()


""" Suggested helper methods """

def check_sig(payload,sig):
    pass

def fill_order(order,txes=[]):
    pass
  
def log_message(d):
    # Takes input dictionary d and writes it to the Log table
    # Hint: use json.dumps or str() to get it in a nice string form
    g.session.add(Log(logtime=datetime.now(), message=json.dumps(d)))
    g.session.commit()

""" End of helper methods """
def process_order(order):

    session=g.session
    new_order = order
    session.add(new_order)
    session.commit()
    # check if there are any existing order that matches
    while (new_order is not None):
        for existing_order in session.query(Order).filter(Order.filled == None).all():
            # if a good rate found,set to filled
            if existing_order.filled == None and existing_order.buy_currency == new_order.sell_currency and \
                    existing_order.sell_currency == new_order.buy_currency and \
                    existing_order.sell_amount / existing_order.buy_amount >= new_order.buy_amount / new_order.sell_amount:
                new_order.filled = datetime.now()
                existing_order.filled = datetime.now()
                existing_order.counterparty_id = new_order.id
                new_order.counterparty_id = existing_order.id

                if new_order.buy_amount < existing_order.sell_amount:
                    remaining_sell = existing_order.sell_amount - new_order.buy_amount
                    remaining_buy =  remaining_sell/(existing_order.sell_amount / existing_order.buy_amount)
                    new_order = Order(sender_pk=existing_order.sender_pk, receiver_pk=existing_order.receiver_pk,
                                      buy_currency=existing_order.buy_currency,
                                      sell_currency=existing_order.sell_currency, buy_amount=remaining_buy,
                                      sell_amount=remaining_sell, creator_id=existing_order.id, filled=None)
                    session.add(new_order)
                    session.commit()
                elif new_order.buy_amount>existing_order.sell_amount :
                    remaining_buy = new_order.buy_amount - existing_order.sell_amount
                    remaining_sell = remaining_buy/(new_order.buy_amount/ new_order.sell_amount)
                    new_order = Order(sender_pk=new_order.sender_pk,receiver_pk=new_order.receiver_pk,
                                        buy_currency=new_order.buy_currency, sell_currency=new_order.sell_currency,
                                        sell_amount= remaining_sell, buy_amount=remaining_buy, creator_id=new_order.id, filled=None)
                    session.add(new_order)
                    session.commit()

                else:
                    # exact amount,no child
                    new_order = None
                break
        return


@app.route('/trade', methods=['POST'])
def trade():
    print("In trade endpoint")
    if request.method == "POST":
        content = request.get_json(silent=True)
        print( f"content = {json.dumps(content)}" )
        columns = [ "sender_pk", "receiver_pk", "buy_currency", "sell_currency", "buy_amount", "sell_amount", "platform" ]
        fields = [ "sig", "payload" ]

        for field in fields:
            if not field in content.keys():
                print( f"{field} not received by Trade" )
                print( json.dumps(content) )
                log_message(content)
                return jsonify( False )
        
        for column in columns:
            if not column in content['payload'].keys():
                print( f"{column} not received by Trade" )
                print( json.dumps(content) )
                log_message(content)
                return jsonify( False )
            
        #Your code here
        #Note that you can access the database session using g.session


        signature = content['sig']
        payload = json.dumps(content['payload'])
        sender_pk = content['payload']['sender_pk']
        receiver_pk = content['payload']['receiver_pk']
        buy_currency = content['payload']['buy_currency']
        sell_currency = content['payload']['sell_currency']
        buy_amount = content['payload']['buy_amount']
        sell_amount = content['payload']['sell_amount']
        platform = content['payload']['platform']
        # TODO: Check the signature
        if platform == 'Ethereum':
            eth_encoded_msg = eth_account.messages.encode_defunct(text=payload)
            if eth_account.Account.recover_message(eth_encoded_msg, signature=signature) == sender_pk:
                # TODO: Fill the order
                process_order(Order(sender_pk=sender_pk, receiver_pk=receiver_pk, buy_currency=buy_currency,sell_currency=sell_currency, buy_amount=buy_amount, sell_amount=sell_amount,
                                    signature=signature))
                return jsonify(True)
            else:
                log_message(content)
                return jsonify(False)
        elif platform == 'Algorand':
            if algosdk.util.verify_bytes(payload.encode('utf-8'), signature, sender_pk):
                # TODO: Fill the order
                process_order(Order(sender_pk=sender_pk, receiver_pk=receiver_pk, buy_currency=buy_currency,sell_currency=sell_currency, buy_amount=buy_amount, sell_amount=sell_amount,
                                    signature=signature))
                return jsonify(True)
            else:
                log_message(content)
                return jsonify(False)

        

@app.route('/order_book')
def order_book():
    #Your code here
    #Note that you can access the database session using g.session
    orders = g.session.query(Order).filter().all()
    lst = []

    for o in orders:
        order = {}
        order['sender_pk'] = o.sender_pk
        order['receiver_pk'] = o.receiver_pk
        order['buy_currency'] = o.buy_currency
        order['sell_currency'] = o.sell_currency
        order['buy_amount'] = o.buy_amount
        order['sell_amount'] = o.sell_amount
        order['signature'] = o.signature
        lst.append(order)
    result = {}
    result['data'] = lst
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')

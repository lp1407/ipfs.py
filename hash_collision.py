import hashlib
import string
import random


def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    #if k > 256:
        #return( b'\x00',b'\x00' )
    #Collision finding code goes here
    terminate = 256 #end_length = terminate 
    Converse =  True #notEqual= Converse
    while(Converse):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        y = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        var_x = hashlib.sha256(x) #hx = var_x
        var_y = hashlib.sha256(y)  #hy = var_y
        #compute hash in hex
        var_x_num = var_x.hexdigest()   #hx16 = var_x_num
        var_y_num = var_y.hexdigest()    #hy16 = var_y_num
        #convert hex into binary string
        var_x2 = bin(int(var_x_num, 16))[2:].zfill(terminate) #hx2 = var_x2
        var_y2 = bin(int(var_y_num, 16))[2:].zfill(terminate) #hy2 = var_y2
        varx_end = var_x2[-k:]                        #hx_trailing = varx_end
        #print("x:", hx_trailing)
        hy_trailing = var_y2[-k:]                        #vary_end
        #print("y:", hy_trailing)
        if varx_end == vary_end:
            Converse = False
    
    return( x, y )

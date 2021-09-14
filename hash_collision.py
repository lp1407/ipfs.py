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
  
    #Collision finding code goes here
    terminate = 256 
    Converse =  True 
    while(Converse):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        y = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        var_x = hashlib.sha256(x) 
        var_y = hashlib.sha256(y)  
      
        var_x_num = var_x.hexdigest() 
        var_y_num = var_y.hexdigest()   
       
        var_x2 = bin(int(var_x_num, 16))[2:].zfill(terminate)
        var_y2 = bin(int(var_y_num, 16))[2:].zfill(terminate) 
        varx_end = var_x2[-k:]                        
  
        vary_end = var_y2[-k:]                      
      
        if varx_end == vary_end:
            Converse = False
    
    return( x, y )

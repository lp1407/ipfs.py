def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
    if k > 256:
        print( "Specify a smaller number" )
        return( b'\x00',b'\x00' )
    #Collision finding code goes here
    end_length = 256
    notEqual =  True
    while(notEqual):
        x = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        y = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 50)).encode('utf-8')
        hx = hashlib.sha256(x)
        hy = hashlib.sha256(y)
        #compute hash in hex
        hx16 = hx.hexdigest()
        hy16 = hy.hexdigest()
        #convert hex into binary string
        hx2 = bin(int(hx16, 16))[2:].zfill(end_length)
        hy2 = bin(int(hy16, 16))[2:].zfill(end_length)
        hx_trailing = hx2[-k:]
        #print("x:", hx_trailing)
        hy_trailing = hy2[-k:]
        #print("y:", hy_trailing)
        if hx_trailing == hy_trailing:
            notEqual = False
    
    return( x, y )

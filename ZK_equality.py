from zksk import Secret, DLRep
from zksk import utils

def ZK_equality(G,H):

    #Generate two El-Gamal ciphertexts (C1,C2) and (D1,D2)
    generate1 = Secret(utils.get_random_num(bits=128))
    generate2 = Secret(utils.get_random_num(bits=128))
    eql = Secret(utils.get_random_num(bits=128))

    req1 = generate1.value * G
    req2 = generate1.value * H + eql.value * G
    meg1 = generate2.value * G
    meg2 = generate2.value * H + eql.value * G

    writt = DLRep(req1,generate1*G) & DLRep(req2,generate1*H+eql*G) & DLRep(meg1,generate2*G) & DLRep(meg2,generate2*H+eql*G)

    #Generate a NIZK proving equality of the plaintexts
    zk_proof = writt.prove()
    writt.verify(zk_proof)

    #Return two ciphertexts and the proof
    return (req1,req2), (meg1,meg2), zk_proof

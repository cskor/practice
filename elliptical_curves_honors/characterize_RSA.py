"""
Author: Cassidy Skorczewski
Project: Characterizing RSA and ECC Cryptosystems
"""
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA

from ecies.utils import generate_eth_key
from fastecdsa import keys, curve,ecdsa

from matplotlib import pyplot as plt
import time

def generateKeysRSA(bitLength):
    """This function generates keys needed for RSA 
            Input:
                bitLength: key bit length
            Outputs:
                private, public keys of RSA
    """
    random_generator = Random.new().read
    key = RSA.generate(bitLength, random_generator)
    return key

def recordTimesRSA(sizes, message):
    """ This function documents the times taken
        to generate the key, encrypt, and decrypt using
        the RSA cryptosystem
            Inputs:
                sizes: RSA key sizes
                message: message to encrypt
            Outputs:
                keyTime, encryptTime, decryptTime: times taken to do task
    """
    keyTime, encryptTime, decryptTime = [], [], []
    for size in sizes:
        print("Starting Size: ", size)
        startK = time.time()
        key = generateKeysRSA(size)
        endK = time.time()
        keyTime.append((endK-startK))
        
        startE = time.time()
        hMessage = SHA.new(message).digest()
        signature = key.sign(hMessage, "")
        endE = time.time()
        encryptTime.append((endE-startE))
        
        startD = time.time()
        key.verify(hMessage, signature)
        endD = time.time()
        decryptTime.append((endD - startD))
    
    return keyTime, encryptTime, decryptTime

def graph(RSA, ECC, title):
    """This function graphs the RSA vs ECC times taken to do a certain task
            Inputs:
                    RSA: RSA timing data
                    ECC: ECC timing data
                    title: title of your graph
    """
    x = [0,1,2,3,4]
    plt.plot(x, RSA, '--', label="RSA Values")
    plt.plot(x, ECC, '--', label="ECC Values")
    plt.legend()
    plt.title(title)
    plt.xticks(x, ['160/1024', '224/2048', '256/3072', '384/7680', '521/15360'])
    plt.xlabel('ECC/RSA Key Size (bits)')
    plt.ylabel('Time (seconds)')
    plt.grid()
    plt.show()
    
def generateKeysECC():
    """This function generates keys needed for ECC 
            Input:
                bitLength: key bit length
            Outputs:
                private, public keys of ECC
    """
    key = generate_eth_key()
    return key.to_hex(), key.public_key.to_hex()

def recordTimeECC(sizes, message):
    """ This function documents the times taken to generate the 
            key, encrypt, and decrypt using the ECC cryptosystem
            Inputs:
                sizes: ECC key sizes
                message: message to encrypt
            Outputs:
                keyTime, encryptTime, decryptTime: times taken to do task
    """
    keyTime, encryptTime, decryptTime = [], [], []
    for size in sizes:
        print("Starting Size: ", size)
        startK = time.time()
        priv_key, pub_key = keys.gen_keypair(size) 
        endK = time.time()
        keyTime.append((endK-startK))
        
        startE = time.time()
        (r,s) = ecdsa.sign(message,priv_key, size)
        endE = time.time()
        encryptTime.append((endE-startE))
        
        startD = time.time()
        ecdsa.verify((r,s),message,pub_key, size)
        endD = time.time()
        decryptTime.append((endD - startD))
    
    return keyTime, encryptTime, decryptTime

def characterizeResults(message):
    """ This function runs the ECC and RSA timing data and plots the results
            Inputs:
                message: the message you want to encrypt
    """
    rsaKeySizes = [1024, 2048, 3072, 7680, 15360]
    eccKeySizes = [curve.brainpoolP160r1, curve.P224, curve.P256 , curve.P384, curve.P521]
    
    kTRSA, eTRSA, dTRSA = recordTimesRSA(rsaKeySizes, str.encode(message))
    kTECC, eTECC, dTECC = recordTimeECC(eccKeySizes, message)
    
    graph(kTRSA, kTECC, 'Generate Keys')
    graph(eTRSA, eTECC, 'Encryption')
    graph(dTRSA, dTECC, 'Decryption')

if __name__ == "__main__":
    message = 'This is my presentation on Elliptical Curve Cryptography.'
    
    characterizeResults(message)


    



    
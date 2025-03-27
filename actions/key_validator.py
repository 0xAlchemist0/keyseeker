from bitcoinlib.keys import Key
from bitcoinlib.wallets import Service, Wallet

from actions.conv import wif_to_private_key


#wif is the private key
def analyze_list(key_list):
    # validate_key(key_list[0]['wif'])
    for index, item in enumerate(key_list):
       current_private_key = wif_to_private_key(item['wif']) 
       print(f"#{index}: {current_private_key}")
       pub_key = get_pub_key(current_private_key)
       check_balance(pub_key)
       
    return None

def validate_key(priv_key):
    wallet_name = 'test'
    pubkey = Key(priv_key)
    # print(pubkey.address)
    # test = Key(pubkey.address)
    # print(f"Pub: {test.address}")
    return None

#the address returned is a legacy addresss
def get_pub_key(priv_key):
     wallet = Key(import_key=priv_key)
     print(f"Address: {wallet.address()}")
     return wallet.address()

def check_balance(pub_key):
    service = Service(network='bitcoin')
    print(f"Balance: {service.getbalance(pub_key)}")
    return None
    

#we must convert the wif to ex (hex format is the private key to import)

# from bitcoinlib.keys import Key

# # Public key in hex format
# public_key_hex = "045e95bb399a6971d376026947f89bde2f282b33810928be4ded112ac4d70e20d539f23f366809085beebfc71181313775a99c9aed7d8ba38b161384c746012865"

# # Create a key object using the public key
# key = Key(public_hex=public_key_hex)

# # Get the corresponding Bitcoin address
# address = key.address

# print("Bitcoin Address:", address)

#
import hashlib

#used for encoding and decoding base 58 data
import base58


#the -> means the function returns a string value
#wif: str means wif must be string to bea able to call this function
def wif_to_private_key(wif: str) -> str:
    decoded = base58.b58decode_check(wif)  # Decode Base58Check in its original byte format
    #the decoded results in a byte sequence first byte likes 0x80 and the rezst 32 bytes and sometiems an optional last bye like 0x01
    #remove decoded values prefixes and optional suffix
    #if length 32 means 1 byte for prefix 32 bytes of private key and 1 byte for compressed bag (sometimes happens sometimes doesnt
    
    # else only first byte and 32 bytes
    private_key = decoded[1:-1] if len(decoded) == 34 else decoded[1:]  # Remove prefix (0x80) and optional suffix (0x01)
    #converts the private key to hex format
    return private_key.hex().upper()


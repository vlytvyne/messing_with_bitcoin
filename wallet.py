import hashlib
import base58check
import secrets

privkey = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D"

def	convert_to_wif(privkey: str) -> str:
	'''Convert hex represntation of priv key to wif'''
	if len(privkey) != 64:
		print("Private key is not valid")
		return None
	privkey.upper()
	wif = "80" + privkey
	checksum = hashlib.sha256(wif.encode('ascii')).hexdigest()
	checksum = hashlib.sha256(checksum.encode('ascii')).hexdigest()
	checksum = checksum[:8].upper()
	wif = wif + checksum
	wif = base58check.b58encode(bytes.fromhex(wif))
	wif = wif.decode('ascii')
	return wif

def	generate_priv_key() -> str:
	'''Generate a private key in hex representation'''
	bits = secrets.randbits(256)
	privkey = hex(bits)[2:].upper()
	return (privkey)
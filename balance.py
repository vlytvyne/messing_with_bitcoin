from slickrpc import Proxy
from getopt import getopt, GetoptError
import sys

ANSI_RED_BOLD = "\x1b[31;1m"
ANSI_MAGENTA_BOLD = "\x1b[35;1m"
ANSI_GREEN_BOLD = "\x1b[32;1m"
ANSI_EOC = "\x1b[0m"

try:
	options, args = getopt(sys.argv[1:], "vd")
except GetoptError:
	print("Usage: py balance.py [-vd]")
	print(" -v - verbose - list addresses and their balances as well as total balance.")
	print(" -d - dump    - dump private key for each address. Works only if 'v' option is set.")
	sys.exit(0)
del args
list_options = [opt for opt, arg in options]

rpcuser = "vlytvyne"
rpcpasswd = "E83FB0B56BF7A2AAAA7989D478AA9845BACADA22F2CA447F5DEEA327EF7DB059"
proxy_address = "http://%s:%s@127.0.0.1:18332"%(rpcuser, rpcpasswd)

bitcoin = Proxy(proxy_address)
balance = bitcoin.getbalance()

print("Total balance is:", ANSI_GREEN_BOLD, balance, ANSI_EOC)

if "-v" in list_options:
	records = bitcoin.listreceivedbyaddress()
	for record in records:
		print("-----------------------------------------------------------")
		print("At address:", ANSI_MAGENTA_BOLD,record['address'], ANSI_EOC, "-", record['amount'])
		if "-d" in list_options:
			print("Corresponding priv key:", ANSI_RED_BOLD, bitcoin.dumpprivkey(record['address']), ANSI_EOC)

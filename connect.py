# 블록체인 접속
from web3 import Web3
from dotenv import load_dotenv
import os
load_dotenv()

infura_url = os.environ.get("MAIN_NET")
web3 = Web3(Web3.HTTPProvider(infura_url))
print("- Connection : ", web3.isConnected())
 
print("- Current Block No.: ", web3.eth.block_number)
balance = web3.eth.getBalance(os.environ.get("WALLET"))
print("- balance : ", balance)
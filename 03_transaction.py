from web3 import Web3
 
ganache_url = "http://ganache:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
 
print("\n[ --- Ganache Local BlockChain --- ]")
print(" - Connection    : ", web3.isConnected())
print(" - Current Block : ", web3.eth.block_number)
 
account_sending = "0x6b2746c2b6Ae21eD903aC2dB03bc9412CDE8F3D2"
account_receiving = "0x815B993FD442277D37f1D09Db12109aE883b7196"
 
# to sign a transaction
private_key = "0x77f57af53616274c8b84df7fd0b38cdffdfa5c419bdc7cf3cfb327c46d71819a"
 
# build - sign - send - get transaction hash
nonce = web3.eth.getTransactionCount(account_sending)
tx = {
    'nonce': nonce,
    'to': account_receiving,
    'value': web3.toWei(3, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
 
signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)
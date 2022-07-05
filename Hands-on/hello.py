from web3 import Web3, HTTPProvider
import json
blockchain_address = 'http://127.0.0.1:9545'

web3 = Web3(HTTPProvider(blockchain_address))

web3.eth.defaultAccount = web3.eth.accounts[0]
print(web3.eth.defaultAccount)

#Application Binary Interface

compiled_contract_path = 'build/contracts/hello.json'

# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x645e911F16D22f8423fD79a4d565c32F139A8F28'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    
# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

a = contract.functions.input(1,2,3).transact()
print(a)

b = contract.functions.sum1.call()
print(b)

c = contract.functions.sub1.call()
print(c)

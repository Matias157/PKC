import json
from solcx import compile_standard
from web3 import Web3

# reading Solidity code
with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

# compiling the code
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "metadata",
                        "evm.bytecode",
                        "evm.sourceMap",
                    ]
                }
            }
        },
    },
    solc_version="0.8.12",
)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

# getting the bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# getting the abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connecting to Ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
private_key = "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"

# Creating the contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Getting the nonce
nonce = w3.eth.getTransactionCount(my_address)

# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce}
)
signed_tx = w3.eth.account.sign_transaction(transaction, private_key=private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

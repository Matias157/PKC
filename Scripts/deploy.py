import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from Crypto.PublicKey import RSA

# reading compiled code
with open("../Data/CompiledFiles/compiled_public_key_chain_factory.json") as file:
    compiled_sol = json.load(file)

# getting the bytecode
bytecode = compiled_sol["contracts"]["PublicKeyChainFactory.sol"][
    "PublicKeyChainFactory"
]["evm"]["bytecode"]["object"]

# getting the abi
abi = compiled_sol["contracts"]["PublicKeyChainFactory.sol"]["PublicKeyChainFactory"][
    "abi"
]

# connecting to the chain
w3 = Web3(
    Web3.HTTPProvider("https://goerli.infura.io/v3/dc9e2171b6064e9b9a577689a90e9355")
)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
chain_id = 5
my_address = "0x07A9CF7790300E884C35A97041059e2941B9EaB6"
private_key = "0xb4a16213105152e39d3286708cef85e47e75736ec5c0db1790a4849b7e8e5471"

# Creating the contract
# 0xf37Db4653204b036c6c2B624025093c31D6a6c68
public_key_chain_factory = w3.eth.contract(
    address="0x84d9F8B13887D16641Eb96e92d1fb8B4f4092820", abi=abi, bytecode=bytecode
)

# Getting the nonce
nonce = w3.eth.getTransactionCount(my_address)

# 1. Build a transaction
# 2. Sign a transaction
# 3. Send a transaction

PublicKeyChainFactory = w3.eth.contract(abi=abi, bytecode=bytecode)
transaction = PublicKeyChainFactory.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)
print("Deploying Contract!")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
print("Waiting for transaction to finish...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Done! Contract deployed to {tx_receipt.contractAddress}")


"""for i in range(3):
    pubKey = "-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4SD0YSMWYAU27mFVKsHgtKWzM\n9jfvs2Xl+zCQpAHNtvYWTo6mnyWTwH4lGn7ulYdGx5gAJj6OlWg+CKoHXqPOh6e4\nP8DM97dM9QfP8d7el2ZCz1+5oMd8iQo+WPTM1qa5TMj9rZMpwAnSrS490LW6ZpTL\n7fChg3APljnspQ/7nQIDAQAB\n-----END PUBLIC KEY-----"
    greeting_transaction = (
        public_key_chain_factory.functions.createPublicKeyChainContract(
            "https://www.google.com.br", pubKey.encode("utf-8")
        ).buildTransaction(
            {
                "chainId": chain_id,
                "from": my_address,
                "nonce": nonce + (2 * i),
            }
        )
    )
    signed_greeting_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=private_key
    )
    tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)
    print("Creating PublicKeyChain...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)
    print("Created!")

    greeting_transaction = public_key_chain_factory.functions.fAddAtribute(
        "0x07A9CF7790300E884C35A97041059e2941B9EaB6",
        "Date of birth",
        str(i) + "/" + str(i) + "/" + str(i),
    ).buildTransaction(
        {
            "chainId": chain_id,
            "from": my_address,
            "nonce": nonce + (2 * i + 1),
        }
    )
    signed_greeting_txn = w3.eth.account.sign_transaction(
        greeting_transaction, private_key=private_key
    )
    tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)
    print("Adicionando atributo...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)
    print("Adicionado!")"""


"""greeting_transaction = public_key_chain_factory.functions.fVote(
    "0x07A9CF7790300E884C35A97041059e2941B9EaB6"
).buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
signed_greeting_txn = w3.eth.account.sign_transaction(
    greeting_transaction, private_key=private_key
)
tx_greeting_hash = w3.eth.send_raw_transaction(signed_greeting_txn.rawTransaction)
print("Votando...")
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_greeting_hash)
print("Votado!")"""


"""num = public_key_chain_factory.functions.getKeysCount().call()
print("Numero de chaves armazenadas = " + str(num))
output = []
for i in range(num):
    # print("Chave #" + str(i))
    stored_value = public_key_chain_factory.functions.fGetAllInfo(i).call()
    output.append(stored_value)
    # print(str(stored_value))
print(output)"""


"""stored_value = public_key_chain_factory.functions.fQuery(
    "https://www.google.com.br/"
).call()
print(stored_value)
num = len(stored_value)
print("Numero de chaves armazenadas = " + str(num))
output = []
for i in range(num):
    # print("Chave #" + str(i))
    stored_value = public_key_chain_factory.functions.fGetAllInfo(
        stored_value[i]
    ).call()
    output.append(stored_value)
    # print(str(stored_value))
print(output)"""

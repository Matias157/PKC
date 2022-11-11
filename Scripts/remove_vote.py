import json
from web3 import Web3
from web3.middleware import geth_poa_middleware


class RemoveVote(object):
    def __init__(self, address, endpoint, priv_key):
        with open("Data/CompiledFiles/compiled_public_key_chain_factory.json") as file:
            compiled_sol = json.load(file)

        self.bytecode = compiled_sol["contracts"]["PublicKeyChainFactory.sol"][
            "PublicKeyChainFactory"
        ]["evm"]["bytecode"]["object"]

        self.abi = compiled_sol["contracts"]["PublicKeyChainFactory.sol"][
            "PublicKeyChainFactory"
        ]["abi"]

        self.w3 = Web3(Web3.HTTPProvider(endpoint))

        self.chain_id = 5
        self.address = address
        self.private_key = priv_key
        self.nonce = self.w3.eth.getTransactionCount(self.address)

    def remove_vote(self, address):
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        public_key_chain_factory = self.w3.eth.contract(
            address="0x6De305f48aB253a92854dd04262a625450391A6E",
            abi=self.abi,
            bytecode=self.bytecode,
        )

        try:
            greeting_transaction = public_key_chain_factory.functions.fRemoveVote(
                address
            ).buildTransaction(
                {
                    "chainId": self.chain_id,
                    "from": self.address,
                    "nonce": self.nonce,
                }
            )

            signed_greeting_txn = self.w3.eth.account.sign_transaction(
                greeting_transaction, private_key=self.private_key
            )

            tx_greeting_hash = self.w3.eth.send_raw_transaction(
                signed_greeting_txn.rawTransaction
            )

            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_greeting_hash)
            return [True]
        except Exception as e:
            return [False, e]

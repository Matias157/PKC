import json
from web3 import Web3
from web3.middleware import geth_poa_middleware


class VotedList(object):
    def __init__(self, endpoint):
        with open("Data/CompiledFiles/compiled_public_key_chain_factory.json") as file:
            compiled_sol = json.load(file)

        self.bytecode = compiled_sol["contracts"]["PublicKeyChainFactory.sol"][
            "PublicKeyChainFactory"
        ]["evm"]["bytecode"]["object"]

        self.abi = compiled_sol["contracts"]["PublicKeyChainFactory.sol"][
            "PublicKeyChainFactory"
        ]["abi"]

        self.w3 = Web3(Web3.HTTPProvider(endpoint))

    def voted_list(self, address):
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        public_key_chain_factory = self.w3.eth.contract(
            address="0x6De305f48aB253a92854dd04262a625450391A6E",
            abi=self.abi,
            bytecode=self.bytecode,
        )

        output = []
        try:
            stored_value = public_key_chain_factory.functions.fGetVotedList(
                address
            ).call()
        except Exception as e:
            return [False, e]
        output.append(stored_value)

        return output

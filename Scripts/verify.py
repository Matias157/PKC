import json
from web3 import Web3
from web3.middleware import geth_poa_middleware


class Verify(object):
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

    def verify(self, url):
        self.w3.middleware_onion.inject(geth_poa_middleware, layer=0)

        public_key_chain_factory = self.w3.eth.contract(
            address="0x5756EcDa3B442B1aA90e90bdD8E6D916Bb15CB63",
            abi=self.abi,
            bytecode=self.bytecode,
        )

        try:
            stored_value = public_key_chain_factory.functions.fQuery(url).call()
        except Exception as e:
            return [False, e]

        num = len(stored_value)
        output = []
        for i in range(num):
            try:
                stored_value = public_key_chain_factory.functions.fGetAllInfo(
                    stored_value[i]
                ).call()
            except Exception as e:
                return [False, e]
            output.append(stored_value)

        return output

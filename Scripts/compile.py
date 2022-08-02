import json
from solcx import compile_standard

class Compile(object):
    def compilePublicKeyChain(self):
        # reading Solidity code
        with open("Contracts/PublicKeyChain.sol", "r") as file:
            public_key_chain_file = file.read()

        # compiling the code
        compiled_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {"PublicKeyChain.sol": {"content": public_key_chain_file}},
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
            base_path="Contracts",
        )

        with open("Data/CompiledFiles/compiled_public_key_chain.json", "w") as file:
            json.dump(compiled_sol, file)

    def compilePublicKeyChainFactory(self):
        # reading Solidity code
        with open("Contracts/PublicKeyChainFactory.sol", "r") as file:
            public_key_chain_factory_file = file.read()

        # compiling the code
        compiled_sol = compile_standard(
            {
                "language": "Solidity",
                "sources": {
                    "PublicKeyChainFactory.sol": {"content": public_key_chain_factory_file}
                },
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
            base_path="Contracts",
        )

        with open("Data/CompiledFiles/compiled_public_key_chain_factory.json", "w") as file:
            json.dump(compiled_sol, file)

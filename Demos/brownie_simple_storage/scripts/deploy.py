from brownie import accounts, StorageFactory, config, network, Contract


def deployContract():
    account = getAccount()
    """storage_factory = StorageFactory.deploy({"from": account})
    transaction = storage_factory.createSimpleStorageContract({"from": account})
    transaction.wait(1)
    stored_value = storage_factory.sfGet(0)
    print(stored_value)
    transaction = storage_factory.sfStore(0, 69, {"from": account})
    updated_stored_value = storage_factory.sfGet(0)
    print(updated_stored_value)"""
    storage_factory = Contract.from_abi(
        "StorageFactory",
        "0x663539Ac937327326af429E7C7DA0123f1E61A97",
        StorageFactory.abi,
    )
    """transaction = storage_factory.createSimpleStorageContract(
        "Alexandre", 13, {"from": account}
    )
    transaction.wait(1)
    transaction = storage_factory.createSimpleStorageContract(
        "Du", 17, {"from": account}
    )
    transaction.wait(1)"""
    stored_value = storage_factory.sfGetName("Alexandre", {"from": account})
    print("O nome de Alexandre = " + stored_value)
    stored_value = storage_factory.sfGetFavoriteNumber("Alexandre", {"from": account})
    print("O numero favorito de Alexandre = " + str(stored_value))
    stored_value = storage_factory.sfGetName("Du", {"from": account})
    print("O nome de Du = " + stored_value)
    stored_value = storage_factory.sfGetFavoriteNumber("Du", {"from": account})
    print("O numero favorito de Du = " + str(stored_value))


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("demo-account")


def main():
    deployContract()


if __name__ == "__main__":
    main()

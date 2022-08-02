from brownie import SimpleStorage, accounts, config


def readContract():
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())


def main():
    readContract()


if __name__ == "__main__":
    main()

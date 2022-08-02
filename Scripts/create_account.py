import csv
import hashlib
import pandas as pd
from Scripts.encrypt import AES_encrypt

class CreateAccount(object):
    def __init__(self, address, endpoint, password):
        crypt = AES_encrypt(password)
        self.address = address
        self.endpoint = crypt.encrypt(endpoint).decode('utf-8')
        self.password = hashlib.sha256(hashlib.sha256(password.encode()).hexdigest().encode()).hexdigest()

    def createAccount(self):
        if not self.verifyUser():
            with open('Data/UserData/accounts.csv', 'a+', newline='') as database:
                databasewriter = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                databasewriter.writerow([self.address, self.endpoint, self.password])
            return True
        else: 
            return False

    def verifyUser(self):
        col_list = ["address", "endpoint", "password"]
        df = pd.read_csv("Data/UserData/accounts.csv", usecols=col_list)
        for row in df["address"]:
            if self.address == row:
                return True
        return False

if __name__ == "__main__":
    acc = CreateAccount("0x07A9CF7790300E884C35A97041059e2941B9EaB6", "https://rinkeby.infura.io/v3/dc9e2171b6064e9b9a577689a90e9355", "abc123")
    if acc.createAccount():
        print("User Created!")
    else:
        print("User already exists!")
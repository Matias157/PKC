import hashlib
import pandas as pd
from Scripts.encrypt import AES_encrypt

class Login(object):
    def __init__(self, address, password):
        self.address = address
        self.password = hashlib.sha256(hashlib.sha256(password.encode()).hexdigest().encode()).hexdigest()
        self.crypt = AES_encrypt(password)

    def login(self):
        data = pd.read_csv("Data/UserData/accounts.csv", index_col="address")
        if self.verifyUser():
            if data.loc[self.address][1] != self.password:
                self.address = ""
                self.password = ""
                self.crypt = ""
                return False
            else:
                self.endpoint = self.crypt.decrypt(data.loc[self.address][0].encode())
                return True
        else:
            self.address = ""
            self.password = ""
            self.crypt = ""
            return False

    def verifyUser(self):
        col_list = ["address", "endpoint", "password"]
        df = pd.read_csv("Data/UserData/accounts.csv", usecols=col_list)
        for row in df["address"]:
            if self.address == row:
                return True
        return False

if __name__ == "__main__":
    login = Login("0x07A9CF7790300E884C35A97041059e2941B9EaB6", "abc123")
    if login.login():
        print(login.address)
        print(login.password)
        print(login.endpoint)
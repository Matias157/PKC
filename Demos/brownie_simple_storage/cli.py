import sys
import pexpect

password = "alerei1998"

child = pexpect.spawn("brownie run scripts/deploy.py --network rinkeby")
i = child.expect([pexpect.TIMEOUT, "Enter password for"])
if i == 0:
    print("Got unexpected output: %s %s" % (child.before, child.after))
    sys.exit()
else:
    child.sendline(password)

temp = child.read()
print(temp.decode("utf-8"))

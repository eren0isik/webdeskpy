# test.py
from __init__ import *

a = Greap(uiloc="/", title="Test")
a.app.secret_key = os.urandom(24)

@a.app.route("/")
def home():
    return "hello"

if __name__ == "__main__":
    a.start()

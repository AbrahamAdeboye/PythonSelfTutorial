import random
import string
from math import *

# This is a python file that explains most basic functions, tags, snippet and syntax. Be sure you understand this
# before moving on to the advanced "coded" file. 
# You can visit this link to learn more >> "https://www.python.org/about/gettingstarted/"


print("Hello baby, Let's get started in Programming with Pyhton3")


def generate_transaction_code():
    letters = string.ascii_uppercase
    digits = string.digits
    code = ''.join(random.choice(letters + digits) for i in range(12))
    return code
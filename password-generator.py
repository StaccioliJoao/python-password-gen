import random
import string
import requests
import hashlib


def lookup(password):
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    url = 'https://api.pwnedpasswords.com/range/' + head
    res = requests.get(url)

    hashes = (line.split(':') for line in res.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail), 0)
    return count


lower_case = string.ascii_letters
upper_case = lower_case.upper()
numbers = string.digits
symbols = '~!@#$%^&*()-=_+[]{}|\\;\',./<>?'
upper, lower, nums, syms = False, False, False, False

upper_bool = input("Do you want upper case letters? (Y/N)")
lower_bool = input("Do you want lower case letters? (Y/N)")
num_bool = input("Do you want numbers? (Y/N)")
syms_bool = input("Do you want symbols? (Y/N)")
seed_bool = input(
    "Do you want to use a seed so you can generate the same passwords at a later time? (Y/N)")

upper_bool.upper()
lower_bool.upper()
num_bool.upper()
syms_bool.upper()
seed_bool.upper()

if seed_bool == 'Y':
    seed = input("What seed do you want?")
    random.seed(seed)

if upper_bool == 'Y':
    upper = True

if lower_bool == 'Y':
    lower = True

if num_bool == 'Y':
    nums = True

if syms_bool == 'Y':
    syms = True

choices = ""

if upper:
    choices += upper_case
if lower:
    choices += lower_case
if nums:
    choices += numbers
if syms:
    choices += symbols

genned_passwords = []

password_length = int(input("What is the size of the password you want?"))
password_amount = int(input("How many passwords do you want?"))
for x in range(password_amount):
    password = "".join(random.sample(choices, password_length))
    genned_passwords.append(password)

for i in genned_passwords:
    count = lookup(i)
    if count:
        genned_passwords.remove(i)
    else:
        print("Brand New Password checked by pwned API:", i)

import random
import string

lower_case = string.ascii_letters
upper_case = lower_case.upper()
numbers = string.digits
symbols = string.punctuation

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
else:
    upper = False

if lower_bool == 'Y':
    lower = True
else:
    lower = False

if num_bool == 'Y':
    nums = True
else:
    nums = False

if syms_bool == 'Y':
    syms = True
else:
    syms = False


choices = ""

if upper:
    choices += upper_case
if lower:
    choices += lower_case
if nums:
    choices += numbers
if syms:
    choices += symbols


password_length = int(input("What is the size of the password you want?"))
password_amount = int(input("How many passwords do you want?"))

for x in range(password_amount):
    password = "".join(random.sample(choices, password_length))
    print(password)

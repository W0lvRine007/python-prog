import random
from typing import ValuesView

from high_low_art import logo, vs
from hl_data import data

print(logo)

def format_data(account):
    account_name = account['name']
    account_desc = account['description']
    account_coun = account['country']
    print(f"{account_name}, a {account_desc}, from {account_coun}")

score = 0

account_foll = account['follower_count']


def account_comp(account):
    account_foll > account
    score += 1
    print("correct answer, your score is {score}")


account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b :
    account_b = random.choice(data)


format_data(account_a)

print(vs)

format_data(account_b)

user_input = input("type 'a' for selecting first option or type 'b' for selecting second option\n").lower()
if user_input == 'a':
    account_foll = account_a
    account_comp()
else:

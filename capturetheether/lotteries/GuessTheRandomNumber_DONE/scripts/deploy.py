#!/usr/bin/python3
from random import randint

from brownie import GuessTheRandomNumberChallenge
from scripts.helpful_scripts import get_account

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


def deploy():
    owner, _ = get_account()
    c = GuessTheRandomNumberChallenge.deploy({"from": owner, "value": "1 ether"})
    # to make some transations
    for i in range(randint(10, 20)):
        owner.transfer(ZERO_ADDRESS, amount="0.1 ether").wait(1)

    return c, owner


def main():
    deploy()

#!/usr/bin/python3
from brownie import TokenBankChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, attacker = get_account()
    c = TokenBankChallenge.deploy(attacker.address, {"from": owner})

    return c, owner


def main():
    deploy()

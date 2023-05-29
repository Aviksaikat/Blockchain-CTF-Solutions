#!/usr/bin/python3
from brownie import RetirementFundChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, attacker = get_account()
    c = RetirementFundChallenge.deploy(attacker, {"from": owner, "value": "1 ether"})

    return c, owner, attacker


def main():
    deploy()

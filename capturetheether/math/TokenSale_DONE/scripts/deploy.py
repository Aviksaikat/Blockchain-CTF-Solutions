#!/usr/bin/python3
from brownie import TokenSaleChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, player = get_account()
    c = TokenSaleChallenge.deploy(player, {"from": owner, "value": "1 ether"})

    return c, owner


def main():
    deploy()

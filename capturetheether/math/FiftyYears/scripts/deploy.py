#!/usr/bin/python3
from brownie import FiftyYearsChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, player = get_account()
    c = FiftyYearsChallenge.deploy(player.address, {"from": owner, "value": "1 ether"})

    return c, owner, player


def main():
    deploy()

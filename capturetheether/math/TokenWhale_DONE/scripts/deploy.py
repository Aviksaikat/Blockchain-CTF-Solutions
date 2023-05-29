#!/usr/bin/python3
from brownie import TokenWhaleChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, player, player2 = get_account()
    c = TokenWhaleChallenge.deploy(player, {"from": owner})

    return c, owner, player, player2


def main():
    deploy()

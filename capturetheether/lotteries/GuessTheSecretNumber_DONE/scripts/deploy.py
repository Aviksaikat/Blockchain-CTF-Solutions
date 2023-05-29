#!/usr/bin/python3
from brownie import GuessTheSecretNumberChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = GuessTheSecretNumberChallenge.deploy({"from": owner, "value": "1 ether"})

    return c, owner


def main():
    deploy()

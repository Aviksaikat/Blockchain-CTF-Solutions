#!/usr/bin/python3
from brownie import PublicKeyChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = PublicKeyChallenge.deploy({"from": owner})
    owner.transfer("0x0000000000000000000000000000000000000000", "0.1 ether").wait(1)
    owner.transfer(owner.address, "0.1 ether").wait(1)

    return c, owner


def main():
    deploy()

#!/usr/bin/python3
from brownie import GatekeeperTwo
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    gkp2 = GatekeeperTwo.deploy({"from": owner})

    print(f"Contract Deployed to: {gkp2.address}")
    return gkp2, owner


def main():
    deploy()

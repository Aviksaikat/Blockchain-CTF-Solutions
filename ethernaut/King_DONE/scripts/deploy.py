#!/usr/bin/python3
from brownie import King
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    king = King.deploy({"from": owner, "value": "0.01 ether"})
    # owner.transfer(to=king.address, amount="1 ether")

    print(f"Contract Deployed to: {king.address}")
    return king, owner


def main():
    deploy()

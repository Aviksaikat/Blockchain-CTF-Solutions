#!/usr/bin/python3
from brownie import Token
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    # * initialSupply 20
    token = Token.deploy(20, {"from": owner})

    print(f"Contract Deployed to: {token.address}")
    return token, owner


def main():
    deploy()

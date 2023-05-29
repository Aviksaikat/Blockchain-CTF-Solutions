#!/usr/bin/python3
from brownie import Vault
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    # * encode the str into bytes
    passwd = "password".encode()
    vault = Vault.deploy(passwd, {"from": owner})

    print(f"Contract Deployed to: {vault.address}")
    return vault, owner


def main():
    deploy()

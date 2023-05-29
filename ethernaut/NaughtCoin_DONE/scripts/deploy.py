#!/usr/bin/python3
from brownie import NaughtCoin
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    nc = NaughtCoin.deploy(owner, {"from": owner})

    print(f"Contract Deployed to: {nc.address}")
    return nc, owner


def main():
    deploy()

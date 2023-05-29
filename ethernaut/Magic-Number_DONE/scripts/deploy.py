#!/usr/bin/python3
from brownie import MagicNum
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    mc = MagicNum.deploy({"from": owner})

    print(f"Contract Deployed to: {mc.address}")

    return mc, owner


def main():
    deploy()

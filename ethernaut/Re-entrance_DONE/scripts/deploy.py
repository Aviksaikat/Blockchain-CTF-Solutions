#!/usr/bin/python3
from brownie import Reentrance
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    reentrance = Reentrance.deploy({"from": owner})

    print(f"Contract Deployed to: {reentrance.address}")
    return reentrance, owner


def main():
    deploy()

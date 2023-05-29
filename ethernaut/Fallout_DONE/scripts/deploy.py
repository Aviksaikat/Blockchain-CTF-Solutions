#!/usr/bin/python3
from brownie import Fallout
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    fallout = Fallout.deploy({"from": owner})

    print(f"Contract Deployed to {fallout.address}")
    return fallout, owner


def main():
    deploy()

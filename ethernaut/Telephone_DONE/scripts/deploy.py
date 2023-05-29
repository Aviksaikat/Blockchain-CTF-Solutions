#!/usr/bin/python3
from brownie import Telephone
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    telephone = Telephone.deploy({"from": owner})

    print(f"Contract Deployed to: {telephone.address}")
    return telephone, owner


def main():
    deploy()

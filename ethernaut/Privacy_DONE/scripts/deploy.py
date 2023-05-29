#!/usr/bin/python3
from brownie import Privacy
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    data = [hex(1), hex(2), hex(3)]
    privacy = Privacy.deploy(data, {"from": owner})

    print(f"Contract Deployed to: {privacy.address}")
    return privacy, owner


def main():
    deploy()

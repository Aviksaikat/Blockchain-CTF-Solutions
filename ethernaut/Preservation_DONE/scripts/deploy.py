#!/usr/bin/python3
from brownie import LibraryContract, Preservation
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    lc1 = LibraryContract.deploy({"from": owner})
    lc2 = LibraryContract.deploy({"from": owner})

    print(f"Library1 Contract Deployed to: {lc1.address}")
    print(f"Library2 Contract Deployed to: {lc2.address}")

    preservation = Preservation.deploy(lc1.address, lc2.address, {"from": owner})
    return preservation, owner


def main():
    deploy()

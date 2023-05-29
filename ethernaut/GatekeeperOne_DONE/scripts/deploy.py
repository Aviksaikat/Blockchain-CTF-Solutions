#!/usr/bin/python3
from brownie import GatekeeperOne
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    gate_keeper_one = GatekeeperOne.deploy({"from": owner})

    print(f"Contract Deployed to: {gate_keeper_one.address}")
    return gate_keeper_one, owner


def main():
    deploy()

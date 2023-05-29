#!/usr/bin/python3
from brownie import Force
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    force = Force.deploy({"from": owner})

    print(f"Contract Deployed to: {force.address}")
    return force, owner


def main():
    deploy()

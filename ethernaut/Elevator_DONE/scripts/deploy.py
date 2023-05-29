#!/usr/bin/python3
from brownie import Elevator
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    elevator = Elevator.deploy({"from": owner})

    print(f"Contract Deployed to: {elevator.address}")
    return elevator, owner


def main():
    deploy()

#!/usr/bin/python3
from brownie import AlienCodex
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    ac = AlienCodex.deploy({"from": owner})

    return ac, owner


def main():
    deploy()

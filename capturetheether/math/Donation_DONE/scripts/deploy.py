#!/usr/bin/python3
from brownie import DonationChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = DonationChallenge.deploy({"from": owner, "value": "1 ether"})

    return c, owner


def main():
    deploy()

#!/usr/bin/python3
from brownie import Shop
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    s = Shop.deploy({"from": owner})

    return s, owner


def main():
    deploy()

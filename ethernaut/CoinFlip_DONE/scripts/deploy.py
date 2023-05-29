#!/usr/bin/python3
from brownie import CoinFlip
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    coin_flip = CoinFlip.deploy({"from": owner})

    print(f"Contract Deployed to: {coin_flip.address}")
    return coin_flip, owner


def main():
    deploy()

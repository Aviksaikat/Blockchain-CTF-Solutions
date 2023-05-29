#!/usr/bin/python3
from brownie import Fallback
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    fallback = Fallback.deploy({"from": owner})
    
    print(f"Contract Deployed to {fallback.address}")
    return fallback, owner


def main():
    deploy()

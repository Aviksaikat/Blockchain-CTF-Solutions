#!/usr/bin/python3
from brownie import Delegate, Delegation
from colorama import Fore
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def deploy():
    owner, _ = get_account()
    delegate = Delegate.deploy(owner, {"from": owner})
    delegation = Delegation.deploy(delegate.address, {"from": owner})

    print(f"{green}Contract Deployed to: {blue}{delegate.address}{reset}")
    print(f"{green}Contract Deployed to: {blue}{delegation.address}{reset}")

    return delegate, delegation, owner


def main():
    deploy()

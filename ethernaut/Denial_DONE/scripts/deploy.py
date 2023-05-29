#!/usr/bin/python3
from brownie import Denial
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = Denial.deploy({"from": owner})

    return c, owner


def main():
    deploy()

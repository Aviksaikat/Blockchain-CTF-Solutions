#!/usr/bin/python3
from brownie import CaptureTheEther, NicknameChallenge
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = CaptureTheEther.deploy({"from": owner})
    n = NicknameChallenge.deploy(c.address, {"from": owner})

    return c, n, owner


def main():
    deploy()

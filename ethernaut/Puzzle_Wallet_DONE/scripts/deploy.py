#!/usr/bin/python3
from brownie import PuzzleProxy, PuzzleWallet
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    pWallet_logic = PuzzleWallet.deploy({"from": owner})

    # bytes memory data = abi.encodeWithSelector(PuzzleWallet.init.selector, 100 ether);

    data = pWallet_logic.init.encode_input("100 ether")
    proxy = PuzzleProxy.deploy(owner, pWallet_logic, data, {"from": owner})

    pWallet = PuzzleWallet.at(proxy.address)

    return proxy, pWallet


def main():
    deploy()

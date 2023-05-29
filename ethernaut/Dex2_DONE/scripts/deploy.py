#!/usr/bin/python3
from brownie import DexTwo, SwappableTokenTwo
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = DexTwo.deploy({"from": owner})

    TKN1 = SwappableTokenTwo.deploy(c.address, "TOKEN1", "TKN1", 110, {"from": owner})
    TKN2 = SwappableTokenTwo.deploy(c.address, "TOKEN2", "TKN2", 110, {"from": owner})

    # print(TKN1.address)
    # print(TKN2.address)
    # print(dir(sT))

    # set tokens
    c.setTokens(TKN1.address, TKN2.address)

    # add liquidity to the DexTwo
    # approve first
    TKN1.approve(owner, c, 100, {"from": owner})
    TKN2.approve(owner, c, 100, {"from": owner})

    # now add liquidity to the DexTwo
    c.add_liquidity(TKN1.address, 100, {"from": owner})
    c.add_liquidity(TKN2.address, 100, {"from": owner})

    return c, owner, TKN1, TKN2


def main():
    deploy()

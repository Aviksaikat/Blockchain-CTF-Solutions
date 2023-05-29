#!/usr/bin/python3
from brownie import Dex, SwappableToken
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()
    c = Dex.deploy({"from": owner})

    TKN1 = SwappableToken.deploy(c.address, "TOKEN1", "TKN1", 110, {"from": owner})
    TKN2 = SwappableToken.deploy(c.address, "TOKEN2", "TKN2", 110, {"from": owner})

    print(TKN1.address)
    print(TKN2.address)
    # print(dir(sT))

    # set tokens
    c.setTokens(TKN1.address, TKN2.address)

    # add liquidity to the dex
    # approve first
    TKN1.approve(owner, c, 100, {"from": owner})
    TKN2.approve(owner, c, 100, {"from": owner})

    # now add liquidity to the dex
    c.addLiquidity(TKN1.address, 100, {"from": owner})
    c.addLiquidity(TKN2.address, 100, {"from": owner})

    return c, owner, TKN1, TKN2


def main():
    deploy()

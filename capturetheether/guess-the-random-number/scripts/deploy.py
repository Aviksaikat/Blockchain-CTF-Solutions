#!/usr/bin/python3
from brownie import accounts, GuessTheRandomNumberChallenge, config, network
from web3 import Web3

def get_account():
    if network.show_active() == "ropsten":
        return accounts.add(config["wallets"]["from_key"])
    return accounts[0]

def read_contract():
    guess_random = GuessTheRandomNumberChallenge[-1]
    print(guess_random.retrieve())

def deploy_guess_random_num():
    account = get_account()
    guess_random = GuessTheRandomNumberChallenge.deploy({"from" : account, "value" : Web3.toWei("1", "ether")})
    print("Contract Deployed !!")
    #is_complete = guess_random.isComplete()
    #print(f"Is complete : {is_complete}")
    #block_number = guess_random.tx.block_number
    #print(f"Block No: {block_number}")
    #print(dir(guess_random))
    return guess_random


def main():
    deploy_guess_random_num()

if __name__ == '__main__':
    main()
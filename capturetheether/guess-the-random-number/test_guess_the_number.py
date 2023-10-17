#!/usr/bin/python3
# from brownie import GuessTheRandomNumberChallenge
# from web3 import Web3
import web3
from brownie import Contract, config, network
from scripts.deploy import deploy_guess_random_num, get_account

# * address of the transaction in which the contract was deployed
TRANSACTION_ID = "0x1f9832dd1c3760e89797641bc1e67b8d6627a3f2e93ae1208454d8e0e0e16e6f"
CONTRACT_ADDRESS = "0x5fFD96105c401A4E8Eb2d8F2685e1E23445E1200"
ROPSTEN_KEY = config["networks"]["ropsten-fork"]
CONNECTION = f"https://ropsten.infura.io/v3/{ROPSTEN_KEY}"
ROPSTEN_FORK = "https://eth-ropsten.alchemyapi.io/v2/7UJ3QtQVCMQdgzWUMkuumCYi-xPy9EY8"


def connect_web3_to_ganache():
    return web3.Web3(web3.Web3.HTTPProvider("http://127.0.0.1:8545"))


def test_guessRandomNum():
    global TRANSACTION_ID
    if network.show_active() == "ropsten-fork":
        w3 = connect_web3_to_ganache(ROPSTEN_FORK)
        guess_num = deploy_guess_random_num()
    else:
        w3 = connect_web3_to_ganache(CONNECTION)
        guess_num = Contract.from_explorer(CONTRACT_ADDRESS)
        transaction_id = w3.eth._get_transaction(TRANSACTION_ID)

    # ? our_deployed_TRANSACTION_IDact_block_num = 12253759
    answer_hash = w3.eth.getStorageAt(CONTRACT_ADDRESS, 0).hex()[-2:]
    num = w3.toInt(hexstr=answer_hash)
    print(f"The Random Number we found is : {num}")
    # exit()

    tx = guess_num.guess(
        num, {"from": get_account(), "value": web3.Web3.toWei("1", "ether")}
    )
    tx.wait(1)
    print(f"Account Balance : {get_account().balance()}")

    assert guess_num.isComplete() == True

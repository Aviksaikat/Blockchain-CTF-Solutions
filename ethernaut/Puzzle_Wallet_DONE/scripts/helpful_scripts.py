#!/usr/bin/python3
from brownie import network, accounts, config

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache-local",
    "ganache-local-new-chainId",
]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0], accounts[1]
    elif network.show_active() == "sepolia-fork-ganache":
        return accounts.at("0x6DC51f9C50735658Cc6a003e07B0b92dF9c98473", force=True)
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])

    return None

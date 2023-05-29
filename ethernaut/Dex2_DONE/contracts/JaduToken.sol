// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract JaduToken is ERC20 {
    constructor(uint initialSupply) ERC20("JaduToken", "JDU") {
        _mint(msg.sender, initialSupply);
    }
}

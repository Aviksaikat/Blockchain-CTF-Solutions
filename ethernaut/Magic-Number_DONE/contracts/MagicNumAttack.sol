// SPDX-License-Identifier: MIT
pragma solidity ^0.8.8;

// https://www.ethervm.io/

// ## Clean version
// command  -> opt code
// PUSH1 2A -> 60 2A -> 602A
// PUSH1 40 -> 60 40 -> 6040
// MSTORE   -> 52    -> 52
// PUSH1 20 -> 60 20 -> 6020
// PUSH1 40 -> 60 40 -> 6040
// RETURN   -> F3    -> F3

// final -> 602A60405260206040F3

contract attack {
    function whatIsTheMeaningOfLife() public returns (uint) {
        return 42;
    }
}

// Deploy from byte code -> https://github.com/Sekin/ethereum-bytecode-deployment/blob/master/DeployBytecode.sol

contract DeployBytecode {
    address public addr;

    function deployByteCode(bytes memory bytecode) public returns (address) {
        address retrun_value;

        // inline assembly
        assembly {
            mstore(0x0, bytecode)
            retrun_value := create(0, 0xa0, calldatasize())
        }
        addr = retrun_value;
        return addr;
    }
}

pragma solidity ^0.4.21;

contract PublicKeyChallenge {
    //address owner = 0x92b28647ae1f3264661f72fb2eb9625a89d88a31;
    // as rikneby is depreciated. this address is obsolete so we will use the main address. 
    address public owner;
    bool public isComplete;

    // constructor added to set the owner
    constructor() public {
        owner = msg.sender;
    }

    function authenticate(bytes publicKey) public {
        require(address(keccak256(publicKey)) == owner);

        isComplete = true;
    }
}

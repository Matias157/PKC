// SPDX-License-Identifier: MIT

pragma solidity >=0.8.12;

import "./SimpleStorage.sol";

contract StorageFactory {
    uint256 private simpleStorageArrayLen;

    SimpleStorage[] public simpleStorageArray;
    mapping(string => uint256) nameToIndex;

    constructor() {
        simpleStorageArrayLen = 0;
    }

    function createSimpleStorageContract(
        string memory name,
        uint256 favoriteNumber
    ) public {
        SimpleStorage simpleStorage = new SimpleStorage(name, favoriteNumber);
        simpleStorageArray.push(simpleStorage);
        nameToIndex[name] = simpleStorageArrayLen;
        simpleStorageArrayLen += 1;
    }

    function sfGetFavoriteNumber(string memory name)
        public
        view
        returns (uint256)
    {
        return
            SimpleStorage(address(simpleStorageArray[nameToIndex[name]]))
                .getFavoriteNumber();
    }

    function sfGetName(string memory name) public view returns (string memory) {
        return
            SimpleStorage(address(simpleStorageArray[nameToIndex[name]]))
                .getName();
    }
}

// SPDX-License-Identifier: MIT

pragma solidity >=0.8.12;

contract PublicKeyChain {
    address private deployer;
    string private url;
    bool private isRovoked;
    bytes private x509;

    address[] private votes;
    uint256 private votesCount;
    mapping(address => bool) voterExists;

    Attribute[] private attributes;
    uint256 private attributesLen;
    mapping(string => uint256) nameToIndex;
    mapping(string => bool) attributeExists;

    struct Attribute {
        string attributeName;
        string data;
    }

    constructor(
        address _deployer,
        string memory _url,
        bytes memory _x509,
        string[] memory attrs,
        uint256 attrsLen
    ) {
        deployer = _deployer;
        url = _url;
        x509 = _x509;
        votesCount = 0;
        attributesLen = 0;
        isRovoked = false;
        if (attrsLen > 0) {
            for (uint256 i = 0; i < attrsLen; i += 2) {
                addAttribute(attrs[i], attrs[i + 1]);
            }
        }
    }

    function addAttribute(string memory _attributeName, string memory _data)
        public
    {
        if (attributeExists[_attributeName])
            revert("An Attribute with the same name already exists!");
        nameToIndex[_attributeName] = attributesLen;
        attributeExists[_attributeName] = true;
        attributes.push(Attribute(_attributeName, _data));
        attributesLen += 1;
    }

    function getDeployer() public view returns (address) {
        return deployer;
    }

    function getUrl() public view returns (string memory) {
        return url;
    }

    function getVotes() public view returns (uint256) {
        return votesCount;
    }

    function getAllInfo()
        public
        view
        returns (
            address,
            string memory,
            string[] memory,
            bytes memory,
            bool,
            uint256
        )
    {
        string[] memory attr = new string[](attributesLen);
        for (uint256 i = 0; i < attributesLen; i += 1) {
            attr[i] = string.concat(
                string.concat(attributes[i].attributeName, ": "),
                attributes[i].data
            );
        }
        return (deployer, url, attr, x509, isRovoked, votesCount);
    }

    function vote(address voter) public {
        if (voterExists[voter])
            revert("You already validated this Certificate!");
        voterExists[voter] = true;
        votes.push(voter);
        votesCount += 1;
    }
}

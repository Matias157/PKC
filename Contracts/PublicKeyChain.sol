// SPDX-License-Identifier: MIT

pragma solidity >=0.8.12;

contract PublicKeyChain {
    address private deployer;
    string private url;
    bool private isRovoked;
    bytes private x509;

    address[] private votes;
    uint256 private votesCount;
    mapping(address => uint256) voterToIndex;
    mapping(address => bool) voterExists;

    address[] private votedAddresses;
    uint256 private votedCount;
    mapping(address => uint256) votedToIndex;
    mapping(address => bool) addressVoted;

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
        votedCount = 0;
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
        if (isRovoked) revert("This Certificate is revoked!");
        if (attributeExists[_attributeName])
            revert("An Attribute with the same name already exists!");
        nameToIndex[_attributeName] = attributesLen;
        attributeExists[_attributeName] = true;
        attributes.push(Attribute(_attributeName, _data));
        attributesLen += 1;
    }

    function getRevokedState() public view returns (bool) {
        return isRovoked;
    }

    function getDeployer() public view returns (address) {
        if (isRovoked) revert("This Certificate is revoked!");
        return deployer;
    }

    function getUrl() public view returns (string memory) {
        if (isRovoked) revert("This Certificate is revoked!");
        return url;
    }

    function getVotes() public view returns (uint256) {
        if (isRovoked) revert("This Certificate is revoked!");
        return votesCount;
    }

    function getVotedList() public view returns (address[] memory) {
        if (isRovoked) revert("This Certificate is revoked!");
        return votedAddresses;
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
        if (isRovoked) revert("This Certificate is revoked!");
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
        if (isRovoked) revert("This Certificate is revoked!");
        if (voterExists[voter])
            revert("You already validated this Certificate!");
        voterToIndex[voter] = votesCount;
        voterExists[voter] = true;
        votes.push(voter);
        votesCount += 1;
    }

    function voted(address addrs) public {
        if (isRovoked) revert("This Certificate is revoked!");
        if (addressVoted[addrs])
            revert("This Certificate already exists in the voted list!");
        votedToIndex[addrs] = votedCount;
        addressVoted[addrs] = true;
        votedAddresses.push(addrs);
        votedCount += 1;
    }

    function removeVote(address addrs) public {
        if (isRovoked) revert("This Certificate is revoked!");
        if (!voterExists[addrs])
            revert("You haven't validated this Certificate!");
        votes[voterToIndex[addrs]] = votes[votes.length - 1];
        voterToIndex[votes[votes.length - 1]] = voterToIndex[addrs];
        voterToIndex[addrs] = 0;
        voterExists[addrs] = false;
        votes.pop();
        votesCount -= 1;
    }

    function removeVoted(address addrs) public {
        if (isRovoked) revert("This Certificate is revoked!");
        if (!addressVoted[addrs])
            revert("This certificate haven't been validated by you!");
        votedAddresses[votedToIndex[addrs]] = votedAddresses[
            votedAddresses.length - 1
        ];
        votedToIndex[votedAddresses[votedAddresses.length - 1]] = votedToIndex[
            addrs
        ];
        votedToIndex[addrs] = 0;
        addressVoted[addrs] = false;
        votedAddresses.pop();
        votedCount -= 1;
    }

    function revoke() public {
        if (isRovoked) revert("This Certificate is already revoked!");
        isRovoked = true;
    }
}

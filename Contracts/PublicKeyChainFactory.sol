// SPDX-License-Identifier: MIT

pragma solidity >=0.8.12;

import "./PublicKeyChain.sol";

contract PublicKeyChainFactory {
    uint256 private publicKeyChainArrayLen;

    PublicKeyChain[] private publicKeyChainArray;
    mapping(address => uint256) addressToIndex;
    mapping(address => bool) addressExists;

    constructor() {
        publicKeyChainArrayLen = 0;
    }

    function createPublicKeyChainContract(
        string memory url,
        bytes memory x509,
        string[] memory attrs,
        uint256 attrsLen
    ) public {
        if (addressExists[msg.sender])
            revert("Only one Certificate per Address allowed!");
        PublicKeyChain publicKeyChain = new PublicKeyChain(
            msg.sender,
            url,
            x509,
            attrs,
            attrsLen
        );
        publicKeyChainArray.push(publicKeyChain);
        addressToIndex[msg.sender] = publicKeyChainArrayLen;
        addressExists[msg.sender] = true;
        publicKeyChainArrayLen += 1;
    }

    function getKeysCount() public view returns (uint256) {
        return publicKeyChainArrayLen;
    }

    function fGetDeployer(address deployer) public view returns (address) {
        if (!addressExists[deployer]) revert("Certificate could not be found!");
        if (
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getRevokedState()
        ) revert("This Certificate is revoked!");
        return
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getDeployer();
    }

    function fGetUrl(address deployer) public view returns (string memory) {
        if (!addressExists[deployer]) revert("Certificate could not be found!");
        if (
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getRevokedState()
        ) revert("This Certificate is revoked!");
        return
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getUrl();
    }

    function fGetVotes(address deployer) public view returns (uint256) {
        if (!addressExists[deployer]) revert("Certificate could not be found!");
        if (
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getRevokedState()
        ) revert("This Certificate is revoked!");
        return
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getVotes();
    }

    function fVote(address deployer) public {
        if (!addressExists[deployer]) revert("Certificate could not be found!");
        if (
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getRevokedState()
        ) revert("This Certificate is revoked!");
        if (!addressExists[msg.sender])
            revert("Create a certificate before voting!");
        if (
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[msg.sender]])
            ).getRevokedState()
        ) revert("Your Certificate is revoked!");
        PublicKeyChain(address(publicKeyChainArray[addressToIndex[deployer]]))
            .vote(msg.sender);
        PublicKeyChain(address(publicKeyChainArray[addressToIndex[msg.sender]]))
            .voted(deployer);
    }

    function fGetAllInfo(address deployer)
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
        if (!addressExists[deployer]) revert("Certificate could not be found!");
        if (
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getRevokedState()
        ) revert("This Certificate is revoked!");
        return
            PublicKeyChain(
                address(publicKeyChainArray[addressToIndex[deployer]])
            ).getAllInfo();
    }

    function fQuery(string memory url) public view returns (address[] memory) {
        uint256 duplicates = 0;
        uint256 j = 0;
        for (uint256 i = 0; i < publicKeyChainArrayLen; i++) {
            if (
                !PublicKeyChain(address(publicKeyChainArray[i]))
                    .getRevokedState()
            ) {
                if (
                    keccak256(
                        bytes(
                            PublicKeyChain(address(publicKeyChainArray[i]))
                                .getUrl()
                        )
                    ) == keccak256(bytes(url))
                ) {
                    duplicates += 1;
                }
            }
        }
        if (duplicates <= 0) revert("Certificate could not be found!");
        address[] memory addr = new address[](duplicates);
        for (uint256 i = 0; i < publicKeyChainArrayLen; i++) {
            if (
                !PublicKeyChain(address(publicKeyChainArray[i]))
                    .getRevokedState()
            ) {
                if (
                    keccak256(
                        bytes(
                            PublicKeyChain(address(publicKeyChainArray[i]))
                                .getUrl()
                        )
                    ) == keccak256(bytes(url))
                ) {
                    addr[j] = PublicKeyChain(address(publicKeyChainArray[i]))
                        .getDeployer();
                    j += 1;
                }
            }
        }
        return (addr);
    }
}


def bc_index():
    print("""sdfds""")

#
# def bc_p0():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.0;
# contract SimpleStorage {
# uint256 private storedData;
# // Function to set the value of storedData
# function set(uint256 x) public {
# storedData = x;
# }
# // Function to get the value of storedData
# function get() public view returns (uint256) {
# return storedData;
# }
# }
#     ''')
#
#
# # def bc_p8():
# #     print('''
# # To check if the prerequisites (Node.js, npm, and Truffle) are installed, you can run the
# # following commands:
# # Step 1: Prerequisites
# # Install Node.js
# # https://nodejs.org/en/download/prebuilt-installer
# # Execute the following Commands:
# # npm install -g truffle
# # npm install -g ganache-cli
# #
# # 1) Check Node.js and npm installation:
# # node -v
# # npm -v
# # 2) Check Truffle installation:
# # truffle version
# # 3) Install Ganache
# # https://archive.trufflesuite.com/ganache/
# # 4) Create a new Workspace (pract_bc) in ganache software.
# # Step 2: Initialize a Truffle Project
# #
# # 1) Create a new directory for your project:
# # mkdir myProj
# # cd myProj
# # 2) Initialize the Truffle project:
# # truffle init
# #
# # Step 3: Create a Solidity Smart Contract
# #
# # 1) Navigate to the Contracts directory(myProj/contracts) in vs code:
# # SimpleStorage.sol
# # // SPDX-License-Identifier: MIT
# # pragma solidity ^0.8.0;
# # contract SimpleStorage {
# # uint256 public storedData;
# # function set(uint256 x) public {
# # storedData = x;
# # }
# # function get() public view returns (uint256) {
# # return storedData;
# # }
# # }
# # 2) Compile the Smart Contract in terminal of vs code.
# # Command: truffle compile
# # C:\\Users\\hp\\Pract bc\\myProj> truffle compile
# #
# # Step 4: Configure Truffle to Use Ganache
# #
# # Open the truffle-config.js file and configure the development network to use Ganache. Update
# # the networks section:
# # module.exports = {
# # networks: {
# # development: {
# # host: "127.0.0.1",
# # port: 7545, // Match the port Ganache is using
# # network_id: "*" // Match any network id
# # }
# # },
# # compilers: {
# # solc: {
# # version: "0.8.0" // Specify the Solidity compiler version
# # }
# # }
# # };
# # Step 5: Migrate the Smart Contract to Ganache
# # 1) Start Ganache (open the Ganache application and start a new
# # workspace(pract_bc))
# # 2) Create a migration script in the migrations directory
# # (e.g., deploy_contracts.js) (following is code for that):
# # \\myProj\\migrations\\2_deploy_contracts.js
# # const SimpleStorage = artifacts.require("SimpleStorage");
# #
# # module.exports = function (deployer) {
# # deployer.deploy(SimpleStorage);
# # };
# #
# # 3) Run the migration (vs code terminal cmd):
# # Command: truffle migrate
# # //Eg. C:\\Users\\hp\\Pract bc\\myProj> truffle migrate
# # //(op: saving artifacts)
# #
# # Step 6: Interact with the Deployed Contract
# # 1) Open the new command prompt terminal of vscode:
# # Command: truffle console
# # //C:\\Users\\hp\\Pract bc\\myProj> truffle console
# # 2) Interact with the deployed contract:
# # Execute the following commands one-by-one
# # let instance = await SimpleStorage.deployed()
# # await instance.set(42)
# # let value = await instance.get()
# # value.toString() // Output should be '42'
# #     ''')
# #
#
#
# def bc_p7():
#     print('''
# 1) Check version and installation (vscode terminal)
# git –-version
# curl –version
# docker –version
# jq –version
#
# 2) Download fabric samples
# curl -sSLO https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh
# &amp;&amp; chmod +x install-fabric.sh
# 3) Pull the docker containers (vscode terminal)
# ./install-fabric.sh
#
# 4) Navigate to test network directory (vscode terminal)
# ls
# cd fabric-samples
# ls
# cd test-network
# ls
# 5) Remove any containers or artifacts (vscode terminal)
# ./network.sh down
# 6) Up the network (vscode terminal)
# ./network.sh up
#
# 7) Now open Docker Desktop in backhgrounff
# 8) Now Create a channel (vscode terminal)
# ./network.sh createChannel
# 9) Deploy chaincode on peers and channel (vscode terminal)
# ./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-javascript -ccl javascript
# //(O/P = “approvals”: {
# //“Org1MSP”: true,
# //“Org2MSP”: true
# //})
# 10) Now Interacting with the network
# 11) Set the path for peer binary and config for core.yaml
# export PATH=${PWD}/../bin:$PATH
# export FABRIC_CFG_PATH=$PWD/../config/
# 12) Set the environment variables to operate Peer as Org1 in (vscode)
# export CORE_PEER_TLS_ENABLED=true
# export CORE_PEER_LOCALMSPID=&quot;Org1MSP&quot;
# export
# CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.exampl
# e.com/peers/peer0.org1.example.com/tls/ca.crt
# export
# CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.co
# m/users/Admin@org1.example.com/msp
# export CORE_PEER_ADDRESS=localhost:7051
# 13) Command to initialize the ledger with assets
# peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --
# cafile
# &quot;${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscac
# erts/tlsca.example.com-cert.pem&quot; -C mychannel -n basic --peerAddresses localhost:7051 --
# tlsRootCertFiles
# &quot;${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.cr
# t&quot; --peerAddresses localhost:9051 --tlsRootCertFiles
# &quot;${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.cr
# t&quot; -c &#39;{&quot;function&quot;:&quot;InitLedger&quot;,&quot;Args&quot;:[]}&#39;
# 14) Query the ledger
# peer chaincode query -C mychannel -n basic -c &#39;{&quot;Args&quot;:[&quot;GetAllAssets&quot;]}&#39;
# 15) Transfer the asset
# peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --
# tls --cafile
# &quot;${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tl
# scacerts/tlsca.example.com-cert.pem&quot; -C mychannel -n basic --peerAddresses localhost:7051 --
# tlsRootCertFiles
# &quot;${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/
# ca.crt&quot; --peerAddresses localhost:9051 --tlsRootCertFiles
#
# &quot;${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.cr
# t&quot; -c &#39;{&quot;function&quot;:&quot;TransferAsset&quot;,&quot;Args&quot;:[&quot;asset6&quot;,&quot;Christopher&quot;]}&#39;
# 16) Lets query the ledger from Org2 peer
# 17) Set the environment variables to operate Peer as Org2
# export CORE_PEER_TLS_ENABLED=true
# export CORE_PEER_LOCALMSPID=&quot;Org2MSP&quot;
# export
# CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.exampl
# e.com/peers/peer0.org2.example.com/tls/ca.crt
# export
# CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.co
# m/users/Admin@org2.example.com/msp
# export CORE_PEER_ADDRESS=localhost:9051
# 18) Query the ledger
# peer chaincode query -C mychannel -n basic -c &#39;{&quot;Args&quot;:[&quot;ReadAsset&quot;,&quot;asset6&quot;]}&#39;
# 19) Bring the network down
# ./network.sh down
#     ''')
#
#
# def bc_p1a():
#     print('''
# import Crypto
# import Crypto.Random
# from Crypto.Hash import SHA
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5       #alogrithm for authoriza on
#
# import pandas as pd
# import numpy as np
# import binascii
#
# class Client:
#
#    def __init__(self):
#       random = Crypto.Random.new().read
#       self._private_key = RSA.generate(1024, random)
#       self._public_key = self._private_key.publickey()
#       self._signer = PKCS1_v1_5.new(self._private_key)
#
#    @property
#    def iden ty(self):
#       return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
#
# Demo = Client()
# print(Demo.iden ty)
#       ''')
#
#
# def bc_p1b():
#     print('''
# import random
# import binascii
# import logging
# import datetime
# import collections
#
# import Crypto
# import Crypto.Random
# from Crypto.Hash import SHA
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
#
# class Client:
#     def __init__(self):
#         random_generator = Crypto.Random.new().read
#         self._private_key = RSA.generate(1024, random_generator)
#         self._public_key = self._private_key.publickey()
#         self._signer = PKCS1_v1_5.new(self._private_key)
#
#     @property
#     def identity(self):
#         return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
#
# class Transaction:
#     def __init__(self, sender, recipient, value):
#         self.sender = sender
#         self.recipient = recipient
#         self.value = value
#         self.time = datetime.datetime.now()
#
#     def to_dict(self):
#         if self.sender == "Genesis":
#             identity = "Genesis"
#         else:
#             identity = self.sender.identity
#         return collections.OrderedDict({
#             'sender': identity,
#             'recipient': self.recipient,
#             'value': self.value,
#             'time' : self.time
#         })
#
#     def sign_transaction(self):
#         private_key = self.sender._private_key
#         signer = PKCS1_v1_5.new(private_key)
#         h = SHA.new(str(self.to_dict()).encode('utf8'))
#         return binascii.hexlify(signer.sign(h)).decode('ascii')
#
# Harshad = Client()
# print("Harshad Key\n")
# print(Harshad.identity)
# Ross = Client()
# print("\nRoss Key\n")
# print(Ross.identity)
#
# t = Transaction(Harshad,Ross.identity,10.0)
# print("\nTransaction Signature\n")
# signature = t.sign_transaction()
# print(signature)
#
#       ''')
#
#
# def bc_p1c():
#     print('''
# import Crypto
# import binascii
# import collections
# import datetime
#
# from Crypto.PublicKey import RSA
# from Crypto import Random
# from Crypto.Hash import SHA
# from Crypto.Signature import PKCS1_v1_5
#
# import hashlib
#
# class Client:
#
#     def __init__(self):
#
#         random = Crypto.Random.new().read	        # Creating a random number for key
#
#
#         self._private_key = RSA.generate(1024, random)	        # Creating a new public key and private key
#         self._public_key = self._private_key.publickey()
#         self._signer = PKCS1_v1_5.new(self._private_key)
#
#     @property
#
#     def identity(self):
#         return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
#
# class Transaction:
#     def __init__(self, sender, receiver, value):
#         self.sender = sender
#         self.receiver = receiver
#         self.value = value
#         self.time = datetime.datetime.now()
#
#     def to_dict(self):
#
#         if self.sender == "Genesis":
#             identity = "Genesis"
#
#         else:
#             identity = self.sender.identity
#         return collections.OrderedDict({
#             "sender": identity,
#             "receiver": self.receiver,
#             "value": self.value,
#             "time": self.time
#         })
#
#     def sign_transaction(self):
#
#         private_key = self.sender._private_key
#         signer = PKCS1_v1_5.new(private_key)
#         h = SHA.new(str(self.to_dict()).encode('utf8'))
#         return binascii.hexlify(signer.sign(h)).decode('ascii')
#
# def sha256(message):
#     return hashlib.sha256(message.encode('ascii')).hexdigest()
#
# def mine(message, difficulty=1):
#     assert difficulty >= 1
#
#     prefix = '1' * difficulty
#
#     for i in range(1000):
#         digest = sha256(str(hash(message)) + str(i))
#         if digest.startswith(prefix):
#             print("after " + str(i) + " iterations found nonce: " + digest)
#             return digest
#
# class Block:
#     def __init__(self):
#         self.verified_transactions = []
#         self.previous_block_hash = ""
#         self.Nonce = ""
#         last_block_hash = ""
#
#     def display_transaction(self, transaction):
#         dict_transaction = transaction.to_dict()
#         print("sender: " + dict_transaction['sender'])
#         print('----')
#         print("recipient: " + dict_transaction['receiver'])
#         print('----')
#         print("value: " + str(dict_transaction['value']))
#         print('----')
#         print("time: " + str(dict_transaction['time']))
#         print('-----')
# TPCoins = []
#
# def dump_blockchain(self):
#
#     print("Number of blocks in the chain: " + str(len(self)))
#
#     for x in range(len(TPCoins)):
#
#         block_temp = TPCoins[x]
#
#         print("block # " + str(x))
#
#         for transaction in block_temp.verified_transactions:
#
#             block_temp.display_transaction(transaction)
#
#             print('--- ----')
#
# last_transaction_index = 0
#
# transactions = []
#
# Raja = Client()
# Rani = Client()
# Seema = Client()
# Reema = Client()
#
# tl = Transaction(Raja, Rani.identity, 15.0)
#
# tl.sign_transaction()
#
# transactions.append(tl)
#
# t2 = Transaction(Raja, Seema.identity, 6.0)
#
# t2.sign_transaction()
#
# transactions.append(t2)
#
# t3 = Transaction(Rani, Reema.identity, 2.0)
#
# t3.sign_transaction()
#
# transactions.append(t3)
#
# t4 = Transaction(Seema, Rani.identity, 4.0)
#
# t4.sign_transaction()
#
# transactions.append(t4)
#
# t5 = Transaction(Reema, Seema.identity, 7.0)
#
# t5.sign_transaction()
#
# transactions.append(t5)
#
# t6 = Transaction(Rani, Seema.identity, 3.0)
#
# t6.sign_transaction()
#
# transactions.append(t6)
#
# t7 = Transaction(Seema, Raja.identity, 8.0)
#
# t7.sign_transaction()
#
# transactions.append(t7)
#
# t8 = Transaction(Seema, Rani.identity, 1.0)
#
# t8.sign_transaction()
#
# transactions.append(t8)
#
# t9 = Transaction(Reema, Raja.identity, 5.0)
#
# t9.sign_transaction()
#
# transactions.append(t9)
#
# t10 = Transaction(Reema, Rani.identity, 3.0)
#
# t10.sign_transaction()
#
# transactions.append(t10)
#
# # Create a new block instance
#
# block = Block()
#
# for transaction in transactions:
#
#     block.verified_transactions.append(transaction)	    # Add transactions to the block
#
#     block.display_transaction(transaction)	    # Display each transaction in the block
#
#     print('---')
#
#       ''')
#
#
# def bc_p1d():
#     print('''
# import hashlib
# import random
# import string
# import json
# import binascii
# import numpy as np
# import pandas as pd
# import pylab as pl
# import logging
# import datetime
# import collections
#
# import Crypto
# import Crypto.Random
# from Crypto.Hash import SHA
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
#
# class Client:
#    def __init__(self):
#       random = Crypto.Random.new().read
#       self._private_key = RSA.generate(1024, random)
#       self._public_key = self._private_key.publickey()
#       self._signer = PKCS1_v1_5.new(self._private_key)
#
#    @property
#    def identity(self):
#       return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
#
# class Transaction:
#     def __init__( self, sender, recipient, value ):
#         self.sender = sender
#         self.recipient = recipient
#         self.value = value
#         self.time = datetime.datetime.now()
#
#     def to_dict( self ):
#         if self.sender == "Genesis":
#             identity = "Genesis"
#         else:
#             identity = self.sender.identity
#
#         return collections.OrderedDict( {
#            'sender': identity,
#            'recipient': self.recipient,
#            'value': self.value,
#            'time' : self.time } )
#
#     def sign_transaction( self ):
#         private_key = self.sender._private_key
#         signer = PKCS1_v1_5.new(private_key)
#         h = SHA.new(str(self.to_dict()).encode('utf8'))
#         return binascii.hexlify(signer.sign(h)).decode('ascii')
# def display_transaction(transaction):
#         #for transaction in transactions:
#         dict = transaction.to_dict()
#         print ("sender: " + dict['sender'])
#         print ('-----')
#         print ("recipient: " + dict['recipient'])
#         print ('-----')
#         print ("value: " + str(dict['value']))
#         print ('-----')
#         print ("time: " + str(dict['time']))
#         print ('-----')
#
# class Block:
#    def __init__(self):
#       self.verified_transactions = []
#       self.previous_block_hash = ""
#       self.Nonce = ""
# last_block_hash = ""
#
# def dump_blockchain (self):
#    print ("Number of blocks in the chain: " + str(len (self)))
#    for x in range (len(TPCoins)):
#       block_temp = TPCoins[x]
#       print ("block # " + str(x))
#       for transaction in block_temp.verified_transactions:
#          display_transaction (transaction)
#          print ('--------------')
#       print ('=====================================')
#
# Harshad = Client()
#
# t0 = Transaction (
#    "Genesis",
#    Harshad.identity,
#    500.0
# )
#
# block0 = Block()
# block0.previous_block_hash = None
# Nonce = None
# block0.verified_transactions.append (t0)
# digest = hash (block0)
# last_block_hash = digest
# TPCoins = []
# TPCoins.append (block0)
# dump_blockchain(TPCoins)
#
#       ''')
#
#
# def bc_p1e():
#     print('''
# import hashlib
# import random
# import string
# import json
# import binascii
# import numpy as np
# import pandas as pd
# import pylab as pl
# import logging
# import datetime
# import collections
#
# import Crypto
# import Crypto.Random
# from Crypto.Hash import SHA
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
#
# def sha256(message):
#     return hashlib.sha256(message.encode('ascii')).hexdigest()
#
# def mine(message, difficulty=1):
#     assert difficulty >= 1
#     prefix = '1' * difficulty
#     for i in range(1000):
#         digest = sha256(str(hash(message)) + str(i))
#         if digest.startswith(prefix):
#             print("after " + str(i) + " iterations found nonce: " + digest)
#             return digest
#
# mine("test message", 2)
#
#       ''')
#
#
# def bc_p2a():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract PrimitiveDataTypes {
#
#     uint8   a = 20; 			    //state variables (global variable)
#     uint256 b = 35;
#     int     c = 10;
#     int8    d = 3;
#
#     bool    flag = true;
#     address addr = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;
#
#     // Operations in solidity
#     uint public addition    = a + b;
#     int  public subtraction = c - d;
#     int  public multiply    = d * c;
#     int  public division    = c / d;
#     int  public moduloDiv   = c % d;
#     int  public increment   = ++c;
#     int  public decrement   = --d;
#
# }
#
#       ''')
#
#
# def bc_p2b():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Loop {
#
#     function summation(uint n) public pure returns (uint) {
#         uint sum = 0;
#         for (uint i = 1; i <= n; i++) {
#             sum += i;
#         }
#         return sum;
#     }
#
#     function sumWhile(uint n) public pure returns (uint) {
#         uint sum = 0;
#         uint i = 1;
#         while (i <= n) {
#             sum += i;
#             i++;
#         }
#         return sum;
#     }
#
#     function sumDoWhile(uint n) public pure returns (uint) {
#         uint sum = 0;
#         uint i = 1;
#         do {
#             sum += i;
#             i++;
#         } while (i <= n);
#         return sum;
#     }
#
# }
#
#       ''')
#
#
# def bc_p2c():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Loop {
#
#     function summation(uint n) public pure returns (uint) {
#         uint sum = 0;
#         for (uint i = 1; i <= n; i++) {
#             sum += i;
#         }
#         return sum;
#     }
#
#     function sumWhile(uint n) public pure returns (uint) {
#         uint sum = 0;
#         uint i = 1;
#         while (i <= n) {
#             sum += i;
#             i++;
#         }
#         return sum;
#     }
#
#     function sumDoWhile(uint n) public pure returns (uint) {
#         uint sum = 0;
#         uint i = 1;
#         do {
#             sum += i;
#             i++;
#         } while (i <= n);
#         return sum;
#     }
#
# }
#
#       ''')
#
#
# def bc_p2d():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Arrays {
#
#     uint[] public array1 = [1, 2, 3, 4];			    // Declaring an array
#
#     function fetch(uint index) public view returns (uint) {
#         require(index < array1.length, "Index out of bounds");
#         return array1[index];
#     }
# }
#
#       ''')
#
#
# def bc_p2e():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Enums{		  	  //Define enum
#     enum week_days {Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday}
#     week_days choice;
#
#     function set_value() public {
#       choice = week_days.Friday;
#     }
#      function get_choice(		         // Defining a function to return value of choice
#     ) public view returns (week_days) {
#       return choice;
#     }
# }
#
#       ''')
#
#
# def bc_p2f():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Structs{
#
#     struct Book {			    //declaring a struct
#         string name;
#         string writer;
#         uint price;
#         bool available;
#     }
#
#     Book book1;			 //set book details like this
#     Book book2 = Book ("Game of Thrones","George R.R. Martin",300,true);
#
#     function set_book_detail() public {	    //set book details like this
#     book1 = Book("Introducing Ethereum and Solidity","Chris Dannen",250, true);
#     }
#
#     function book1_info() public view returns (string memory, string memory, uint, bool) {
#         return(book2.name, book2.writer,book2.price, book2.available);
#     }
#
#       function book2_info() public view returns (string memory, string memory, uint, bool) {
#       return (book1.name, book1.writer, book1.price, book1.available);
#    }
# }
#
#       ''')
#
#
# def bc_p2g():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract maps{
#
#     mapping (uint=>string) public roll_no;
#
#     function set(uint keys, string memory value) public {
#         roll_no[keys]=value;
#     }
# }
#
#       ''')
#
#
# def bc_p2h():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Conversion {
#
#     uint   a = 5;
#     uint8  b = 10;
#     uint16 c = 15;
#
#     function convert() public view returns (uint) {
#         uint result = a + uint(b) + uint(c);
#         return result;
#     }
#
#     function etherUnits() public pure returns (uint, uint, uint) { //Demo Ether u
#         uint oneWei = 1 wei;
#         uint oneEther = 1 ether;
#         uint oneGwei = 1 gwei;
#         return (oneWei, oneEther, oneGwei);
#     }
#
#     // Demo Sp.Variables
#     function specialVariables() public view returns (address, uint, uint) {
#         address sender = msg.sender; 	// Sender of the message (current call)
#         uint timestamp = block.timestamp; 	// Current block timestamp
#         uint blockNumber = block.number; 	// Current block number
#         return (sender, timestamp, blockNumber);
#     }
# }
#
#       ''')
#
#
# def bc_p2i():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract StringExample {		    // State variable to store a string
#     string public greeting = "Hello, ";
#
#     function concatenate(string memory _name) public view returns (string memory) {				 // Function to concatenate strings
#         return string(abi.encodePacked(greeting, _name));
#     }
#
#     function compareStrings(string memory _a, string memory _b) public pure returns (bool) {		    	// Function to compare two strings
#         return keccak256(abi.encodePacked(_a)) == keccak256(abi.encodePacked(_b));
#     }
#   // Function to update the greeting
#     function updateGreeting(string memory _newGreeting) public {
#         greeting = _newGreeting;
#     }
# }
#
#       ''')
#
#
# def bc_p3a():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract Addition {
#
#     int public input1;
#     int public input2;
#
#     function setInputs(int _input1, int _input2) public {
#         input1 = _input1;
#         input2 = _input2;
#     }
#
#     function additions() public view returns(int) {
#         return input1 + input2;
#     }
#
#     function subtract() public view returns(int) {
#         return input1 - input2;
#     }
# }
#
#       ''')
#
#
# def bc_p3b():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract fallbackfn
# {
#     event Log(string func,address sender, uint value, bytes data);
#
#     fallback() external payable{
#         emit Log("fallback",msg.sender,msg.value,msg.data);
#     }
#
#     receive() external payable{
#         emit Log("receive",msg.sender,msg.value,"");
#         //msg.data is empty hence no need to specify it and mark it as empty string
#     }
# }
#
#       ''')
#
#
# def bc_p3c():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract MathOperations {
#     // addMod computes (x + y) % k
#     // mulMod computes (x * y) % k
#
#     function computeMod() public pure returns (uint addModResult, uint mulModResult) {
#         uint x = 3;
#         uint y = 2;
#         uint k = 6;
#         addModResult = addmod(x, y, k);
#         mulModResult = mulmod(x, y, k);
#     }
# }
#
#       ''')
#
#
# def bc_p3d():
#     print('''
# pragma solidity ^0.5.0;
#  contract Test{
#  function callKeccak256() public pure returns(bytes32 result){
#  return keccak256("BLOCKCHAIN");
#  }
#  function callsha256() public pure returns(bytes32 result){
#  return sha256("BLOCKCHAIN");
#  }
#  function callripemd() public pure returns (bytes20 result){
#  return ripemd160("BLOCKCHAIN");
#  }
#  }
#
#
#       ''')
#
#
# def bc_p3e():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.13;
#
# contract FunctionModifier{
#
#     address public owner;
#     uint public x = 100;
#     bool public locked;
#
#     constructor() {                // Set the transaction sender as the owner of the contract.
#         owner = msg.sender;
#         }
#
#         modifier onlyOwner() {
#             require(msg.sender == owner, "Not owner");
#             _;
#             }
#
#         modifier validAddress(address _addr) {
#             require(_addr != address(0), "Not valid address");
#             _;
#             }
#
#     function changeOwner(address _newOwner) public onlyOwner validAddress(_newOwner) {
#         owner = _newOwner;
#         }
#
#         modifier noReentrancy() {
#             require(!locked, "No reentrancy");
#             locked = true;
#             _;
#             locked = false;
#         }
#
#     function decrement(uint i) public noReentrancy {
#         x -= i;
#         if (i > 1) {
#             decrement(i - 1);
#         }
#     }
# }
#
#       ''')
#
#
# def bc_p3f():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.3;
#
# contract ViewAndPure {
#     uint public x = 1;
#
#     // Promise not to modify the state.
#     function addToX(uint y) public view returns (uint) {
#         return x + y;
#     }
#
#     // Promise not to modify or read from the state.
#     function add(uint i, uint j) public pure returns (uint) {
#         return i + j;
#     }
# }
#
#       ''')
#
#
# def bc_p3g():
#     print('''
# // SPDX-License-Identifier: MIT
#     pragma solidity ^0.8.17;
#
#     contract FunctionOverloading {
#         // Function with one parameter
#         function sum(uint a) public pure returns (uint) { return a + 10; }
#
#         // Overloaded function with two parameters
#         function sum(uint a, uint b) public pure returns (uint) { return a + b; }
#
#         // Overloaded function with three parameters
#         function sum(uint a, uint b, uint c) public pure returns (uint) { return a + b + c; }
#
#         // Examples of calling overloaded functions
#         function exampleUsage() public pure returns (uint, uint, uint) {
#             uint result1 = sum(5);                	// Calls the first sum function
#             uint result2 = sum(5, 10);          	// Calls the second sum function
#             uint result3 = sum(5, 10, 15);    	// Calls the third sum function
#
#             return (result1, result2, result3);
#         }
#     }
#
#       ''')
#
#
# def bc_p4a():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.13;
#
# contract withdrawalPattern{
#     address public richest;
#     uint public mostSent;
#
#     mapping (address=>uint) pendingWithdrawals;
#     error NotEnoughEther();
#
#     constructor() payable{
#         richest = msg.sender;
#         mostSent = msg.value;
#     }
#
#     function becomeRichest() public payable{
#         if (msg.value <= mostSent) revert NotEnoughEther();
#         pendingWithdrawals[richest] += msg.value;
#         richest = msg.sender;
#         mostSent = msg.value;
#     }
#
#     function withdraw() public {
#         uint amount = pendingWithdrawals[msg.sender];
#         pendingWithdrawals[msg.sender] = 0;
#         payable (msg.sender).transfer(amount);
#     }
# }
#
#
#       ''')
#
#
# def bc_p4b():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
# contract AccessRestriction {
#
#     address public owner = msg.sender;
#     uint public creationTime = block.timestamp;
#
#     error Unauthorized();
#     error TooEarly();
#     error NotEnoughEther();
#
#     modifier onlyBy(address account){
#         if (msg.sender != account)
#         revert Unauthorized();
#         _;
#     }
#
#     modifier costs(uint amount) {
#         if (msg.value < amount)
#             revert NotEnoughEther();
#             _;
#         if (msg.value > amount)
#             payable(msg.sender).transfer(msg.value - amount);
#     }
#
#     modifier onlyAfter(uint time) {
#         if (block.timestamp < time)
#             revert TooEarly();
#             _;
#     }
#
#     function changeOwner(address newOwner)public onlyBy(owner){
#         owner = newOwner;
#     }
#
#     function disown()public onlyBy(owner) onlyAfter(creationTime + 6 weeks){
#         delete owner;
#     }
#
#     function forceOwnerChange(address newOwner)public payable costs(20 ether){
#         owner = newOwner;
#         // just some example condition
#         if (uint160(owner) & 0 == 1)
#             return;
#     }
#
#       ''')
#
#
# def bc_p5a():
#     print('''
# import hashlib
# import time
#
# class Block(object):
#     def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
#         self.index = index
#         self.proof_number = proof_number
#         self.previous_hash = previous_hash
#         self.data = data
#         self.timestamp = timestamp or time.time()
#
#     @property
#     def compute_hash(self):
#         string_block = "{}{}{}{}{}".format(self.index, self.proof_number, self.previous_hash, self.data, self.timestamp)
#         return hashlib.sha256(string_block.encode()).hexdigest()
#
#     def __repr__(self):
#         return "{} - {} - {} - {} - {}".format(self.index, self.proof_number, self.previous_hash,  self.data, self.timestamp)
#
# class BlockChain(object):
#     def __init__(self):
#         self.chain = []
#         self.current_data = []
#         self.nodes = set()
#         self.build_genesis()
#
#     def build_genesis(self):
#         self.build_block(proof_number=0, previous_hash=0)
#
#     def build_block(self, proof_number, previous_hash):
#         block = Block(
#             index=len(self.chain),
#             proof_number=proof_number,
#             previous_hash=previous_hash,
#             data=self.current_data
#         )
#         self.current_data = []
#         self.chain.append(block)
#         return block
#
#     @staticmethod
#     def confirm_validity(block, previous_block):
#         if previous_block.index + 1 != block.index:
#             return False
#         elif previous_block.compute_hash != block.previous_hash:
#             return False
#         elif block.timestamp <= previous_block.timestamp:
#             return False
#         return True
#
#     def get_data(self, sender, receiver, amount):
#         self.current_data.append({
#             'sender': sender,
#             'receiver': receiver,
#             'amount': amount
#         })
#         return True
#
#     @staticmethod
#     def proof_of_work(last_proof):
#         pass
#
#     @property
#     def latest_block(self):
#         return self.chain[-1]
#
#     def chain_validity(self):
#         pass
#
#     def block_mining(self, details_miner):
#         self.get_data(
#             sender="0",  # it implies that this node has created a new block
#             receiver=details_miner,
#             amount=1  # creating a new block (or identifying the proof number) is awarded with 1
#         )
#
#         last_block = self.latest_block
#         last_proof_number = last_block.proof_number
#         proof_number = self.proof_of_work(last_proof_number)
#         last_hash = last_block.compute_hash
#         block = self.build_block(proof_number, last_hash)
#         return vars(block)
#
#     def create_node(self, address):
#         self.nodes.add(address)
#         return True
#
#     @staticmethod
#     def get_block_object(block_data):
#         return Block(
#             block_data['index'],
#             block_data['proof_number'],
#             block_data['previous_hash'],
#             block_data['data'],
#             timestamp=block_data['timestamp']
#         )
#
# blockchain = BlockChain()
#
# print("GET READY! MINING ABOUT TO START")
# print(blockchain.chain)
#
# last_block = blockchain.latest_block
# last_proof_number = last_block.proof_number
#
# proof_number = blockchain.proof_of_work(last_proof_number)
#
# blockchain.get_data(
#     sender="0",  # this means that this node has constructed another block
#     receiver="Harshad",
#     amount=1  # building a new block (or figuring out the proof number) is awarded with 1
# )
#
# last_hash = last_block.compute_hash
#
# block = blockchain.build_block(proof_number, last_hash)
#
# print("Hurray, MINING HAS BEEN SUCCESSFUL!")
# print(blockchain.chain)
#
#       ''')
#
#
# def bc_p5b():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# contract constructors{
#
#     string str;
#     uint amount;
#
#     constructor(){
#         str  = "Shlok is learning Solidity";
#         amount = 10;
#     }
#
#     function const()public view returns(string memory,uint){
#         return (str,amount);
#
#     }
# }
#
#
#       ''')
#
# def bc_p5c():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
# abstract contract Main {
#     // Define an abstract function that can be overridden
#     function add(uint a, uint b) public virtual pure returns (uint);
# }
# contract Adder is Main {
#     // Override the add function from the Main contract
#     function add(uint a, uint b) public override pure returns (uint) {
#         return a + b;
#     }
# }
#     ''')
#
#
# def bc_p5d():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
# interface University { // Define the interface
# function getDepartment() external pure returns (string memory);
# function getCourses() external pure returns (string[4] memory);
# }
# contract Test is University { // Implement the contract
# function getDepartment() public pure override returns (string memory) {
# return &quot;Information Technology &amp; Data Science&quot;;
# }
# function getCourses() public pure override returns (string[4] memory) {
# return [
# &quot;Image Processing&quot;, &quot;Big Data&quot;, &quot;Networking&quot;, &quot;Machine Learning&quot;
# ];
# }
# }
#     ''')
#
#
# def bc_p6a():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# library Search {
#    function indexOf(uint[] storage self, uint value) internal view returns (uint) {
#       for (uint i = 0; i < self.length; i++) {
#          if (self[i] == value) {
#             return i;
#          }
#       }
#       return type(uint).max;
#
#    }
# }
#
# contract Test {
#    uint[] data;
#
#    constructor() {
#       data.push(1);
#       data.push(2);
#       data.push(3);
#       data.push(4);
#       data.push(5);
#    }
#
#    function isValuePresent() external view returns (uint) {
#       uint value = 4;
#
#       // Search if value is present in the array using Library function
#       uint index = Search.indexOf(data, value);
#       return index;
#    }
# }
#
# library MathLibrary {
#    function square(uint num) internal pure returns (uint) {
#       return num * num;
#    }
# }
#
# contract SquareContract {
#    using MathLibrary for uint;
#
#    function calculateSquare(uint num) external pure returns (uint) {
#       return num.square();
#    }
# }
#
#
#       ''')
#
#
# def bc_p6b():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
#
# library Sum {
#    function sumUsingInlineAssembly(uint[] memory _data) public pure returns (uint sum) {
#       for (uint i = 0; i < _data.length; ++i) {
#          assembly {
#             // Load the value from memory at the current index
#             let value := mload(add(add(_data, 0x20), mul(i, 0x20)))
#             // Add the value to the sum
#             sum := add(sum, value)
#          }
#       }
#       // Return the calculated sum
#       return sum;
#    }
# }
#
# contract Test {
#    uint[] data;
#
#    constructor() {
#       data.push(1);
#       data.push(2);
#       data.push(3);
#       data.push(4);
#       data.push(5);
#    }
#
#    function sum() external view returns (uint) {
#       return Sum.sumUsingInlineAssembly(data);
#    }
# }
#
#       ''')
#
#
# def bc_p6c():
#     print('''
# pragma solidity ^0.8.17;
#
# contract ErrorHandlingExample {
#     constructor() payable {
#   			      // Allow the contract to receive Ether during deployment
#     }
#
#     function divide(uint256 numerator, uint256 denominator) external pure returns (uint256) {
#         require(denominator != 0, "Division by zero is not allowed");
#         return numerator / denominator;
#     }
#
#     function withdraw(uint256 amount) external {
#         require(amount <= address(this).balance, "Insufficient balance");
#         payable(msg.sender).transfer(amount);
#     }
#
#     function assertExample() external pure {
#         uint256 x = 5;
#         uint256 y = 10;
#         assert(x < y);
#     }
#
#     function tryCatchExample() external view returns (bool, string memory) {
#         try this.divide(10, 5) returns (uint256 result) {
#            							 // Handle successful division
#             return (true, "Division successful");
#         } catch Error(string memory errorMessage) {	         // Handle division error
#
#             return (false, errorMessage);
#         } catch {			        			    // Handle unexpected errors
#             return (false, "Unexpected error occurred");
#         }
#     }
# }
#
#       ''')
#
#
# def bc_p6d():
#     print('''
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.17;
# contract EventExample { // Define an event
# event Deposit(address indexed from, uint256 amount);
# event Withdraw(address indexed to, uint256 amount);
# // Mapping to keep track of user balances
# mapping(address =&gt; uint256) public balances;
# // Function to deposit ether into the contract
# function deposit() public payable {
#
# require(msg.value &gt; 0, &quot;Must deposit more than 0 ether&quot;);
# balances[msg.sender] += msg.value; // Update the balance
# emit Deposit(msg.sender, msg.value); // Emit the Deposit event
# }
# function withdraw(uint256 amount) public { // Func to withdraw ether sc
# require(balances[msg.sender] &gt;= amount, &quot;Insufficient balance&quot;);
# balances[msg.sender] -= amount; // Update the balance
# payable(msg.sender).transfer(amount); // Transfer the ether
# emit Withdraw(msg.sender, amount); // Emit the Withdraw event
# }
# }
#     ''')
#
#
#
# def bc_p9():
#     print('''
# import requests
#
# # Task 1: Get information regarding the current block
# def get_current_block_info():
#     response = requests.get("https://blockchain.info/latestblock")
#     block_info = response.json()
#     print("Current block information:")
#     print("Block height:", block_info['height'])
#     print("Block hash:", block_info['hash'])
#     print("Block index:", block_info['block_index'])
#     print("Timestamp:", block_info['time'])
#
#
# # Task 3: Get balance of an address
# def get_address_balance(address):
#     response = requests.get(f"https://blockchain.info/q/addressbalance/{address}")
#     balance = float(response.text) / 10**8
#     print("Balance of address", address, ":", balance, "BTC")
#
# # Example usage
# if __name__ == "__main__":
#     # Task 1: Get information regarding the current block
#     get_current_block_info()
#
#     # Task 3: Get balance of an address
#     address = "3Dh2ft6UsqjbTNzs5zrp7uK17Gqg1Pg5u5"
#     get_address_balance(address)
#
#       ''')

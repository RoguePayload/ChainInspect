# Ethereum API endpoints
ETH_API_URL = 'https://api.ethereum.org/'
ETH_CONTRACT_ABI_URL = 'https://api.etherscan.io/api?module=contract&action=getabi&address={}&apikey=YourApiKeyToken'
ETH_CONTRACT_BYTECODE_URL = 'https://api.etherscan.io/api?module=proxy&action=eth_getCode&address={}&tag=latest&apikey=YourApiKeyToken'

# Binance Smart Chain API endpoints
BSC_API_URL = 'https://bscscan.com/'
BSC_CONTRACT_ABI_URL = 'https://api.bscscan.com/api?module=contract&action=getabi&address={}&apikey=YourApiKeyToken'
BSC_CONTRACT_BYTECODE_URL = 'https://api.bscscan.com/api?module=proxy&action=eth_getCode&address={}&tag=latest&apikey=YourApiKeyToken'

# Other blockchain API endpoints can be added as needed

# Common vulnerabilities
KNOWN_VULNERABILITIES = {
    'Reentrancy': 'https://consensys.net/diligence/blog/2019/09/stop-using-soliditys-transfer-now/',
    'Overflow/Underflow': 'https://solidity.readthedocs.io/en/v0.8.0/security-considerations.html#integer-overflow-and-underflow',
    'Unchecked External Calls': 'https://solidity.readthedocs.io/en/v0.8.0/security-considerations.html#unchecked-external-calls',
    'DoS with (Unexpected) revert': 'https://swcregistry.io/docs/SWC-116',
    'Unchecked Call Return Value': 'https://swcregistry.io/docs/SWC-133',
    'Use of Tx.origin': 'https://swcregistry.io/docs/SWC-114',
    'Floating Pragma': 'https://swcregistry.io/docs/SWC-106',
    'Uninitialized Storage Pointer': 'https://swcregistry.io/docs/SWC-128',
    'Delegatecall to Untrusted Callee': 'https://swcregistry.io/docs/SWC-112',
    'Front Running': 'https://swcregistry.io/docs/SWC-114',
    'Shadowing State Variables': 'https://swcregistry.io/docs/SWC-126',
    'Time Manipulation': 'https://swcregistry.io/docs/SWC-128',
    'Arbitrary Jump with Function Type Variable': 'https://swcregistry.io/docs/SWC-111',
    'DoS by External Contract Reference': 'https://swcregistry.io/docs/SWC-104',
    'Uninitialized Storage': 'https://swcregistry.io/docs/SWC-128',
    'Unchecked Retval': 'https://swcregistry.io/docs/SWC-133',
    'Assert Violation': 'https://swcregistry.io/docs/SWC-115',
    'Use of Deprecated Solidity Functions': 'https://swcregistry.io/docs/SWC-106',
    'Insufficient Gas Griefing': 'https://swcregistry.io/docs/SWC-116',
    'Incorrect Constructor Name': 'https://swcregistry.io/docs/SWC-105',
    'Insufficient Gas Griefing on Deployment': 'https://swcregistry.io/docs/SWC-116',
    'Uninitialized Argument Storage Pointer': 'https://swcregistry.io/docs/SWC-128',
    'DoS with Block Gas Limit': 'https://swcregistry.io/docs/SWC-128',
    'Missing Lock for Reentrancy': 'https://swcregistry.io/docs/SWC-107',
    'Missing Event Data': 'https://swcregistry.io/docs/SWC-131',
    'Floating Pragma': 'https://swcregistry.io/docs/SWC-106',
    'External Contract Reference': 'https://swcregistry.io/docs/SWC-104',
    'Unchecked SELFDESTRUCT': 'https://swcregistry.io/docs/SWC-106',
    'DoS with Failed Call': 'https://swcregistry.io/docs/SWC-117',
    'Assembly Call to Unknown Function': 'https://swcregistry.io/docs/SWC-132',
    'Short Address Attack': 'https://swcregistry.io/docs/SWC-130',
    'Uninitialized Pointer': 'https://swcregistry.io/docs/SWC-128',
    'Missing Arguments': 'https://swcregistry.io/docs/SWC-118',
    'Missing Return': 'https://swcregistry.io/docs/SWC-118',
    'Delegatecall Forwarding Attack': 'https://swcregistry.io/docs/SWC-112',
    'Floating Pragma': 'https://swcregistry.io/docs/SWC-106',
    'External Contract Size': 'https://swcregistry.io/docs/SWC-125',
    'Use of Uninitialized Storage Pointer': 'https://swcregistry.io/docs/SWC-128',
    'Use of Uninitialized Local Variable': 'https://swcregistry.io/docs/SWC-128',
    'Unhandled Exception': 'https://swcregistry.io/docs/SWC-113',
    'Redeclaration of Library': 'https://swcregistry.io/docs/SWC-127',
    'Floating Pragma': 'https://swcregistry.io/docs/SWC-106',
    'Uninitialized Constant': 'https://swcregistry.io/docs/SWC-128',
    'DoS with Block Gas Limit': 'https://swcregistry.io/docs/SWC-128',
    'Infinite Loop': 'https://swcregistry.io/docs/SWC-110',
    'Immutable Variable Modification': 'https://swcregistry.io/docs/SWC-110',
    'Unchecked SUICIDE': 'https://swcregistry.io/docs/SWC-106',
    'Weak Sources of Randomness from Chain Attributes': 'https://swcregistry.io/docs/SWC-130',
    'Non-Strict Equality Comparison': 'https://swcregistry.io/docs/SWC-120',
    'Insecure Dependency': 'https://swcregistry.io/docs/SWC-122',
    'Misleading Naming Convention': 'https://swcregistry.io/docs/SWC-121',
}
# Other constants related to smart contract auditing can be added as needed

# File paths
LOG_FILE_PATH = 'chaininspect.log'
CONFIG_FILE_PATH = 'config.ini'
DATA_DIR = 'data/'

# API endpoints
API_URL = 'https://api.example.com/'

# Logging levels
LOG_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
    'CRITICAL': 50
}

# Gas prices
GAS_PRICES = {
    'LOW': 1,
    'MEDIUM': 10,
    'HIGH': 100
}

# Blockchain network IDs
BLOCKCHAIN_NETWORK_IDS = {
    'MAINNET': 1,
    'ROPSTEN': 3,
    'RINKEBY': 4,
    'GOERLI': 5,
    'KOVAN': 42
}

# Security token standards
TOKEN_STANDARDS = {
    'ERC20': 'https://eips.ethereum.org/EIPS/eip-20',
    'ERC721': 'https://eips.ethereum.org/EIPS/eip-721',
    'ERC1155': 'https://eips.ethereum.org/EIPS/eip-1155'
}

# Contract status codes
CONTRACT_STATUSES = {
    'ACTIVE': 1,
    'INACTIVE': 0,
    'DEPRECATED': -1
}

# Audit report statuses
AUDIT_REPORT_STATUSES = {
    'PENDING': 'Pending',
    'IN_PROGRESS': 'In Progress',
    'COMPLETED': 'Completed',
    'FAILED': 'Failed'
}

# Audit report severities
AUDIT_REPORT_SEVERITIES = {
    'LOW': 'Low',
    'MEDIUM': 'Medium',
    'HIGH': 'High',
    'CRITICAL': 'Critical'
}

# API rate limits
API_RATE_LIMITS = {
    'BLOCKCHAIN_EXPLORER': 1000,  # Requests per minute
    'EXTERNAL_SERVICES': 500      # Requests per minute
}

# Timeouts
TIMEOUTS = {
    'API_REQUEST': 10,  # Timeout in seconds
    'CONTRACT_EXECUTION': 30  # Timeout in seconds
}

# Contract size limits
CONTRACT_SIZE_LIMITS = {
    'MAX_SIZE': 10000  # Maximum contract size in bytes
}

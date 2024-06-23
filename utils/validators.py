import re

def validate_contract_name(name):
    """
    Validate the name of a smart contract.
    The name should start with an uppercase letter and contain only letters, numbers, and underscores.
    """
    if not re.match("^[A-Z][A-Za-z0-9_]*$", name):
        raise ValueError("Invalid contract name. Name should start with an uppercase letter and contain only letters, numbers, and underscores.")

def validate_contract_address(address):
    """
    Validate the address of a smart contract.
    The address should be a hexadecimal string of length 40.
    """
    if not re.match("^(0x)?[0-9a-fA-F]{40}$", address):
        raise ValueError("Invalid contract address. Address should be a hexadecimal string of length 40.")

def validate_contract_source_code(source_code):
    """
    Validate the source code of a smart contract.
    The source code should be a non-empty string.
    """
    if not source_code:
        raise ValueError("Invalid contract source code. Source code should be a non-empty string.")

def validate_contract_abi(abi):
    """
    Validate the ABI (Application Binary Interface) of a smart contract.
    The ABI should be a list of dictionaries.
    """
    if not isinstance(abi, list) or not all(isinstance(item, dict) for item in abi):
        raise ValueError("Invalid contract ABI. ABI should be a list of dictionaries.")


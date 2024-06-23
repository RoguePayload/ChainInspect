import unittest
from core.parser import parse_smart_contract

class TestParser(unittest.TestCase):

    def test_parse_smart_contract(self):
        # Test parsing a simple smart contract code
        contract_code = """
        contract SimpleStorage {
            uint storedData;

            function set(uint x) public {
                storedData = x;
            }

            function get() public view returns (uint) {
                return storedData;
            }
        }
        """
        parsed_code = parse_smart_contract(contract_code)

        # Verify that the parsed code matches the expected structure
        expected_parsed_code = {
            'contract_name': 'SimpleStorage',
            'functions': [
                {'name': 'set', 'visibility': 'public', 'parameters': ['uint x'], 'return_type': 'void'},
                {'name': 'get', 'visibility': 'public', 'parameters': [], 'return_type': 'uint'}
            ]
        }
        self.assertEqual(parsed_code, expected_parsed_code)

if __name__ == '__main__':
    unittest.main()

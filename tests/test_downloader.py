import unittest
from unittest.mock import patch, Mock
import asyncio
from core.downloader import download_smart_contract

class TestDownloader(unittest.IsolatedAsyncioTestCase):

    async def test_download_smart_contract_success(self):
        # Mock the ClientSession to return a successful response
        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = Mock(status=200, text=asyncio.coroutine(lambda: 'Smart contract code'))
            mock_session.return_value.get.return_value.__aenter__.return_value = mock_response

            # Call the download_smart_contract function
            contract_code = await download_smart_contract('https://example.com/smart_contract.sol')

            # Assert that the function returns the correct contract code
            self.assertEqual(contract_code, 'Smart contract code')

    async def test_download_smart_contract_failure(self):
        # Mock the ClientSession to return a failed response
        with patch('aiohttp.ClientSession') as mock_session:
            mock_response = Mock(status=404, text=asyncio.coroutine(lambda: 'Not Found'))
            mock_session.return_value.get.return_value.__aenter__.return_value = mock_response

            # Call the download_smart_contract function
            with self.assertRaises(Exception) as context:
                await download_smart_contract('https://example.com/non_existent_contract.sol')

            # Assert that the function raises an exception
            self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()

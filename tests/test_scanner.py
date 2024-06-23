import unittest
from unittest.mock import patch, MagicMock
import asyncio
from core.scanner import scan_smart_contract

class TestScanner(unittest.IsolatedAsyncioTestCase):

    async def test_scan_smart_contract_success(self):
        # Mock download_smart_contract function
        with patch('core.downloader.download_smart_contract') as mock_download:
            mock_download.return_value = 'contract_code'

            # Mock subprocess.run to return a successful result
            mock_run = MagicMock()
            mock_run.stdout.decode.return_value = '{"mythril": "Mythril scan result", "slither": "Slither scan result"}'
            with patch('subprocess.run', return_value=mock_run):
                scan_result = await scan_smart_contract('contract_code')

                # Assert that the function returns the correct scan result
                self.assertEqual(scan_result, '{"mythril": "Mythril scan result", "slither": "Slither scan result"}')

    async def test_scan_smart_contract_failure(self):
        # Mock download_smart_contract function
        with patch('core.downloader.download_smart_contract') as mock_download:
            mock_download.return_value = 'contract_code'

            # Mock subprocess.run to raise an exception
            with patch('subprocess.run', side_effect=Exception('Error running scan')):
                with self.assertRaises(Exception) as context:
                    await scan_smart_contract('contract_code')

                # Assert that the function raises an exception
                self.assertIsNotNone(context.exception)

if __name__ == '__main__':
    unittest.main()

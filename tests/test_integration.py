import unittest
from unittest.mock import patch, MagicMock
from core.downloader import download_smart_contract
from core.parser import parse_smart_contract
from core.scanner import scan_smart_contract
from core.report_generator import generate_pdf_report

class TestIntegration(unittest.IsolatedAsyncioTestCase):

    async def test_integration_success(self):
        # Mock the download_smart_contract function to return a sample contract code
        with patch('core.downloader.download_smart_contract') as mock_download:
            mock_download.return_value = 'sample_contract_code'

            # Mock the scan_smart_contract function to return a sample scan result
            with patch('core.scanner.scan_smart_contract') as mock_scan:
                mock_scan.return_value = 'sample_scan_result'

                # Call the functions in sequence
                contract_code = await download_smart_contract('https://example.com/smart_contract.sol')
                parsed_code = parse_smart_contract(contract_code)
                scan_result = await scan_smart_contract(contract_code)
                report_file = generate_pdf_report(scan_result)

                # Assert that the report file was generated
                self.assertTrue(report_file.endswith('.pdf'))

    async def test_integration_failure(self):
        # Mock the download_smart_contract function to raise an exception
        with patch('core.downloader.download_smart_contract', side_effect=Exception('Error downloading contract')):
            # Call the download_smart_contract function and catch the exception
            with self.assertRaises(Exception) as context:
                await download_smart_contract('https://example.com/non_existent_contract.sol')

            # Assert that the exception message matches the expected message
            self.assertEqual(str(context.exception), 'Error downloading contract')

if __name__ == '__main__':
    unittest.main()

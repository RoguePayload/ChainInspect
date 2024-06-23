import unittest
from unittest.mock import patch
from core.report_generator import generate_pdf_report

class TestReportGenerator(unittest.TestCase):

    @patch('reportlab.pdfgen.canvas.Canvas')
    def test_generate_pdf_report_success(self, mock_canvas):
        # Mock the Canvas class to avoid actual PDF generation
        mock_canvas_instance = mock_canvas.return_value
        file_path = '/path/to/report.pdf'
        
        # Call the generate_pdf_report function
        generate_pdf_report('Scan Result', file_path)
        
        # Assert that the Canvas class was called with the correct arguments
        mock_canvas.assert_called_once_with(file_path, pagesize=(595.2755905511812, 841.8897637795277))
        
        # Assert that the drawString method was called with the correct arguments
        mock_canvas_instance.drawString.assert_called_once_with(100, 791.8897637795277, 'ChainInspect Smart Contract Audit Report')
        mock_canvas_instance.drawString.assert_called_with(100, 746.8897637795277, 'Scan Result')

    @patch('reportlab.pdfgen.canvas.Canvas')
    def test_generate_pdf_report_exception(self, mock_canvas):
        # Mock the Canvas class to raise an exception
        mock_canvas.side_effect = Exception('Error creating PDF')
        file_path = '/path/to/report.pdf'
        
        # Call the generate_pdf_report function and catch the exception
        with self.assertRaises(Exception) as context:
            generate_pdf_report('Scan Result', file_path)
        
        # Assert that the exception message matches the expected message
        self.assertEqual(str(context.exception), 'Error creating PDF')

if __name__ == '__main__':
    unittest.main()

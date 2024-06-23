import unittest
import tkinter as tk
from unittest.mock import patch
from gui.main_window import MainWindow

class TestGUI(unittest.TestCase):

    @patch('tkinter.Tk')
    def test_gui_initialization(self, mock_tk):
        # Mock the Tk class to avoid actual GUI initialization
        app = MainWindow()
        
        # Assert that the Tk class was called
        mock_tk.assert_called_once()
        
        # Assert that the title was set correctly
        app.root.title.assert_called_once_with('ChainInspect')
        
        # Assert that the geometry was set correctly
        app.root.geometry.assert_called_once_with('800x600')

    @patch('tkinter.Entry')
    @patch('tkinter.Button')
    @patch('tkinter.scrolledtext.ScrolledText')
    def test_gui_elements(self, mock_scrolledtext, mock_button, mock_entry):
        # Mock the Entry, Button, and ScrolledText classes to avoid actual GUI element creation
        app = MainWindow()
        
        # Assert that the URL label was created
        app.url_label.pack.assert_called_once()
        
        # Assert that the URL entry was created
        app.url_entry.pack.assert_called_once()
        
        # Assert that the Download button was created
        app.download_button.pack.assert_called_once()
        
        # Assert that the Scan button was created
        app.scan_button.pack.assert_called_once()
        
        # Assert that the ScrolledText widget was created
        app.report_text.pack.assert_called_once()

    @patch('tkinter.messagebox')
    def test_gui_download_button(self, mock_messagebox):
        # Mock the messagebox module to avoid actual message box display
        app = MainWindow()
        app.url_entry.get.return_value = 'https://example.com/smart_contract.sol'
        
        # Call the download_contract method
        app.download_contract()
        
        # Assert that the message box was not called for a valid URL
        mock_messagebox.showwarning.assert_not_called()

    @patch('tkinter.messagebox')
    def test_gui_scan_button(self, mock_messagebox):
        # Mock the messagebox module to avoid actual message box display
        app = MainWindow()
        app.url_entry.get.return_value = 'https://example.com/smart_contract.sol'
        
        # Call the scan_contract method
        app.scan_contract()
        
        # Assert that the message box was not called for a valid URL
        mock_messagebox.showwarning.assert_not_called()

if __name__ == '__main__':
    unittest.main()

import asyncio
import logging
import os
from tkinter import messagebox, scrolledtext, Button, Tk, Label, Entry

from core.downloader import download_smart_contract
from core.parser import parse_smart_contract
from core.scanner import scan_smart_contract
from core.report_generator import generate_pdf_report

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("ChainInspect")
        self.root.geometry("800x600")

        self.url_label = Label(self.root, text="Smart Contract URL:")
        self.url_label.pack(pady=10)

        self.url_entry = Entry(self.root, width=70)
        self.url_entry.pack(pady=10)

        self.download_button = Button(self.root, text="Download", command=self.download_contract)
        self.download_button.pack(pady=10)

        self.scan_button = Button(self.root, text="Scan", command=self.scan_contract)
        self.scan_button.pack(pady=10)

        self.report_text = scrolledtext.ScrolledText(self.root, height=20, width=80)
        self.report_text.pack(pady=20)

    async def download_contract(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        try:
            contract_code = await download_smart_contract(url)
            self.report_text.insert("end", "\n\nDownloaded Contract:\n" + contract_code)
            messagebox.showinfo("Download", "Downloaded the smart contract.")
        except Exception as e:
            messagebox.showerror("Download Error", str(e))

    async def scan_contract(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return

        try:
            contract_code = await download_smart_contract(url)
            parsed_code = await parse_smart_contract(contract_code)
            scan_result = await scan_smart_contract(parsed_code)
            self.report_text.insert("end", "\n\nScan Result:\n" + scan_result)
            report_file = os.path.join(os.path.dirname(__file__), "report.pdf")
            await generate_pdf_report(scan_result, report_file)
            messagebox.showinfo("Scan", "Scanned the smart contract. Report saved as report.pdf")
        except Exception as e:
            messagebox.showerror("Scan Error", str(e))

    def run(self):
        self.root.mainloop()

async def main():
    app = MainWindow()
    app.run()

if __name__ == "__main__":
    asyncio.run(main())

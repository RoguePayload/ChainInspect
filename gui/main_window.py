import tkinter as tk
from tkinter import messagebox, scrolledtext
import asyncio
from core.downloader import download_smart_contract
from core.parser import parse_smart_contract
from core.scanner import scan_smart_contract
from core.report_generator import generate_pdf_report

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ChainInspect")
        self.root.geometry("800x600")

        self.url_label = tk.Label(self.root, text="Smart Contract URL:")
        self.url_label.pack(pady=10)
        
        self.url_entry = tk.Entry(self.root, width=70)
        self.url_entry.pack(pady=10)
        
        self.download_button = tk.Button(self.root, text="Download", command=self.download_contract)
        self.download_button.pack(pady=10)
        
        self.scan_button = tk.Button(self.root, text="Scan", command=self.scan_contract)
        self.scan_button.pack(pady=10)

        self.report_text = scrolledtext.ScrolledText(self.root, height=20, width=80)
        self.report_text.pack(pady=20)
    
    async def download_contract_async(self, url):
        try:
            contract_code = await download_smart_contract(url)
            parsed_code = parse_smart_contract(contract_code)
            self.report_text.insert(tk.END, str(parsed_code))
            messagebox.showinfo("Download", "Downloaded and parsed the smart contract.")
        except Exception as e:
            messagebox.showerror("Download Error", str(e))
    
    def download_contract(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return
        
        asyncio.create_task(self.download_contract_async(url))
    
    async def scan_contract_async(self, url):
        try:
            contract_code = await download_smart_contract(url)
            scan_result = await scan_smart_contract(contract_code)
            self.report_text.insert(tk.END, "\n\nScan Result:\n" + scan_result)
            report_file = generate_pdf_report(scan_result)
            messagebox.showinfo("Scan", "Scanned the smart contract. Report saved as " + report_file)
        except Exception as e:
            messagebox.showerror("Scan Error", str(e))
    
    def scan_contract(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL.")
            return
        
        asyncio.create_task(self.scan_contract_async(url))
    
    def run(self):
        self.root.mainloop()

def main():
    app = MainWindow()
    app.run()

if __name__ == "__main__":
    main()

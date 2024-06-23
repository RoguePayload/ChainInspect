kimport asyncio
import json
import subprocess

async def scan_smart_contract(contract_code):
    try:
        mythril_command = ["myth", "analyze", "--solv", "0.6.10", "--execution-timeout", "60", "--max-depth", "12", "--max-transaction-count", "3", "--color", "0", "--json", "-"]
        slither_command = ["slither", "--json", "-"]

        # Run mythril command asynchronously
        mythril_process = await asyncio.create_subprocess_exec(*mythril_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mythril_stdout, _ = await mythril_process.communicate(input=contract_code.encode())
        mythril_result = json.loads(mythril_stdout.decode())

        # Run slither command asynchronously
        slither_process = await asyncio.create_subprocess_exec(*slither_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        slither_stdout, _ = await slither_process.communicate(input=contract_code.encode())
        slither_result = json.loads(slither_stdout.decode())

        # Combine and format results
        scan_result = {
            "mythril": mythril_result,
            "slither": slither_result
        }
        return json.dumps(scan_result, indent=4)
    except Exception as e:
        raise Exception(f"Failed to scan smart contract: {e}")


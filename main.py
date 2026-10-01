import argparse
from modules import osint_tool
from ai.ollama_client import OllamaClient

def main():
    parser = argparse.ArgumentParser(description="Local AI OSINT Auditor")
    parser.add_argument("--target", type=str, required=True, help="Instagram username to audit")
    args = parser.parse_args()

    print(f"🔍 Starting Local AI OSINT Audit for: @{args.target}")

    # Step 1: Get OSINT Data (Mocked for open-source demo)
    raw_data = osint_tool.get_mock_osint_data(args.target)

    # Step 2: Send to Local AI
    print("[*] Sending data to Local LLM for analysis...")
    ai = OllamaClient()
    report = ai.generate_privacy_report(raw_data)

    # Step 3: Output
    print("\n" + "="*50)
    print("       PRIVACY EXPOSURE AUDIT REPORT")
    print("="*50)
    print(report)

if __name__ == "__main__":
    main()
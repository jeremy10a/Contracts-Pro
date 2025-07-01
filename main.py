import json
from modules.procurement import extract_vendor_fees
from modules.finance import extract_payment_terms
from modules.legal import extract_legal_flags
from modules.startups import extract_revenue_share

def analyze_contract(text):
    return {
        "procurement": extract_vendor_fees(text),
        "finance": extract_payment_terms(text),
        "legal": extract_legal_flags(text),
        "startups": extract_revenue_share(text)
    }

if __name__ == "__main__":
    with open("sample_contract.txt") as f:
        contract_text = f.read()

    results = analyze_contract(contract_text)
    print(json.dumps(results, indent=2))

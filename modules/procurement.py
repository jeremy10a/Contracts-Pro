import re

def extract_vendor_fees(text):
    vendors = re.findall(r'(\b[A-Z][a-zA-Z]+ Inc\.|\b[A-Z][a-zA-Z]+ LLC)', text)
    fees = re.findall(r'\$[\d,]+(?:\.\d{2})?', text)
    recurring = [f for f in fees if "monthly" in text.lower() or "annual" in text.lower()]
    return {
        "vendors_detected": list(set(vendors)),
        "recurring_fees": recurring
    }

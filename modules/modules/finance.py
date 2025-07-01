import re

def extract_payment_terms(text):
    terms = re.findall(r'Net\s*(\d+)', text)
    return {
        "net_terms": [int(t) for t in terms]
    }

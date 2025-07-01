def extract_legal_flags(text):
    flags = {}
    if "indemnify" in text.lower() and "uncapped" in text.lower():
        flags["uncapped_indemnity"] = True
    if "termination fee" in text.lower() and "$" in text:
        flags["termination_fee"] = True
    return flags

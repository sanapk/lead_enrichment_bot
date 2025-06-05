import requests

def enrich_company(company):
    url = f"https://autocomplete.clearbit.com/v1/companies/suggest?query={company}"
    try:
        res = requests.get(url, timeout=5).json()
        if res:
            return {
                "company_name": company,
                "website": res[0].get("domain", ""),
                "industry": res[0].get("type", "")
            }
    except Exception:
        pass
    return {"company_name": company, "website": "", "industry": ""}

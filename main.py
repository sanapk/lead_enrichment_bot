import pandas as pd
from helpers.enrich import enrich_company
from helpers.scraper import scrape_homepage
from helpers.ai_analysis import analyze_with_llm

df = pd.read_csv("data/input.csv")
results = []

for _, row in df.iterrows():
    company = row['company_name']
    info = enrich_company(company)
    homepage_text = scrape_homepage(info['website'])
    llm = analyze_with_llm(homepage_text)
    
    results.append({
        **info,
        "summary_from_llm": llm['summary'],
        "automation_pitch_from_llm": llm['pitch']
    })

out_df = pd.DataFrame(results)
out_df.to_csv("data/enriched_output.csv", index=False)

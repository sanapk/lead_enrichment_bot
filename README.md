# Lead Enrichment Bot

Upload a list of company names → Get their website, industry, homepage analysis, and a pitch for AI automation!

# Features

-  Enrich company data using Clearbit
-  Scrape homepage text using BeautifulSoup
-  Use Gemini to summarize and suggest automation
- Download final CSV
-  Simple Streamlit UI

sample input:
- already mentioned in the data/input.csv
sample output:
- already mentioned in the data/enriched_output.csv

sample video:
https://drive.google.com/file/d/1Ptsj2OAzS7nQ7XbQ1FHkrC-8yFyGtXRW/view?usp=drivesdk

```bash
git clone https://sanapk/lead_enrichment_bot
cd lead_enrichment_bot
pip install -r requirements.txt
streamlit run app.py



import streamlit as st
import pandas as pd
from helpers.enrich import enrich_company
from helpers.scraper import scrape_homepage
from helpers.ai_analysis import analyze_with_llm

st.set_page_config(page_title="AI LeadGen Enrichment", layout="centered")
st.title("🔍 AI-Powered LeadGen Tool")

# Upload CSV
file = st.file_uploader("📤 Upload CSV file (must have 'company_name' column)", type=["csv"])

if file:
    try:
        df = pd.read_csv(file)
        if "company_name" not in df.columns:
            st.error("❌ The CSV must contain a column named 'company_name'.")
        else:
            st.success("✅ File uploaded successfully!")
            st.subheader("📋 Preview of Uploaded Data")
            st.dataframe(df.head())

            # Enrichment
            enriched_data = []

            with st.spinner("🔄 Enriching company data..."):
                for _, row in df.iterrows():
                    name = row["company_name"]

                    try:
                        info = enrich_company(name)
                        homepage = scrape_homepage(info.get("website", ""))
                        ai = analyze_with_llm(homepage)

                        enriched_data.append({
                            "company_name": name,
                            "website": info.get("website", ""),
                            "industry": info.get("industry", ""),
                            "summary_from_llm": ai.get("summary", ""),
                            "automation_pitch_from_llm": ai.get("pitch", "")
                        })
                    except Exception as e:
                        enriched_data.append({
                            "company_name": name,
                            "website": "ERROR",
                            "industry": "ERROR",
                            "company_size": "ERROR",
                            "hq_location": "ERROR",
                            "summary_from_llm": f"Error: {e}",
                            "automation_pitch_from_llm": "N/A"
                        })

            # Final DataFrame
            out_df = pd.DataFrame(enriched_data)

            st.success("✅ Enrichment complete!")
            st.subheader("📈 Enriched Output")
            st.dataframe(out_df)

            # Download button
            st.download_button(
                label="📥 Download Enriched CSV",
                data=out_df.to_csv(index=False),
                file_name="enriched_output.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Failed to process file: {e}")

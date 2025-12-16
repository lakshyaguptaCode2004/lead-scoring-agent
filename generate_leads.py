import pandas as pd
from src.identification import load_profiles
from src.enrichment import enrich_profile
from src.scoring import calculate_score

print("✅ generate_leads.py started")

# Load data
profiles = load_profiles("data/linkedin_profiles.csv")
pubmed = pd.read_csv("data/pubmed_papers.csv")
funding = pd.read_csv("data/funding_data.csv")

print(f"Loaded {len(profiles)} LinkedIn profiles")

rows = []

for _, profile in profiles.iterrows():
    enrich = enrich_profile(profile, pubmed, funding)
    score = calculate_score(profile, enrich)

    rows.append({
        "Name": profile["name"],
        "Title": profile["title"],
        "Company": profile["company"],
        "Person Location": profile["person_location"],
        "HQ Location": enrich["hq_location"],
        "Probability Score": score,
        "LinkedIn": profile["linkedin_url"]
    })

df = pd.DataFrame(rows).sort_values("Probability Score", ascending=False)

df.to_csv("lead_output.csv", index=False)

print("✅ Leads generated → lead_output.csv")

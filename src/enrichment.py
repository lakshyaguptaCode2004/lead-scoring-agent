def enrich_profile(profile, pubmed_df, funding_df):
    result = {}

    # Scientific intent: recent paper?
    papers = pubmed_df[
        pubmed_df["author"].str.contains(
            profile["name"].split()[0], case=False, na=False
        )
    ]
    result["recent_paper"] = not papers.empty

    # Funding & HQ info
    funding = funding_df[funding_df["company"] == profile["company"]]
    if not funding.empty:
        result["funding_stage"] = funding.iloc[0]["funding_stage"]
        result["hq_location"] = funding.iloc[0]["hq_location"]
    else:
        result["funding_stage"] = "Unknown"
        result["hq_location"] = "Unknown"

    return result

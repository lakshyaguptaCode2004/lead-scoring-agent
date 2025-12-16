def calculate_score(profile, enrichment):
    score = 0

    title = profile["title"].lower()

    # Role fit
    if any(keyword in title for keyword in ["toxicology", "safety", "hepatic", "3d"]):
        score += 30

    # Funding intent
    if enrichment.get("funding_stage") in ["Series A", "Series B"]:
        score += 20

    # Location hub
    hq = enrichment.get("hq_location", "").lower()
    if any(city in hq for city in ["cambridge", "boston", "bay", "san francisco"]):
        score += 10

    # Scientific intent
    if enrichment.get("recent_paper"):
        score += 40

    return min(score, 100)

from smart_agri_agent.models.contracts import FarmRecommendationInput, FarmRecommendationOutput

def generate_recommendation(data: FarmRecommendationInput) -> FarmRecommendationOutput:
    """
    Synthesizes all data points into a final, actionable recommendation for the farmer.
    """
    plan = []
    summary = ""
    
    if data.overall_risk_score > 70:
        summary = f"CRITICAL: High risk farming conditions detected (Score: {data.overall_risk_score}). Immediate action required."
    elif data.overall_risk_score > 30:
        summary = f"WARNING: Moderate risk conditions (Score: {data.overall_risk_score}). Monitor closely."
    else:
        summary = f"ALL CLEAR: Favorable farming conditions (Score: {data.overall_risk_score}). Proceed with standard operations."
        
    if data.soil_health_score < 60:
        plan.append("Apply soil amendments immediately to correct deficiencies.")
        
    if data.disease_risk_level in ["HIGH", "MED"]:
        plan.append("Apply preventative fungicide/pesticide treatments for potential diseases.")
        
    if data.water_needed_liters > 0:
        plan.append(f"Ensure irrigation system is prepared to deliver {data.water_needed_liters} L/sqm.")
        
    plan.append(f"Consider planting: {', '.join(data.suitable_crops) if data.suitable_crops else 'No suitable crops recommended at this time'}.")
    
    return FarmRecommendationOutput(
        action_plan=plan,
        summary=summary
    )

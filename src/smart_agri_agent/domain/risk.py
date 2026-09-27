from smart_agri_agent.models.contracts import FarmRiskAssessmentInput, FarmRiskAssessmentOutput

def assess_farm_risk(data: FarmRiskAssessmentInput) -> FarmRiskAssessmentOutput:
    """
    Aggregates soil, weather, and disease risks into a holistic risk score.
    """
    score = 0.0
    warnings = []
    
    # Analyze soil deficiencies
    if len(data.soil_deficiencies) > 2:
        score += 30
        warnings.append("Multiple severe soil nutrient deficiencies.")
    elif len(data.soil_deficiencies) > 0:
        score += 15
        warnings.append("Minor soil deficiencies detected.")
        
    # Analyze weather extremes
    if data.weather_extremes:
        score += 40
        warnings.append("Extreme weather conditions expected.")
        
    # Analyze disease risk
    if data.disease_risk == "HIGH":
        score += 30
        warnings.append("High risk of crop disease.")
    elif data.disease_risk == "MED":
        score += 15
        
    score = min(100.0, score)
    
    return FarmRiskAssessmentOutput(
        overall_risk_score=round(score, 2),
        critical_warnings=warnings
    )

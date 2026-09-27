from smart_agri_agent.models.contracts import SoilAnalysisInput, SoilAnalysisOutput

def analyze_soil(data: SoilAnalysisInput) -> SoilAnalysisOutput:
    """
    Evaluates soil parameters against standard baselines.
    Target optimal: pH=6.5, N=100, P=20, K=100
    """
    deficiencies = []
    
    if data.N < 50:
        deficiencies.append("Low Nitrogen")
    if data.P < 10:
        deficiencies.append("Low Phosphorus")
    if data.K < 50:
        deficiencies.append("Low Potassium")
    if data.pH < 5.5:
        deficiencies.append("High Acidity")
    elif data.pH > 7.5:
        deficiencies.append("High Alkalinity")
        
    # Calculate a simplified health score 0-100
    ph_score = max(0, 100 - (abs(data.pH - 6.5) * 20))
    n_score = min(100, data.N)
    p_score = min(100, data.P * 5)
    k_score = min(100, data.K)
    
    health_score = (ph_score + n_score + p_score + k_score) / 4.0
    
    return SoilAnalysisOutput(
        health_score=round(health_score, 2),
        deficiencies=deficiencies
    )

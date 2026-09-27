from smart_agri_agent.models.contracts import CropDiseaseRiskInput, CropDiseaseRiskOutput

def assess_disease_risk(data: CropDiseaseRiskInput) -> CropDiseaseRiskOutput:
    """
    Assesses the likelihood of specific crop diseases based on humidity, temperature, and crop type.
    """
    risk_level = "LOW"
    potential_diseases = []
    
    # Simple deterministic rules
    if data.humidity > 80:
        if data.avg_temp > 25:
            risk_level = "HIGH"
            potential_diseases.append("Fungal Infection (e.g., Rust/Blight)")
        elif data.avg_temp > 15:
            risk_level = "MED"
            potential_diseases.append("Mildew")
            
    if data.crop == "Wheat" and data.humidity > 70 and data.avg_temp > 20:
        potential_diseases.append("Wheat Rust")
        risk_level = "HIGH"
        
    if data.crop == "Rice" and data.humidity > 85:
        potential_diseases.append("Rice Blast")
        risk_level = "HIGH"
        
    return CropDiseaseRiskOutput(
        risk_level=risk_level,
        potential_diseases=potential_diseases
    )

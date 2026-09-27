from smart_agri_agent.models.contracts import CropSuitabilityInput, CropSuitabilityOutput

def evaluate_crop_suitability(data: CropSuitabilityInput) -> CropSuitabilityOutput:
    """
    Recommends viable crops based on soil health and region.
    """
    suitable_crops = []
    
    # Generic logic for demonstration
    if data.soil_health > 80:
        suitable_crops.extend(["Wheat", "Corn", "Soybeans"])
    elif data.soil_health > 50:
        suitable_crops.extend(["Barley", "Oats"])
    else:
        suitable_crops.extend(["Cassava", "Millet"])
        
    if data.region.lower() in ["tropical", "equatorial"]:
        suitable_crops = [c for c in suitable_crops if c not in ["Wheat", "Barley", "Oats"]]
        suitable_crops.extend(["Rice", "Sugarcane"])
        
    confidence = round(data.soil_health / 100.0, 2)
    
    return CropSuitabilityOutput(
        suitable_crops=list(set(suitable_crops)),
        confidence=confidence
    )

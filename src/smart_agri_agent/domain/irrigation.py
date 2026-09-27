from smart_agri_agent.models.contracts import IrrigationAdvisorInput, IrrigationAdvisorOutput

def advise_irrigation(data: IrrigationAdvisorInput) -> IrrigationAdvisorOutput:
    """
    Calculates watering needs based on crop type, soil moisture, and weather forecast.
    """
    # Base requirement per square meter
    base_water_needs = {
        "Rice": 15.0,
        "Sugarcane": 12.0,
        "Corn": 8.0,
        "Wheat": 6.0,
        "Soybeans": 7.0,
        "Millet": 4.0,
        "Cassava": 5.0
    }
    
    crop = data.crop if data.crop in base_water_needs else "Corn"
    daily_need = base_water_needs[crop]
    
    # Adjust based on current soil moisture (0-100)
    # If moisture is high, need less water
    moisture_deficit = max(0, 70 - data.soil_moisture) / 100.0
    
    # Calculate required water
    water_required = daily_need * (1.0 + moisture_deficit)
    
    # Subtract forecasted rain
    water_required = max(0, water_required - data.forecast_rain)
    
    if water_required == 0:
        frequency = "Skip watering"
    elif water_required < 3:
        frequency = "every 3 days"
    elif water_required < 7:
        frequency = "every 2 days"
    else:
        frequency = "daily"
        
    return IrrigationAdvisorOutput(
        water_needed_liters=round(water_required, 2),
        frequency=frequency
    )

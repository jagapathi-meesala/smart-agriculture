from typing import Dict, Any
from smart_agri_agent.core.registry import ToolRegistry

class ExecutionEngine:
    """
    Manages rules, evaluations, and workflow steps by executing tools from the registry.
    """
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute_pipeline(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes the agricultural analysis pipeline using deterministic tools.
        The context must contain: 'pH', 'N', 'P', 'K', 'region', 'crop', 'soil_moisture', 'location'.
        """
        results = {}

        # 1. Soil Analysis
        soil_out = self.registry.execute(
            "soil-analysis", 
            pH=context["pH"], N=context["N"], P=context["P"], K=context["K"]
        )
        results["soil_health_score"] = soil_out.health_score
        results["soil_deficiencies"] = soil_out.deficiencies
        
        # 2. Crop Suitability
        crop_out = self.registry.execute(
            "crop-suitability", 
            soil_health=soil_out.health_score, region=context["region"]
        )
        results["suitable_crops"] = crop_out.suitable_crops
        
        # 3. Weather Analysis
        weather_extremes = False
        try:
            weather_out = self.registry.execute("weather-analysis", location=context["location"], days=3)
            results["weather"] = weather_out.model_dump()
            forecast_rain = weather_out.rain_chance * 0.1 # Simplistic estimation
            if weather_out.avg_temp > 35 or weather_out.avg_temp < 5:
                weather_extremes = True
        except Exception as e:
            # Handle external API failure safely
            results["weather_error"] = str(e)
            weather_out = None
            forecast_rain = 0.0
            
        # 4. Irrigation Advisor
        irrigation_out = self.registry.execute(
            "irrigation-advisor",
            crop=context["crop"], soil_moisture=context["soil_moisture"], forecast_rain=forecast_rain
        )
        results["water_needed_liters"] = irrigation_out.water_needed_liters
        
        # 5. Disease Risk
        if weather_out:
            disease_out = self.registry.execute(
                "crop-disease-risk",
                crop=context["crop"], humidity=weather_out.humidity, avg_temp=weather_out.avg_temp
            )
        else:
            # Fallback if weather is unavailable
            disease_out = self.registry.execute(
                "crop-disease-risk",
                crop=context["crop"], humidity=50.0, avg_temp=20.0
            )
        results["disease_risk_level"] = disease_out.risk_level
        
        # 6. Farm Risk Assessment
        risk_out = self.registry.execute(
            "farm-risk-assessment",
            soil_deficiencies=soil_out.deficiencies,
            weather_extremes=weather_extremes,
            disease_risk=disease_out.risk_level
        )
        results["overall_risk_score"] = risk_out.overall_risk_score
        
        # 7. Farm Recommendation
        rec_out = self.registry.execute(
            "farm-recommendation",
            soil_health_score=soil_out.health_score,
            suitable_crops=crop_out.suitable_crops,
            water_needed_liters=irrigation_out.water_needed_liters,
            weather_avg_temp=weather_out.avg_temp if weather_out else 20.0,
            disease_risk_level=disease_out.risk_level,
            overall_risk_score=risk_out.overall_risk_score
        )
        
        results["recommendation"] = rec_out.model_dump()
        return results

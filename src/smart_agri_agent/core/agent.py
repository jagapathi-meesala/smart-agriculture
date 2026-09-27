from typing import Dict, Any
from smart_agri_agent.core.registry import ToolRegistry
from smart_agri_agent.core.engine import ExecutionEngine

# Import domain tools
from smart_agri_agent.domain.soil import analyze_soil
from smart_agri_agent.domain.crop import evaluate_crop_suitability
from smart_agri_agent.domain.irrigation import advise_irrigation
from smart_agri_agent.domain.weather import analyze_weather
from smart_agri_agent.domain.disease import assess_disease_risk
from smart_agri_agent.domain.risk import assess_farm_risk
from smart_agri_agent.domain.recommend import generate_recommendation

# Import contracts
from smart_agri_agent.models.contracts import (
    SoilAnalysisInput, SoilAnalysisOutput,
    CropSuitabilityInput, CropSuitabilityOutput,
    IrrigationAdvisorInput, IrrigationAdvisorOutput,
    WeatherAnalysisInput, WeatherAnalysisOutput,
    CropDiseaseRiskInput, CropDiseaseRiskOutput,
    FarmRiskAssessmentInput, FarmRiskAssessmentOutput,
    FarmRecommendationInput, FarmRecommendationOutput
)

class AgentCore:
    """
    The Single Source of Truth for the Smart Agriculture Agent.
    """
    def __init__(self):
        self.registry = ToolRegistry()
        self._register_tools()
        self.engine = ExecutionEngine(self.registry)

    def _register_tools(self):
        self.registry.register("soil-analysis", analyze_soil, SoilAnalysisInput, SoilAnalysisOutput)
        self.registry.register("crop-suitability", evaluate_crop_suitability, CropSuitabilityInput, CropSuitabilityOutput)
        self.registry.register("irrigation-advisor", advise_irrigation, IrrigationAdvisorInput, IrrigationAdvisorOutput)
        self.registry.register("weather-analysis", analyze_weather, WeatherAnalysisInput, WeatherAnalysisOutput)
        self.registry.register("crop-disease-risk", assess_disease_risk, CropDiseaseRiskInput, CropDiseaseRiskOutput)
        self.registry.register("farm-risk-assessment", assess_farm_risk, FarmRiskAssessmentInput, FarmRiskAssessmentOutput)
        self.registry.register("farm-recommendation", generate_recommendation, FarmRecommendationInput, FarmRecommendationOutput)

    def process_request(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Public API for the adapters.
        """
        return self.engine.execute_pipeline(input_data)

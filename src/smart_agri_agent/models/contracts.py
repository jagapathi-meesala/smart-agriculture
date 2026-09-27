from pydantic import BaseModel, Field
from typing import List

# --- Soil Analysis ---
class SoilAnalysisInput(BaseModel):
    pH: float = Field(..., description="Soil pH level")
    N: int = Field(..., description="Nitrogen content in mg/kg")
    P: int = Field(..., description="Phosphorus content in mg/kg")
    K: int = Field(..., description="Potassium content in mg/kg")

class SoilAnalysisOutput(BaseModel):
    health_score: float = Field(..., description="Calculated soil health score (0-100)")
    deficiencies: List[str] = Field(default_factory=list, description="List of identified nutrient deficiencies")

# --- Crop Suitability ---
class CropSuitabilityInput(BaseModel):
    soil_health: float = Field(..., description="Soil health score (0-100)")
    region: str = Field(..., description="Geographical region of the farm")

class CropSuitabilityOutput(BaseModel):
    suitable_crops: List[str] = Field(default_factory=list, description="List of recommended crops")
    confidence: float = Field(..., description="Confidence score (0-1)")

# --- Irrigation Advisor ---
class IrrigationAdvisorInput(BaseModel):
    crop: str = Field(..., description="Target crop")
    soil_moisture: float = Field(..., description="Current soil moisture percentage (0-100)")
    forecast_rain: float = Field(..., description="Forecasted rainfall in mm")

class IrrigationAdvisorOutput(BaseModel):
    water_needed_liters: float = Field(..., description="Liters of water needed per square meter")
    frequency: str = Field(..., description="Recommended watering frequency (e.g., 'daily', 'every 3 days')")

# --- Weather Analysis ---
class WeatherAnalysisInput(BaseModel):
    location: str = Field(..., description="Farm location")
    days: int = Field(default=3, description="Number of days to forecast")

class WeatherAnalysisOutput(BaseModel):
    avg_temp: float = Field(..., description="Average temperature in Celsius")
    humidity: float = Field(..., description="Average humidity percentage")
    rain_chance: float = Field(..., description="Probability of rain (0-100)")

# --- Crop Disease Risk ---
class CropDiseaseRiskInput(BaseModel):
    crop: str = Field(..., description="Target crop")
    humidity: float = Field(..., description="Average humidity percentage")
    avg_temp: float = Field(..., description="Average temperature in Celsius")

class CropDiseaseRiskOutput(BaseModel):
    risk_level: str = Field(..., description="Risk level: LOW, MED, HIGH")
    potential_diseases: List[str] = Field(default_factory=list, description="List of potential diseases")

# --- Farm Risk Assessment ---
class FarmRiskAssessmentInput(BaseModel):
    soil_deficiencies: List[str] = Field(..., description="List of soil deficiencies")
    weather_extremes: bool = Field(..., description="Whether extreme weather conditions are expected")
    disease_risk: str = Field(..., description="Disease risk level (LOW/MED/HIGH)")

class FarmRiskAssessmentOutput(BaseModel):
    overall_risk_score: float = Field(..., description="Overall risk score (0-100)")
    critical_warnings: List[str] = Field(default_factory=list, description="List of critical warnings")

# --- Farm Recommendation ---
class FarmRecommendationInput(BaseModel):
    soil_health_score: float
    suitable_crops: List[str]
    water_needed_liters: float
    weather_avg_temp: float
    disease_risk_level: str
    overall_risk_score: float

class FarmRecommendationOutput(BaseModel):
    action_plan: List[str] = Field(default_factory=list, description="Actionable steps for the farmer")
    summary: str = Field(..., description="Final comprehensive summary/recommendation")

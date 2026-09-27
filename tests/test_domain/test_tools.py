from smart_agri_agent.domain.soil import analyze_soil
from smart_agri_agent.models.contracts import SoilAnalysisInput

def test_soil_analysis_healthy():
    input_data = SoilAnalysisInput(pH=6.5, N=100, P=20, K=100)
    output = analyze_soil(input_data)
    assert output.health_score > 90
    assert len(output.deficiencies) == 0

def test_soil_analysis_deficient():
    input_data = SoilAnalysisInput(pH=5.0, N=30, P=5, K=30)
    output = analyze_soil(input_data)
    assert output.health_score < 70
    assert "Low Nitrogen" in output.deficiencies
    assert "High Acidity" in output.deficiencies
    
# More tests could be added for other tools...

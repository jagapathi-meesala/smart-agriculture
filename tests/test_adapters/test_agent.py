from smart_agri_agent.core.agent import AgentCore

def test_agent_core_pipeline(monkeypatch):
    # Mock the weather tool so we don't rely on external network in tests
    agent = AgentCore()
    
    # Simple monkeypatch of the weather domain tool output
    from smart_agri_agent.models.contracts import WeatherAnalysisOutput
    
    def mock_weather(*args, **kwargs):
        return WeatherAnalysisOutput(avg_temp=25.0, humidity=60.0, rain_chance=10.0)
        
    # We replace the actual registered function in the registry
    agent.registry._tools["weather-analysis"]["func"] = mock_weather
    
    context = {
        "location": "Test Farm",
        "region": "temperate",
        "crop": "Corn",
        "pH": 6.5,
        "N": 100,
        "P": 20,
        "K": 100,
        "soil_moisture": 40.0
    }
    
    results = agent.process_request(context)
    
    assert "recommendation" in results
    assert "overall_risk_score" in results
    assert "soil_health_score" in results
    assert results["soil_health_score"] == 100.0  # Perfect soil
    assert results["overall_risk_score"] < 50.0   # Low risk due to good inputs

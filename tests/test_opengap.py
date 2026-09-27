import os
import yaml
import pytest
from smart_agri_agent.core.agent import AgentCore

def test_opengap_manifest_consistency():
    """
    Dynamically discover the registered Python tools and compare them 
    with the declared tools in the tools/ directory.
    """
    agent = AgentCore()
    python_tools = set(agent.registry.list_tools())
    
    tools_dir = os.path.join(os.path.dirname(__file__), "..", "tools")
    yaml_tools = set()
    
    for filename in os.listdir(tools_dir):
        if filename.endswith(".yaml"):
            with open(os.path.join(tools_dir, filename), "r") as f:
                schema = yaml.safe_load(f)
                yaml_tools.add(schema["name"])
                
    assert python_tools == yaml_tools, f"Mismatch between implemented tools {python_tools} and OpenGAP YAML tools {yaml_tools}"

def test_opengap_agent_yaml():
    """
    Check if the main agent.yaml exists and is valid.
    """
    agent_yaml_path = os.path.join(os.path.dirname(__file__), "..", "agent.yaml")
    assert os.path.exists(agent_yaml_path)
    
    with open(agent_yaml_path, "r") as f:
        manifest = yaml.safe_load(f)
        
    assert manifest["spec_version"] == "0.1.0"
    assert "name" in manifest
    assert "description" in manifest

import sys
import json
from dotenv import load_dotenv
from smart_agri_agent.core.agent import AgentCore

def main():
    load_dotenv()
    
    print("Welcome to Smart Agriculture Agent")
    print("----------------------------------")
    
    # Normally we would parse args, using hardcoded for demonstration
    # if not doing an interactive prompt. Let's do a basic interactive prompt.
    
    try:
        location = input("Enter farm location (e.g., 'Nairobi, Kenya'): ")
        region = input("Enter region type (e.g., 'tropical', 'temperate'): ")
        crop = input("Enter target crop (e.g., 'Wheat', 'Corn'): ")
        
        ph = float(input("Enter soil pH (e.g., 6.5): "))
        n = int(input("Enter Nitrogen mg/kg (e.g., 100): "))
        p = int(input("Enter Phosphorus mg/kg (e.g., 20): "))
        k = int(input("Enter Potassium mg/kg (e.g., 100): "))
        
        soil_moisture = float(input("Enter soil moisture % (0-100): "))
        
    except ValueError:
        print("Invalid input type provided. Exiting.")
        sys.exit(1)
        
    context = {
        "location": location,
        "region": region,
        "crop": crop,
        "pH": ph,
        "N": n,
        "P": p,
        "K": k,
        "soil_moisture": soil_moisture
    }
    
    agent = AgentCore()
    
    print("\nProcessing...\n")
    try:
        results = agent.process_request(context)
        print("====== RESULTS ======")
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"\nError processing request: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

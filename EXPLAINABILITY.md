# Explainability Statement

## 1. Purpose
The Smart Agriculture Agent provides transparent, data-driven, and explainable decision support for farmers. Its goal is to analyze environmental and soil conditions logically and present clear recommendations, ensuring that farmers understand exactly why specific actions are advised.

## 2. Decision Architecture
The agent follows a strict, linear decision flow to ensure maximum explainability:
User Input 
→ AgentCore (Single Source of Truth) 
→ Tool Registry 
→ Domain Tool 
→ Structured Result 
→ Recommendation

This architecture guarantees that business logic resides solely within deterministic domain tools, not within ambiguous LLM prompts or UI adapters.

## 3. Tool Explainability
Every tool relies on explicit inputs and generates defined outputs:
- **soil-analysis**: Uses mathematical baselines for pH, Nitrogen, Phosphorus, and Potassium to calculate a normalized health score and list distinct nutrient deficiencies.
- **crop-suitability**: Cross-references the calculated soil health score with the geographical region to filter and recommend viable crops.
- **irrigation-advisor**: Calculates daily water requirements (L/sqm) based on base crop needs, adjusted by current soil moisture deficits and forecasted rainfall.
- **weather-analysis**: Interprets external meteorological data (temperature, humidity, precipitation) directly from an external provider adapter without modification.
- **crop-disease-risk**: Uses hardcoded thresholds for humidity and temperature mapped against specific crops to determine the risk level (LOW/MED/HIGH) of fungal or bacterial infections.
- **farm-risk-assessment**: Aggregates the identified soil deficiencies, weather extremes, and disease risks into a holistic, weighted overall risk score (0-100).
- **farm-recommendation**: Synthesizes the structured outputs of all prior tools into a final summary and actionable steps, ensuring every recommendation corresponds directly to an underlying metric.

## 4. Data Sources
The system explicitly distinguishes its data sources:
- **User-provided measurements**: Real-time soil metrics, moisture levels, and farm location.
- **Deterministic/rule-based calculations**: Risk scores, irrigation deficits, and crop suitability derived via pure code logic.
- **External weather data**: Fetched from live meteorological APIs (e.g., Open-Meteo).
- **Unavailable external data**: Clearly flagged when an API fails, preventing downstream tools from making unsafe assumptions.

## 5. No Fabrication
The agent must not invent weather, soil measurements, crop conditions, disease observations, or external API results. If data is missing or a service fails, the agent will explicitly report the gap rather than hallucinating plausible values.

## 6. Recommendation Traceability
Every piece of advice in the final action plan maps directly back to the structured outputs of the domain tools. If the agent recommends applying a fungicide, it is strictly because the `crop-disease-risk` tool returned a HIGH risk level, which in turn was driven by specific temperature and humidity thresholds. 

## 7. Risk and Limitations
- The outputs provided are strictly **decision support**.
- Real-world agricultural conditions can vary wildly due to microclimates or unmeasured variables.
- External weather and API data can be temporarily unavailable or inaccurate.
- The recommendations are mathematically sound but are **not guaranteed outcomes**.
- Local agricultural expertise should always be consulted for high-impact or financial decisions.

## 8. Error Handling
Invalid inputs are caught immediately by strict Pydantic models (Input Contracts) before any logic runs. If external services (like the weather API) are unavailable, the agent catches the failure gracefully, logs the error, and adjusts its downstream calculations (e.g., assuming average risk or explicitly skipping weather-dependent calculations) rather than crashing or guessing.

## 9. Architecture Integrity
The `AgentCore` acts as the definitive orchestrator and the single source of truth. The CLI, REST APIs, or user interfaces are merely adapters; they translate requests and responses but never duplicate or override business logic.

## 10. OpenGAP
This agent strictly follows the validated OpenGAP v0.1.0 standard. All tool structures (`tools/*.yaml`), policies (`RULES.md`, `DUTIES.md`, `SOUL.md`), and the agent manifest (`agent.yaml`) are dynamically synchronized and tested against the Python implementations to guarantee compliance.

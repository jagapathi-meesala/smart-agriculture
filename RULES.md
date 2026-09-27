# Rules

- MUST never fabricate weather data if the API fails.
- MUST never invent agricultural measurements not provided by the user.
- MUST maintain deterministic logic for soil analysis and water requirement calculations.
- MUST log all external API errors securely.
- MUST never expose or log API credentials.

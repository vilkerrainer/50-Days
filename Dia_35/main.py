# ================================================= #
# ---Uso de APIs externas (exemplo: API de clima)-- #
# Consuma uma API pública e exiba dados formatados. #
# ================================================= #

import openmeteo_requests
from openmeteo_sdk.Variable import Variable

def temp():
    om = openmeteo_requests.Client()
    params = {
        "latitude": -17.8575,
        "longitude": -41.5053,
        "hourly": ["temperature_2m"],
        "current": ["temperature_2m"]
    }

    responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
    response = responses[0]

    current = response.Current()
    current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
    current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))

    return f"{current_temperature_2m.Value():.0f}°C"

print(temp())

# ================================= #
# Para rodar: python -m Dia_35.main #
# ================================= #

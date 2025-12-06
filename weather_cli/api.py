import os
from typing import Any, Dict

import requests


def fetch_weather(city: str, api_key: str | None = None, units: str = "metric") -> Dict[str, Any]:
    """Fetch current weather for `city` from OpenWeather.

    Args:
        city: City name (e.g., "London" or "London,UK").
        api_key: OpenWeather API key. If None, read from `OPENWEATHER_API_KEY` env var.
        units: One of `metric`, `imperial`, or `standard`.

    Returns:
        Parsed JSON response as a dict.

    Raises:
        RuntimeError: if API key is missing.
        requests.HTTPError: for non-2xx responses.
    """
    if api_key is None:
        api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise RuntimeError("OpenWeather API key not found. Set OPENWEATHER_API_KEY in environment or .env file.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": units}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

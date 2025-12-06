import os
import sys
import json

import click
from dotenv import load_dotenv

from .api import fetch_weather


load_dotenv()


@click.command()
@click.argument("city", required=True)
@click.option("--units", "units", type=click.Choice(["metric", "imperial", "standard"]), default="metric", show_default=True)
@click.option("--raw", is_flag=True, help="Print raw JSON response")
def main(city: str, units: str, raw: bool) -> None:
    """Fetch and display current weather for CITY using OpenWeather API.

    Example: `python -m weather_cli.cli London` or `python -m weather_cli.cli "Seattle,US"`.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        click.echo("Error: OPENWEATHER_API_KEY not set. Create a .env file or set the environment variable.", err=True)
        sys.exit(2)

    try:
        data = fetch_weather(city, api_key=api_key, units=units)
    except Exception as exc:
        click.echo(f"Error fetching weather: {exc}", err=True)
        sys.exit(1)

    if raw:
        click.echo(json.dumps(data, indent=2))
        return

    name = data.get("name", city)
    weather = (data.get("weather") or [{}])[0]
    main = data.get("main", {})
    wind = data.get("wind", {})

    unit_label = "C" if units == "metric" else "F" if units == "imperial" else "K"
    speed_unit = "m/s" if units != "imperial" else "mph"

    click.echo(f"{name} — {weather.get('main','')} — {weather.get('description','').capitalize()}")
    click.echo(f"Temperature: {main.get('temp', 'N/A')}°{unit_label} (feels like {main.get('feels_like', 'N/A')}°)")
    click.echo(f"Humidity: {main.get('humidity', 'N/A')}%")
    click.echo(f"Wind: {wind.get('speed', 'N/A')} {speed_unit}")


if __name__ == "__main__":
    main()

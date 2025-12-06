# Weather-CLI-App

A simple Python command-line application that fetches real-time weather information for any city using the OpenWeather API. The app securely manages API keys using a `.env` file and is set up for practicing Git workflows (branches, commits, PRs).

**Quick features**
- Fetch current weather by city name
- Supports `metric`, `imperial`, and `standard` units
- Loads API key securely from `.env` using `python-dotenv`
- Simple formatted output or raw JSON

**Files added**
- `weather_cli/` — package containing `api.py`, `cli.py`, and `__main__.py`
- `.env.example` — example env file showing how to set `OPENWEATHER_API_KEY`
- `requirements.txt` — dependencies
- `.gitignore`

**Setup**

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your OpenWeather API key:

```powershell
copy .env.example .env
# then edit .env and replace the placeholder with your real key
```

**Usage**

Run the CLI (examples):

```powershell
python -m weather_cli.cli London
python -m weather_cli.cli "Seattle,US" --units imperial
python -m weather_cli.cli Tokyo --raw
```

You can also run via the module entrypoint:

```powershell
python -m weather_cli London
```

**Git workflow (practice)**

Create a feature branch, commit, push, and open a PR (example):

```powershell
git checkout -b feature/add-cli
git add .
git commit -m "Add weather CLI package and OpenWeather integration"
git push -u origin feature/add-cli
# Open a PR on GitHub from feature/add-cli into main
```

If you'd like, I can create the branch and commit these files for you.

Weather CLI App using OpenWeather API – A Python command-line application that fetches real-time weather information for any city using the OpenWeather API.

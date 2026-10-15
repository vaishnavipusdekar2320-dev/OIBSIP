# Task 3 — Basic Weather App

## Overview
A Python command-line application that asks for a city and displays current weather conditions, temperature, feels-like temperature, humidity, and wind speed. It uses the OpenWeatherMap Current Weather API.

## Requirements
- Python 3.8 or newer
- Internet connection
- An OpenWeatherMap API key
- The `requests` Python package

## Setup
1. Create an account at OpenWeatherMap and obtain an API key from its API keys section. New keys may take a little time to activate.
2. Open a terminal or command prompt in this folder.
3. Install the dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Set the API key as an environment variable. Do not paste your real API key into the code or upload it to GitHub.

   **Windows Command Prompt (for the current terminal window):**
   ```bat
   set OPENWEATHER_API_KEY=PASTE_YOUR_KEY_HERE
   ```

   **Windows PowerShell (for the current terminal window):**
   ```powershell
   $env:OPENWEATHER_API_KEY="PASTE_YOUR_KEY_HERE"
   ```

   **macOS/Linux:**
   ```bash
   export OPENWEATHER_API_KEY="PASTE_YOUR_KEY_HERE"
   ```

   Replace `PASTE_YOUR_KEY_HERE` with your own key. Keep the key private.

5. Run the app in the same terminal window:

   ```bash
   python weather_app.py
   ```

6. Enter a city name when prompted.

## Features
- Fetches current weather from an online API.
- Displays temperature in Celsius.
- Shows condition, feels-like temperature, humidity, and wind speed.
- Handles common errors such as an unknown city, missing/invalid API key, and connection problems.

## Example output
The values depend on the city and current weather:
```text
=== Basic Weather App ===
Enter city name: Pune

Weather for Pune, IN
------------------------------
Condition: Clear sky
Temperature: (live value) °C
Feels like: (live value) °C
Humidity: (live value)%
Wind speed: (live value) m/s
```

## Important security note
Never commit or share your API key in a public repository, screenshots, or the task submission form. The app reads the key from the `OPENWEATHER_API_KEY` environment variable instead.

## Files
- `weather_app.py` — application source code.
- `requirements.txt` — Python dependency list.

## What I learned
- Calling a web API using Python's `requests` library.
- Reading JSON responses.
- Using environment variables to keep API keys out of source code.
- Handling HTTP and connection errors.

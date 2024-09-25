# Show Weather

![Python](https://img.shields.io/badge/Python-3.9-blue) ![Django](https://img.shields.io/badge/Django-5.1.1-green) ![License MIT](https://img.shields.io/badge/License-MIT-yellow)

## Overview

**Show Weather** is a simple web application that allows you to check the weather in your city by integrating with [OpenWeather](https://openweathermap.org/).

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Step 1: Clone the Repository](#step-1-clone-the-repository)
  - [Step 2: Create a Virtual Environment](#step-2-create-a-virtual-environment)
  - [Step 3: Obtain an API Key](#step-3-obtain-an-api-key)
  - [Step 4: Configure the API Key](#step-4-configure-the-api-key)
  - [Step 5: Run the Server](#step-5-run-the-server)
- [Additional Information](#additional-information)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of [Python](https://www.python.org/downloads/).
- You have a [GitHub](https://github.com/) account.
- You have a basic understanding of Django.

## Installation

Follow these steps to set up and run the project locally.

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/viloker/Show-weather.git
```
### Step 2: Create a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd Show-weather
python -m venv venv
```
Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

### Step 3: Obtain an API Key

Register on [OpenWeather](https://openweathermap.org/) to obtain a free API key.

### Step 4: Configure the API Key

In the `main/api.py` file, replace the API value with the one you received from OpenWeather:
```bash
weather_api = 'YOUR_OPENWEATHER_API_KEY'
```
Replace 'YOUR_OPENWEATHER_API_KEY' with your actual API key.

### Step 5: Run the Server

In the terminal, execute the following command to start the Django development server:
```
bash python manage.py runserver
```
Open your web browser and navigate to http://localhost:8000 to view the application.

## Additional Information
Django Documentation: https://docs.djangoproject.com/
OpenWeather API Documentation: https://openweathermap.org/api

# Weather App with User Authentication and MySQL Integration

This is a weather app built using Python, Flask, and the OpenWeatherMap API. It also includes user authentication, allowing users to register, log in, and get weather updates for their city. User data is securely stored in a MySQL database.

## Features

- **Weather Information**: Fetches real-time weather data based on the city entered by the user using the OpenWeatherMap API.
- **User Authentication**: Allows users to register, log in, and log out. User information is stored securely in a MySQL database.
- **MySQL Database Integration**: User data (username, email, password) is stored and retrieved from a MySQL database.
- **Environment Configuration**: API key and database credentials are stored securely in a `.env` file.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
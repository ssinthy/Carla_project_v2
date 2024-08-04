import time

# Function to classify fog density based on fog density value
def get_fog_condition(weather):
    fog_density = weather.fog_density

    if fog_density == 0:
        return "No fog"
    elif 0 < fog_density <= 10:
        return "Very light fog"
    elif 10 < fog_density <= 30:
        return "Light fog"
    elif 30 < fog_density <= 50:
        return "Moderate fog"
    elif 50 < fog_density <= 70:
        return "Dense fog"
    else:
        return "Very dense fog"
    
# Function to get visibilty range based on fog distance value
def get_fog_visibility(weather):
    fog_distance = weather.fog_distance

    if fog_distance > 1000:
        return "Clear visibility"
    elif 500 < fog_distance <= 1000:
        return "Good visibility"
    elif 200 < fog_distance <= 500:
        return "Moderate visibility"
    elif 100 < fog_distance <= 200:
        return "Low visibility"
    else:
        return "Very low visibility"

def get_wind_force(weather):
    wind_intensity = weather.wind_intensity

    if wind_intensity == 0:
        return "No wind"
    elif 0 < wind_intensity <= 10:
        return "Light wind"
    elif 10 < wind_intensity <= 20:
        return "Light breeze"
    elif 20 < wind_intensity <= 30:
        return "Gentle breeze"
    elif 30 < wind_intensity <= 50:
        return "Moderate breeze"
    elif 50 < wind_intensity <= 70:
        return "Strong breeze"
    elif 70 < wind_intensity <= 90:
        return "High Wind"
    else:
        return "Storm"

def get_rain_status(weather):
    rain_intensity = weather.precipitation

    if rain_intensity == 0:
        return "No Rain"
    elif rain_intensity > 0 and rain_intensity <= 20:
        return "Light Rain"
    elif rain_intensity > 20 and rain_intensity <= 50:
        return "Moderate Rain"
    elif rain_intensity > 50 and rain_intensity <= 80:
        return "Heavy Rain"
    elif rain_intensity > 80:
        return "Violent Rain"
    else:
        return "Unknown"
    
def get_cloud_condition(weather):
    # Get the cloudiness value
    cloudiness = weather.cloudiness

    if cloudiness < 10:
        return "Sky clear"
    elif 10 <= cloudiness < 25:
        return "Few clouds"
    elif 25 <= cloudiness < 50:
        return "Scattered clouds"
    elif 50 <= cloudiness < 75:
        return "Broken clouds"
    else:
        return "Overcast"

def get_time_of_day(weather):
    sun_altitude_angle = weather.sun_altitude_angle

    # Infer the time of day from the sun altitude angle
    if sun_altitude_angle > 70:
        return "Noon"
    elif 10 <= sun_altitude_angle <= 70:
        return "Morning"
    elif -10 <= sun_altitude_angle < 10:
        return "Evening"
    else:
        return "Night"
    
def set_environmental_condition(world, weather, cloudiness, precipitation, sun_altitude_angle, wind_intensity, fog_density, fog_distance):
    weather.cloudiness = cloudiness  # Ensure it's cloudy when it rains
    weather.precipitation = precipitation
    weather.precipitation_deposits = precipitation  # Set wetness based on rain intensity
    weather.wetness = precipitation  # Reflect the rain on the road
    weather.sun_altitude_angle = sun_altitude_angle
    weather.wind_intensity = wind_intensity
    weather.fog_density = fog_density
    weather.fog_distance = fog_distance

    world.set_weather(weather)
    time.sleep(2)  # Allow some time for the environment to update

def set_up_environment(world, weather):

    set_environmental_condition(world, weather, cloudiness = 30, precipitation = 80, sun_altitude_angle = 30, 
                                wind_intensity = 30, fog_density = 30, fog_distance = 30)
    time.sleep(5)

    # Get day of time information
    time_of_day = get_time_of_day(weather)

    # Get rain status
    rain_status = get_rain_status(weather)
    
    # Get fog condition
    fog_condition = get_fog_condition(weather)
    
    # Get fog visibility
    fog_visibility = get_fog_visibility(weather)
    
    # Get wind force
    wind_force = get_wind_force(weather)
    
    # Get cloud condition
    cloud_condition = get_cloud_condition(weather)

    return time_of_day, rain_status, fog_condition, fog_visibility, wind_force, cloud_condition
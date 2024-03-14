pm25 = float(input("PM2.5: "))

if 12 >= pm25 >= 0:
    print("AQI: Good")
elif 35.5 > pm25 > 12:
    print("AQI: Moderate")
elif 55.5 > pm25 >= 35.5 :
    print("AQI: Unhealthy for Sensitive Groups")
elif 150.5 > pm25 >= 55.5:
    print("AQI: Unhealthy")
elif 250.5 > pm25 >= 150.5:
    print("AQI: Very Unhealthy")
elif 350.5 > pm25 >= 250.5:
    print("AQI: Hazardous")
elif 500 >= pm25 >= 350.5:
    print("AQI: Hazardous")
else:
    print("Invalid PM2.5 level. Please enter a valid value.")

# Output
# Interaction example
# Outcome when inputting the level of PM2.5 as 11
# PM2.5: 11
# AQI: Good
# Outcome when inputting the level of PM2.5 as 35
# PM2.5: 35
# AQI: Moderate
# Outcome when inputting the level of PM2.5 as 50
# PM2.5: 50
# AQI: Unhealthy for Sensitive Groups
# Outcome when inputting the level of PM2.5 as 60
# PM2.5: 60
# AQI: Unhealthy
# Outcome when inputting the level of PM2.5 as 250
# PM2.5: 250
# AQI: Very Unhealthy
# Outcome when inputting the level of PM2.5 as 300
# PM2.5: 300
# AQI: Hazardous
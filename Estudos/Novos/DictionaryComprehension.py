# Dicionary comprehension

# Dicionary = {key: expression for (key, value) in iterable}
# Dicionary = {key: expression for (key, value) in iterable if conditional}
# Dicionary = {key:(if/else) for (key, value) in iterable}
# Dicionary = {key:function(value) for (key, value) in iterable}
#--------------------------------------------------------------------------

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#citties_in_C = {key: round(((value-32)*5/9)) for (key, value) in cities_in_F.items()}
#print(citties_in_C)

#--------------------------------------------------------------------------

#weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
#weather_in_sunny = {key: value for (key, value) in weather.items() if value == 'sunny'}
#print(weather_in_sunny)

#--------------------------------------------------------------------------

#cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#desc_citties = {key: ('WARM' if value >= 40 else "COLD") for (key, value) in cities.items()}
#print(desc_citties)

#--------------------------------------------------------------------------

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69>= value >=40:
        return "WARM"
    else:
        return "COLD"
        


cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_citties = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_citties)
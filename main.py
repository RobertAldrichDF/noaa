from noaa_sdk import noaa

n = noaa.NOAA()
observations = n.get_observations('49616','US')
for observation in observations:
    print(observation)
    break
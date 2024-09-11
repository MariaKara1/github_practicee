print("Welcome to the Space Travel Calculator!")
distance = float(input("What's the distance to the celestial object (in light-years)? \n \n"))
speed = float(input("What's the speed of the spacecraft (in a fraction of the speed of light)? \n \n"))
time = distance/speed
print(f"It would take: {time} years to reach your destination!")
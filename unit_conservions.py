# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Cade Hart
#               Ben Moran
#               Matthew Sterniuk
#               Andrew Himebrook
# Section: ENGR 102-216
# Assignment: Lab 3.20
# Date: 4 September 2025

#Gets the respective positions and times
time1 = float(input("Enter time 1: "))
x1 = float(input("\nEnter the x position of the object at time 1: "))
y1 = float(input("\nEnter the y position of the object at time 1: "))
z1 = float(input("\nEnter the z position of the object at time 1: "))
time2 = float(input("\nEnter time 2: "))
x2 = float(input("\nEnter the x position of the object at time 2: "))
y2 = float(input("\nEnter the y position of the object at time 2: "))
z2 = float(input("\nEnter the z position of the object at time 2: "))

#Gets the slope for each of the dimensions and the increment between the time values
xslope = (x2 - x1) / (time2 - time1)
yslope = (y2 - y1) / ( time2 - time1)
zslope = (z2 - z1) / (time2 - time1)
increment = (time2 - time1) / 4

#Prints the position of the object in form (x,y,z) for each of the increments between time 1 and time 2
print(f"\n\nAt time {time1:.2f} seconds the object is at ({x1:.3f},{y1:.3f},{z1:.3f})")
print(f"At time {time1+increment:.2f} seconds the object is at ({xslope*(increment)+x1:.3f},{yslope*(increment)+y1:.3f},{zslope*(increment)+z1:.3f})")
print(f"At time {time1+increment*2:.2f} seconds the object is at ({xslope*(increment*2)+x1:.3f},{yslope*(increment*2)+y1:.3f},{zslope*(increment*2)+z1:.3f})")
print(f"At time {time1+increment*3:.2f} seconds the object is at ({xslope*(increment*3)+x1:.3f},{yslope*(increment*3)+y1:.3f},{zslope*(increment*3)+z1:.3f})")
print(f"At time {time2:.2f} seconds the object is at ({xslope*(increment*4)+x1:.3f},{yslope*(increment*4)+y1:.3f},{zslope*(increment*4)+z1:.3f})")

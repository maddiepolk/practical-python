# bounce.py
#
# Exercise 1.5
 
# A rubber ball is dropped from a height of 100 meters and each time it hits the ground, 
# it bounces back up to 3/5 the height it fell. 
# Write a program bounce.py that prints a table showing the height of the first 10 bounces.

h = 100
x = 0
while x < 10:
    h *= (3/5)
    x += 1
    print(x, round(h, 4))

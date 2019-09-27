"""WRONG! - Pythagorean Theorem with Decimal Degrees - WRONG!"""
import math
x1 = -90.212452861859035
y1 = 32.316272202663704
x2 = -88.952170968942525
y2 = 30.438559624660321
x_dist = x1 - x2
y_dist = y1 - y2
dist_sq = x_dist**2 + y_dist**2
dist_deg = math.sqrt(dist_sq)
print(dist_deg * 6371)

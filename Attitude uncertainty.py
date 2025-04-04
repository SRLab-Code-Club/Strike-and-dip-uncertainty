# Created by Yun-Pin Chen. March, 2025
# Reference: Cronin, V. S. (2008). Finding the mean and 95 percent confidence interval of a set of strike-and-dip or lineation data. Environmental & Engineering Geoscience, 14(2), 113-119.

# start
import numpy as np

#recognize csv file
filename = str()+".csv"

#read csv file
# 1st column is strike, 2nd column is dip, no title
strike = np.loadtxt(filename, delimiter=",", usecols=0, dtype=int)
#print(strike)
dip = np.loadtxt(filename, delimiter=",", usecols=1, dtype=int)
#print(dip)

# tested data from Cronin(2008)
#strike = np.array([310, 319, 322])
#dip = np.array([38, 45, 30])

# define N
number = 0
for i in strike:
    number += 1
print("Number of attitudes =", number)

# define P. For 95 percent confidence interval, P = 0.05
P = 0.05
print("Probability = ", P)

# calculate trend, which is (strike + 90) or dip direction
trend = strike + 90

# transform trend and dip from degrees to radians
trend = np.radians(trend)
dip = np.radians(dip)

# calculate plane vector, l is northing, m is easting, d is downward
l = np.cos(trend) * np.cos(dip)
m = np.sin(trend) * np.cos(dip)
n = np.sin(dip)

# calculate mean dip vector
l_mean = np.sum(l)
m_mean = np.sum(m)
n_mean = np.sum(n)
#print("mean l=", l_mean)
#print("mean m=", m_mean)
#print("mean n=", n_mean)

# calculate the length of the mean dip vector（R）
vector_length = np.sqrt(l_mean**2 + m_mean**2 + n_mean**2)
#print("Mean vector length =", vector_length)

# calculate the unit vector of the mean dip vector
unit_vector_l = l_mean/vector_length
unit_vector_m = m_mean/vector_length
unit_vector_n = n_mean/vector_length
#print("Unit vector l =", unit_vector_l)
#print("Unit vector m =", unit_vector_m)
#print("Unit vector n =", unit_vector_n)

# calculate mean dip
mean_dip = np.arcsin((unit_vector_n))
mean_dip = np.degrees(mean_dip)

# calculate mean strike
mean_trend=np.arccos(unit_vector_l/(np.cos(np.arcsin(unit_vector_n))))
mean_trend=np.degrees(mean_trend)
if unit_vector_m<0:
    mean_trend=360-mean_trend
mean_strike=mean_trend-90
if mean_strike<0:
    mean_strike=360+mean_strike

# calculate 95 percent confidence interval of dip
alpha95 = np.arccos(1-(((number-vector_length)/vector_length)*((1/P)**(1/((number)-1))-1)))
alpha95 = np.degrees(alpha95)

# calculate 95 percent confidence interval of strike
theta = np.arcsin((np.sin(np.radians(alpha95))*np.sin(np.radians(mean_dip)))/(np.cos(np.radians(alpha95))*np.cos(np.radians(mean_dip))))
beta=np.arctan((np.sin(np.radians(alpha95))*np.cos(theta))/((np.cos(np.radians(alpha95))*np.cos(np.radians(mean_dip)))-(np.sin(np.radians(alpha95))*np.sin(theta)*np.sin(np.radians(mean_dip)))))
beta=np.degrees(beta)

# print results
print("Mean strike = ", mean_strike)
print("Mean dip=", (mean_dip))
print("95% CI of strike = ", beta)
print("95% CI of dip =", alpha95)


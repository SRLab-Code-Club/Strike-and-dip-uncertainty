# Strike-and-Dip-Uncertainty
Calculate the mean value and 95 percent confidence interval for a given strike and dip dataset

# Introduction
Given a set of plane attitudes (strike/dip, right-hand rule), the mean value and the 95% confidence level can be calculated.

# How to use it?
1. Save the attitude data into a CSV file. The first column is strike, and the second column is dip. No header.
2. Open the python file (Attitude uncertainty.py)
3. Input the path of the CSV file (without filename extension) in row 8
4. Run the code and the reults will be printed

# What is the meaning of the printed data?
1. Number of attitudes: just what that means
2. Probability: for 95 percent confidence interval, the value of Probability should be 0.05
3. Mean strike: the strike angle (right-hand rule) of the mean attitude
4. Mean dip: the dip angle (right-hand rule)of the mean attitude
5. 95% CI of strike: 95 percent confidence interval of strike for the given dataset
6. 95% CI of dip: 95 percent confidence interval of dip for the given dataset

# It should be noted that...
1. Collect more than 7 attitude measurements for a given structure with approximately the same orientation
2. The uncertainty in "attitude measuring" is not considered
3. The following paper should be read to ensure you understand how this code works (you may not find this paper on the internet, so I am providing the PDF file: cronin2008.pdf)

# For more (mathematical) information, you can refer to...
Cronin, V. S. (2008). Finding the mean and 95 percent confidence interval of a set of strike-and-dip or lineation data. Environmental & Engineering Geoscience, 14(2), 113-119.

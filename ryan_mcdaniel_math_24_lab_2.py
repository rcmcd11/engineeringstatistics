# -*- coding: utf-8 -*-
"""Ryan McDaniel Math 24 Lab 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144BR3LcFujF_V4az6F2iz1Sj5Uq72ekR
"""

import numpy as np #libraries
import matplotlib.pyplot as plt

numbers= np.array([1,2,2,3,3,3,4,4,4,4]) #make an array with these numbers

plt.hist(numbers,100); #plot a histogram of the array

"""# PRNG"""

x = 0.12345

x = x*3

x % 1





current_point = 0.12345          # seed value
points_to_save = np.zeros(50000,)  # initialize an array of zeros of size 50,000

for i in range(points_to_save.shape[0]):
    current_point = 3*current_point % 1      # update x and store the value in points_to_save,
    points_to_save[i] = current_point

plt.plot(points_to_save, '.')     # plot the values in X

plt.hist(points_to_save);  #plot a histogram of the x values, this is a uniform distribution

def coin():
    return 2*(np.random.random() > 0.5) - 1 #"True" value defaults to 1, "False" to zero.  Multiplying by two and subtracting one makes a false value into a -1 and a true value into a +1

coin() #test the function

x = 0 #x is our starting point
x + coin() #move x to the right one for a success and left one for a failure

x = 0

for i in range(3): # do the same as above three times in a row
    x = x + coin()

x

x = 0

for i in range(100): #now lets do it 100 times, and we end very near our starting point
    x = x + coin()

x #final x is near our initial value of x

M = 10000 #M is our matrix size
N = 100 #N is the number of times we flip our coin

X = np.zeros(M,)

for j in range(M):

    x = 0

    for i in range(N):
        x = x + coin()

    X[j] = x

plt.hist(X); #by doing the same operation 100 times on 10000 values, we get a normal distribution



"""# Bonus: Explain Pascal's Triangle"""

P = np.zeros((12,18))

P[0,5]=1

for i in range(1,P.shape[0]):

    for j in range(1,P.shape[1]-1):

        P[i,j] = P[i-1,j-1]+P[i-1,j]

print(P[:,5:])

"""# Normal Distribution"""

# Define the parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 0.1  # Standard deviation (sigma) of the distribution

# Generate 1000 data points following a normal distribution with the specified mean and standard deviation
sample_size = 10000
data_points = np.random.normal(mean, std_dev, sample_size)

# Plot the histogram of the data points
bins_number = 30  # Number of bins for the histogram
hist_count, x, ignored = plt.hist(data_points, bins_number, density=True)

x = np.linspace(-15,15,1000) #define x as 1000 points between -15 and 15

y = np.exp(-x**2) #this is the equation for a standard normal curve

plt.plot(x,y)

y2 = np.sin(10*x) #this is the equation of a sin wave

plt.plot(x,y2) #graph it

plt.plot(x,y*y2) #this is the equation of the normal curve multiplied by the sin wave

y3 =  np.exp(- (x - 0) ** 2 ) #again the normal distribution equation
plt.plot(x, y3, linewidth=2, color='r')

# Define the parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 0.1  # Standard deviation (sigma) of the distribution

# Generate 1000 data points following a normal distribution with the specified mean and standard deviation
sample_size = 10000
data_points = np.random.normal(mean, std_dev, sample_size)

# Plot the histogram of the data points
bins_number = 30  # Number of bins for the histogram
hist_count, x, ignored = plt.hist(data_points, bins_number, density=True)

# Plot the probability density function of the normal distribution
normal_dist_curve = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std_dev ** 2))
plt.plot(x, normal_dist_curve, linewidth=2, color='r')

# Set the title and labels for the plot
plt.title('Normal Distribution Visualization')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Display the plot
plt.show()



x = np.array([1,2,3,4])

np.sum(x) #you can sum the values of an array

x.shape[0] #this gives the size of the first dimenstion of the array

np.sum(x)/x.shape[0] #sum over number of values gives mean

def mean(x):
    return np.sum(x)/x.shape[0] #now we make a function to get the mean of an array

mean(x) #use it

x #our x values

x - mean(x)

(x - mean(x))**2 #we start building a variance equation

def var(x):
  return mean((x - mean(x))**2) #this gives us our variance equation

def std(x):
  return np.sqrt(var(x)) #stdv is just the square root of variance

mean(x) #now we have three working functions for our distributions

var(x) #run variance

std(x) #run stdv



"""### Uniform Random Numbers"""

X = np.random.random(500000,) #make a one dimensional array with 500000 uniformly distributed random numbers

X

plt.hist(X,100); #histogram of these random numbers

np.random.random() #uniform distribution random number between 0 and 1

r = np.random.random()

r

r = np.random.randint(1,10) #random integer between 1 and 9

r

np.random.randn() #generates a normally distributed random number centered on zero

numbers  = np.random.randn(2,4) #creates a matrix with two rows and four columns

numbers.shape



numbers = numbers.reshape(-1) #reshapes the array into a flat matrix, the .reshape() function takes arguments in the form of array dimensions.  You can reshape an array into an array with any number of dimensions

numbers.shape #shape of the flattened matrix

numbers= np.array([1,2,2,3,3,3,4,4,4,4])

plt.hist(numbers,100); #same histogram as before

numbers = np.random.randn(100000,) #generate a matrix with 100k normally distributed numbers centered on zero
plt.hist(numbers,100); #plot a histogram with 100 bins of this matrix

numbers = np.random.rand(1000000,) #uniformly distributed numbers between 0 and 1, 100k of them
plt.hist(numbers,100); #histogram with 100 bins

np.random.seed(12345) #sets the seed for all the random number generators so that we can reproduce the same results with the same seed
data = np.random.randn(2, 100) #normally distributed matrix with two rows and 100 columns

plt.figure(1, figsize=(14, 14)) #sets the size of each figure that matplotlib will plot

plt.subplot(2,2,1) #the matrix to print the subplot on, (split the figure into two columns and rows and print this figure in the first quadrant)
plt.hist(data[0]) #histogram of our normal matrix

plt.subplot(2,2,2)
plt.scatter(data[0], data[1]) #scatterplot of the matrix, using the first row as the x value and the second row as the y value

plt.subplot(2,2,3)
plt.plot(data[0], data[1],'-') #plot a line of all the points, first row x, second row y, this is good if order matters

plt.subplot(2,2,4)
plt.hist2d(data[0], data[1]) #this is a 2d histogram which uses colors to map elevation of the histogram

plt.show() #show the plot

"""Normal Dist Data"""

x = 10*np.random.randn(10000) #generate rand matrix one dimensional normal distribution with 10000 values

plt.hist(x); #plot a histogram of the matrix

x = np.random.rand(1000,) #generate rand matrix one dimensional uniform distribution with 1000 values

plt.hist(x); #plot a histogram of it



mu = 0  # mean of distribution
sigma = 1  # standard deviation of distribution
x = mu + sigma * np.random.randn(10000) #this is standardizing a normal distribution. (multiply by the standard deviation then add the mean)

n,bins,patches = plt.hist(x,bins=100) #n is matrix containing the number of values in each bin.  bins is a matrix containing the endpoints of each bin.  patches is the rectangles from which the histogram is created

bins

n

patches

y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(y) # this is the probability density function of our normal curve

num_bins = 50
n,bins,patches = plt.hist(x, num_bins, density=1)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
plt.plot(bins,y) #plot histogram with probability density curve over top of it



x

def mean(x): #make a function to determine the mean of any first dimension of an array
    return np.sum(x)/x.shape[0]

def var(x): #variance function of an array
    return mean((x - mean(x))**2)

def std(x): #standard deviation in an array
    return np.sqrt(var(x))

def median(x): #function to find the median
    n = len(x) #save the length of the matrix as n
    sorted_x = np.sort(x) #save your matrix in ascending order as a new matrix
    mid = n // 2 # find the midpoint of your matrix
    if n % 2 == 0: #if the midpoint is even, take your midpoint value and your midpoint + 1 value and average them
        return (sorted_x[mid - 1] + sorted_x[mid]) / 2
    else: #if the midpoint is odd return the midpoint value
        return sorted_x[mid]

def mode(x): #function to find the mode
    values, counts = np.unique(x, return_counts=True) #make two matrices that consist of the unique values in the input matrix and a corresponding matrix containing the amount of times each value appears in the matrix
    max_count_index = np.argmax(counts) #find the index where the max of the times any value appears exists on the values matrix
    return values[max_count_index] #return the unique number in values which is indexed at the max of the counts matrix

def range(x): #function to find range
    return np.max(x) - np.min(x) #find the max of x and the min of x and take the difference of them to find range

data = np.array([1, 2, 2, 3, 4, 5, 5, 5, 6])

# Testing the functions
mean_value = mean(data)
var_value = var(data)
std_value = std(data)
median_value = median(data)
mode_value = mode(data)
range_value = range(data)

mean_value, var_value, std_value, median_value, mode_value, range_value



"""# Homework



"""



"""# Pi from Random Numbers"""

N = 10 #the amount of points we want in our random matrix

points = -1 + 2*np.random.random((N,2)) #make a random 2d matrix, and change the possible values to be max 1 and min -1 in both dimensions

points

plt.plot(points[:,0],points[:,1],'.') #plot first dimension by second dimension of matrix in dots

plt.gca().set_aspect(1) #sets the aspect ratio of the axes so that they appear as 1:1

inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1 #use the formula for a circle to check if a point falls within the circle or not
outside_circle = points[:,0]**2 + points[:,1]**2  > 1

plt.plot(points[inside_circle,0],points[inside_circle,1],'g.') #set the dots to be green if they fall inside the circle and red outside
plt.plot(points[outside_circle,0],points[outside_circle,1],'r.')


plt.gca().set_aspect(1)

np.sum(inside_circle),np.sum(outside_circle) #sum the amount of dots that appear within the circle and outside the circle

total_area = 4 #the area of the square containing the circle

fraction_inside = np.sum(inside_circle)/N #find the percentage of the numbers within the circle out of all data points

fraction_inside*total_area #take the percentage of the total area that the points within the circle occupy, the more points the more accurate

N = 100000000 #wayyyyyy more points so we can approximate pi
points = -1 + 2*np.random.random((N,2))
inside_circle  = points[:,0]**2 + points[:,1]**2  <=  1
fraction_inside = np.sum(inside_circle)/N
fraction_inside*4

"""# Complete Code for Estimating π using Monte Carlo Simulation"""

# Number of random points to generate
num_points = 10000

# Generating random points
x_points = np.random.uniform(-1, 1, num_points) #generate your random numbers between -1 and 1 for your x values, we need x values uniformly distributed equal to the number of points we want
y_points = np.random.uniform(-1, 1, num_points) #same thing except y values, we need the same length matrix and uniform dist

# Calculating the number of points inside the quarter circle
points_inside = np.sqrt(x_points**2 + y_points**2) <= 1 #use the formula for the graph of a circle to return True into our matrix if the point is within the circle, and False if not
num_inside = np.sum(points_inside) #since trues count as one and falses as zero the sum of this matrix will be the number of points within the circle

# Estimating π
pi_estimate = 4 * num_inside / num_points #4 is the area of the square where the points are generated and num_inside/num_points is the percentage of points within the circle
#this gives the percent of the area in the circle which should be our pi estimate because pi r squared = pi for a circle with radius one

# Plotting the points and the quarter circle
plt.figure(figsize=(6, 6)) #make the whole figure 6 by 6 inches
plt.scatter(x_points[points_inside], y_points[points_inside], color='green', label='Inside') #plot the points inside the circle as a scatter plot
plt.scatter(x_points[~points_inside], y_points[~points_inside], color='red', label='Outside') #plot the points outside as another scatter plot with red as the color
circle = plt.Circle((0, 0), 1, color='blue', fill=False) #make a variable to save the parameters of our circle we want to plot.  centered at 0,0 with radius 1, color blue, and just outlined
plt.gca().add_artist(circle) #plot the circle as an artist on the current axes
plt.title('Estimating π using Monte Carlo Simulation') #title the graph
plt.xlabel('x') #label x
plt.ylabel('y') #label y
plt.legend() #show the legend
plt.axis('equal') #makes the ratio of the axes equal to one another
plt.show() #shows the plot

pi_estimate #prints our pi estimate beneath the plot



"""# e from Random Numbers"""

X = np.random.random((1000000,10)) #make a uniformly distributed randomly generated matrix with 10 dimensions

Y = np.cumsum(X,1) #the Y matrix is the cumulative sum across the first dimension of the matrix (adding horizontally and keeping the values)

Y

Z = np.argmax(Y > 1,1) + 1 #returns the index of the first value of Y that is greater than 1, and adds 1 to the index to make it one based, not zero based.
Z

np.mean(Z) #The mean of these values should give us an approximation of Euler's number

np.mean(np.argmax(np.cumsum(np.random.random((10000000,10)),1) > 1,1) + 1) #Done all in one line

np.exp(1) #The value of Euler's number pulled from Numerical Python

"""# Further Reading:

### Quantum Random Numbers API

https://aws.amazon.com/marketplace/pp/prodview-246kyrfjo3bag
"""
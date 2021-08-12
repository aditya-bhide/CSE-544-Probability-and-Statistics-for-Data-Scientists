###### Question 3a ######
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(0)

print("Give input numbers. (Input q to stop)")
nums = []
while True:
    num = input()
    if num == "q" or num =="Q":
        break
    else:
        nums.append(int(num))

# nums = [1,1,1,2,2,3,3,4,4,4,5,5,5,5,5,5]
print("Answer for question 3 a: ")

def draw_step(nums):
    count = {}
    for i in range(1,len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] +=1
    x = []
    y = []
    for i in count:
        x.append(i)
    x.sort()

    step = 0
    for i in x:
        step += count[i]
        y.append(step/len(nums))

    plt.step(x, y)
    t = "eCDF for size " + str(len(nums))
    plt.title(t) 
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.step(x, y, label="eCDF")
    plt.legend(loc="upper left")
    x_coordinates = x
    y_coordinates = [0 for i in range(len(x))] 
    plt.scatter(x_coordinates, y_coordinates, marker="X")
    plt.show()
draw_step(nums)

####### Question 3b #######
print("Answer for question 3 b: ")
nums1 = np.random.randint(low=1, high=99, size=10)
nums2 = np.random.randint(low=1, high=99, size=100)
nums3 = np.random.randint(low=1, high=99, size=1000)
draw_step(nums1)
draw_step(nums2)
draw_step(nums3)

##### Question 3c #####
print("Answer for question 3 c:")

length = int(input("Size of sample: "))
size = int(input("Total number of samples: "))
maximum = 0
minimum = 100000

nums_arr = np.zeros((size,length))
for i in range(size):
    for j in range(length):
        nums_arr[i][j] = int(input())
    minimum = min(minimum, nums_arr[i].min())
    maximum = max(maximum, nums_arr[i].max())
print(nums_arr)

# nums_arr = np.array([[3,3,1,2,8],
#             [3,3,2,1,2],
#             [4,4,1,2,3]])

# for i in range(nums_arr.shape[0]):
#     minimum = min(minimum, nums_arr[i].min())
#     maximum = max(maximum, nums_arr[i].max())
#     print(minimum, maximum)

for i in range(0,nums_arr.shape[0]):
    nums_arr[i].sort()

counts_arr = []
for i in range(0,nums_arr.shape[0]):
    counts_arr.append({})
    for j in range(0, nums_arr.shape[1]):
        if nums_arr[i][j] not in counts_arr[i]:
            counts_arr[i][nums_arr[i][j]] = 1
        else:
            counts_arr[i][nums_arr[i][j]] +=1

sample_size = nums_arr.shape[1]
n = nums_arr.shape[0]
average_eCDF = []

cdf = 0
for i in range(int(minimum), int(maximum+1)):
    temp = 0
    for j in range(0, nums_arr.shape[0]):
        if i in counts_arr[j]:
            temp += counts_arr[j][i]/sample_size
    cdf += (temp/n)
    average_eCDF.append(cdf)

y = average_eCDF
x = [i for i in range(int(minimum), int(maximum+1))]

plt.step(x, y)
plt.title("eCDF") 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.step(x, y, label="eCDF")
plt.legend(loc="upper left")
x_coordinates = x
y_coordinates = [0 for i in range(len(x))] 
plt.scatter(x_coordinates, y_coordinates, marker="X")
plt.show()


####### Question 3d ######
print("Answer for question 3 d")
m_10 = np.random.randint(low=0, high=99, size=(10,10))

m_100 = np.random.randint(low=0, high=99, size=(10,100))

m_1000 = np.random.randint(low=0, high=99, size=(10,1000))

def calculate_avg_eCDF(nums_arr):
    for i in range(0,nums_arr.shape[0]):
        nums_arr[i].sort()

    counts_arr = []
    for i in range(0,nums_arr.shape[0]):
        counts_arr.append({})
        for j in range(0, nums_arr.shape[1]):
            if nums_arr[i][j] not in counts_arr[i]:
                counts_arr[i][nums_arr[i][j]] = 1
            else:
                counts_arr[i][nums_arr[i][j]] +=1

    sample_size = nums_arr.shape[1]
    n = nums_arr.shape[0]
    average_eCDF = []

    cdf = 0
    for i in range(0, 100):
        temp = 0
        for j in range(0,nums_arr.shape[0]):
            if i in counts_arr[j]:
                temp += counts_arr[j][i]/sample_size
        cdf += (temp/n)
        average_eCDF.append(cdf)

    y = average_eCDF
    x = [i for i in range(0,100)]
    plt.step(x, y)
    t = "eCDF for m = "+str(nums_arr.shape[1])
    plt.title(t) 
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.step(x, y, label="eCDF")
    plt.legend(loc="upper left")
    x_coordinates = x
    y_coordinates = [0 for i in range(len(x))] 
    plt.scatter(x_coordinates, y_coordinates, marker="X")
    plt.show()

calculate_avg_eCDF(m_10)
calculate_avg_eCDF(m_100)
calculate_avg_eCDF(m_1000)



######## Question 3e ########
print("Answer for question 3 e: ")
x = pd.read_csv("a3_q3.csv").to_numpy()
x = x.reshape(1,-1)[0]

def draw_ci_step(nums):
    count = {}
    for i in range(len(nums)):
        if i not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] +=1
    x = []
    y = []
    for i in count:
        x.append(i)
    x.sort()

    step = 0
    for i in x: 
        step += count[i]
        y.append(step/len(nums))
        
    lb = []
    ub = []
    
    n = len(y)
    for i in range(n):
        lb_value = y[i] - 1.96 * (np.sqrt((y[i] * (1 - y[i])) / n))
        ub_value = y[i] + 1.96 * (np.sqrt((y[i] * (1 - y[i])) / n))
        lb.append(lb_value)
        ub.append(ub_value)
    
    plt.step(x, lb, label="lower bound")
    plt.step(x, ub, label="upper bound")
    plt.step(x, y, label="eCDF")
    plt.legend(loc="upper left")
    plt.title("eCDF and Normal Based CI") 
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    x_coordinates = x
    y_coordinates = [0 for i in range(len(x))] 
    plt.show()
draw_ci_step(x)



######## Question 3f ########
print("Answer for question 3 f: ")
x = pd.read_csv("a3_q3.csv").to_numpy()
x = x.reshape(1,-1)[0]

def draw_dkw_ci_step(nums):
    count = {}
    for i in range(len(nums)):
        if i not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] +=1
    x = []
    y = []
    for i in count:
        x.append(i)
    x.sort()

    step = 0
    for i in x: 
        step += count[i]
        y.append(step/len(nums))
        
    lb = []
    ub = []
    
    n = len(y)
    for i in range(n):
        lb_value = y[i] - np.sqrt(((1/(2*n)) * np.log(2/0.05)))
        ub_value = y[i] + np.sqrt(((1/(2*n)) * np.log(2/0.05)))
        lb.append(lb_value)
        ub.append(ub_value)
    
    plt.step(x, lb, label="lower bound")
    plt.step(x, ub, label="upper bound")
    plt.step(x, y, label="eCDF")
    plt.legend(loc="upper left")
    plt.title("eCDF and DKW based CI") 
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    x_coordinates = x
    y_coordinates = [0 for i in range(len(x))] 
    plt.show()
draw_dkw_ci_step(x)
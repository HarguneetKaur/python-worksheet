import numpy as np

# ## question 1
# arr=np.arange(5,25)
# print(arr)
# A=np.random.randint(10,50, size=(3,4))
# print(A)

# ## question 2A
# arr=np.arange(5,25)
# print(arr)
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)

# ## question 2B
# A=np.random.randint(10,50, size=(3,4))
# print(A)
# print(A.shape)
# print(A.size)
# print(A.dtype)

# ## question 3A
# arr=np.array([2,4,6,8,10])
# arrr=np.array([1,3,5,7,9])
# print(arr)
# print(arrr)

# ## question 3B
# print(np.add(arr,arrr))
# print(np.subtract(arr,arrr))
# print(np.multiply(arr,arrr))
# print(np.divide(arr,arrr))

# ## question 4A
# arr=np.arange(1,10).reshape(3,3)
# print(arr)

# ## question 4B
# print(arr*5)

# ## question 5
# arr=np.arange(10,26).reshape(4,4)
# print(arr)

# A=arr[1,:]
# B=arr[:,3]
# print(A)
# print(B)

# arr=[0,:] = 0
# print("\n Array aftre replacing first row with zeros:",arr)

## question 6
# arr=np.random.randint(20,41, size=10)
# print(arr)

# greater_than_30 = arr[arr > 30]
# print(greater_than_30)

# ## question 7
# arr = np.arange(11, 23)
# print(arr)

# reshaped_arr= arr.reshape(3, 4)
# print(reshaped_arr)

# ## question 8
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# print(A)
# print(B)

# matrix_multiplication = np.dot(A, B)
# print(matrix_multiplication)

# transpose_A = A.T
# print(transpose_A)

# ## question 9
# arr = np.random.randint(10, 61, size=15)
# print(arr)

# mean_val = np.mean(arr)
# median_val = np.median(arr)
# std_dev = np.std(arr)

# print("Mean:", mean_val)
# print("Median:", median_val)
# print("Standard Deviation:", std_dev)

## question 10
A = np.array([[2, 1, 3],
              [0, 5, 6],
              [7, 8, 9]])

print(A)

det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("Inverse of A:\n", inv_A)
else:
    print("Inverse of A does not exist (det = 0)")

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

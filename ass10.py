
'''A company collects the monthly salaries (in 1,00,000 Rs.) of 12 employees. 
Reshape this 1D array into a 3x4 matrix, where each row represents a 
department, and each column represents employees in that department. 
Display the original and reshaped array along with their shapes. '''
'''import numpy as np
salaries=np.array([1,22,4,4,66,7,5,3,2,2,2,3])
print(salaries)
print(salaries.shape)
reshape=salaries.reshape(3,4)
print("reshape:")
print(reshape)
print(reshape.shape)'''
'''Accept an array of hospital bill amount paid by last 10 patients. Compute the 
total amount. Calculate the total monthly amount assuming these are weekly 
amounts.  '''
'''
import numpy as np
bill=np.array([33,4,5,6,6,6,6,6,6])
print(bill)
total=bill.sum()
print(total)
print("monthly amt")
month=total*4
print(month)
'''
''' Store the student’s marks in 6 subjects using NumPy array and generate the 
following:  
1.  Total Marks obtained 
2. Average marks  
3. Maximum marks '''
'''import numpy as np
marks=np.array([22,3,3,4,5,5])
print(marks)
total=marks.sum()
print("total",total)
av=marks.mean()
print("average",av)
ma=marks.max()
print("max",ma)'''
''' Perform the following operations on two arrays:  
1. Addition  
2. Multiplication 
3. Accept the number from user and add, multiply the array  
4. Find the square root of maximum number in each array'''
'''import numpy as np
array1=np.array([3,4,5,6,2,3])
array2=np.array([3,4,5,6,2,3])
newarray=array1+array2
print(newarray)
newarray=array1*array2
print(newarray)'''
'''import numpy as np
ar1=[]
arr2=[]
e1=int(input("how many elements want"))
for i in range(e1):
    n1=int(input("elemet"))
    n2=int(input("elemet"))
    ar1.append(n1)
    arr2.append(n2)
print(ar1)
print(arr2)
ar1=np.array(ar1)
arr2=np.array(arr2)
new=ar1+arr2
print(new)
mu=ar1*arr2
print(mu)
m1=ar1.max()
print(m1)
m2=arr2.max()
print(m2)
sq1=np.sqrt(m1)
print(sq1)
sq2=np.sqrt(m2)
print(sq2)
'''
'''Create a Pandas DataFrame with the following employee data and display it. 
Name Age Department 
Alice 
Bob 
25 
30 
IT 
HR 
Charlie 28 Finance 
Create the DataFrame using pandas. Print the DataFrame. Display the shape of the 
DataFrame.'''
'''import pandas as pd
data={'name':['alice','bob'],'age':['25','30'],'department':['it','hr']}
df=pd.DataFrame(data)
print(df)
print(df.shape)'''
'''Read data from a CSV file named "employees.csv".Display first 5 rows. '''

'''import pandas as pd
//check thisp
# Read the data from the CSV file
df = pd.read_csv("count.csv")

# Display the first 5 rows of the DataFrame
print(df.head())'''
'''Given student marks data in a Pandas DataFrame: 
Student Math  
Science 
Jignesh  85  
Emma 79  
Mamta 90  
Sunita 
88  
78  
85  
88  
92  
English 
92 
88 
76 
80 
Display students who scored more than 80 in Mathematics. Find students who 
scored more than 80 in both Mathematics and Science. '''
'''import pandas as pd
data = {
    'Student': ['Jignesh', 'Emma', 'Mamta', 'Sunita'],
    'Math': [85, 79, 90, 88],
    'Science': [92, 88, 76, 80]
}
df=pd.DataFrame(data)
print(df)
print(df[df['Math']>80])
print(df[(df['Math']>80)&(df['Science']>80)])
'''
'''A store sells three products, and their prices and tax rates. Create a dataframe 
with initial values considering three columns as product name, price and tax.  
Add new column in dataframe with name Final Price which is calculated as -    
Final Price=Price+(Price×Tax Rate) 
Display the updated dataframe.  '''
import pandas as pd

# Create a DataFrame with product names, prices, and tax rates
'''data = {
    'Product': ['Product A', 'Product B', 'Product C'],
    'Price': [100, 200, 150],
    'Tax Rate': [0.05, 0.10, 0.08]  # Tax rates as decimal values (5%, 10%, 8%)
}

# Create the DataFrame
df = pd.DataFrame(data)

# Calculate the Final Price and add it as a new column
df['Final Price'] = df['Price'] + (df['Price'] * df['Tax Rate'])

# Display the updated DataFrame
print(df)
'''
data = {
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Region': ['North', 'South', 'East', 'West', 'North'],
    'Sales': [2500, 1500, 3000, 1800, 2200]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame based on the 'Sales' column (without using `by`)
df_sorted = df.sort_values('Sales', ascending=True)

# Display the sorted DataFrame
print(df_sorted)

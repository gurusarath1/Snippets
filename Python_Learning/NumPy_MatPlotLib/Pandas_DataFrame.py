import pandas as pd

# Reading data from an external csv file
print('\n\n-- Import external data --')
employee_df = pd.read_csv('employeeDetails.csv')
print(employee_df)

print('\n\n-- Describe the data --')
print(employee_df.describe())

print('\n\n-- Creating data frames --')
data = {'Name':['Guru','Priyanka','Ramesh','Keerthi'], 'Age':[23,24,34,56]}
print( pd.DataFrame(data),'\n' )
print( pd.DataFrame(data, index=['First','Second', 'Third','Forth']) )


print('\n\n-- Creating data frames 2 --')
data = [['Tea',2],['Milk',1],['Coffee',3],['Rice',5],['Wheat',8],['Oats',10]]
print( pd.DataFrame(data),'\n' )
print( pd.DataFrame(data, columns = ['Item', 'Quantity'], dtype=float),'\n' )
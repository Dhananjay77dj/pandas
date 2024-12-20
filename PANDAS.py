import pandas as pd
import numpy as np 


dic = {
    "name":['dhananjay','elon musk','sam altman'],
    "salary":[809,8900,394,],
    "city":['silicon valley', 'texas', 'mexico'],
}
a = pd.DataFrame(dic) # this will creat a table like format 
row = a.iloc[1]
# print(type(row))
# print(a)
# a.to_csv('first.csv', index = False)

# print(a['name'])
r = pd.read_csv('third.csv' )
# print(r)
# r.index =['a','b','c']  FOR THE CHANGE OF INDEX NAME
# r.columns= [1,2,3]   FOR THE CHANGE OF COLUMN NAME !!
# print(r)
# a.head()
# print(a.head())

# CREATING  A SERIRES 

data = [10, 20, 30, 40, 50]
series = pd.Series(data)
# d = pd.Series(np.random.rand(34))
# print(d)
# print(np.random.rand(34,5)

newdf = pd.DataFrame(np.random.rand(334,5), index = np.arange(334))
newdf.columns = list('ABCDE')
# print(newdf)
# print(type(newdf))
# print(newdf.describe())
# print(newdf.index)
# print(newdf.head(5))  THIS WILL SHOW ME THE DATA OF FIRST 5 ROWS 

pd_ar = newdf.to_numpy()  # TO CONVERT A PANDAS DATAFRAM INTO A NUMPY !!
# print(pd_ar)l̥
# print(type(pd_ar))
# newdf.drop("C", axis=1, inplace=True)
 # THIS WILL RETURN A NEW DATAFRAME AND YOU HAVE TO STORE IT IN OTHER 
#VARIABLE  BASICALLY IT WILL DROP OR REMOVE A COLUMN OR ROW  
# newdf2 = newdf
# newdf2[0][0] = 452
print(newdf)
newdf.loc[0]['A']=45
print(newdf) 
print(newdf.loc[[0,1],['B','C']]) #this will give us the value of 0 and 1 th row form which
#      inside 0th and 1st row it will give 1st and 2nd column

# print(newdf.loc[(newdf[A]<.2)])
print(newdf.columns)
# newdf.drop('C',axis=1 , inplace = True)
print(newdf)

# print(newdf.loc[(newdf['A']<0.2)])
print(newdf.notnull())



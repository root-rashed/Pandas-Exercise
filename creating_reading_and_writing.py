import pandas as pd
df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
dff = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(df)
print(dff)



dfff = pd.Series([1, 2, 3, 4, 5])
print(dfff)


dffff = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(dffff)


dfffff= pd.DataFrame({'name':['rashed','raze'],'dep':['cse','ano']})
print(dfffff)
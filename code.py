import pandas as pd

"""
This algo imports a list of emails and returns the top 5
create empty list
for each email address split on @ delimter and keep index 1
on each iteration the domain is appended to the new list
upon completion the list is transformed into a new data frame
the final product is the top 5 count in the new data frame

"""

def popProv(email):
    newList = []
    for domain in email:
        newList.append(domain.split('@')[1])
    newDF=pd.DataFrame(newList)
    return newDF[0].value_counts().head(5)

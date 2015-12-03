import numpy as np
import pandas as pd

#Read the top 250 from IMDb from the clipboard
top250 = pd.read_clipboard()

#Drop columns with no useful information
top250.dropna(axis=1, inplace=True)
top250.columns = ['TitleYear','Rating']

#Fix the title, now it has the index, title and year together
theindex = [int(i.split('.',1)[0]) for i in top250.TitleYear]
thetitle_year = [i.split('.',1)[1].strip() for i in top250.TitleYear]
thetitle = [i.rsplit('(',1)[0].strip() for i in thetitle_year]
theyear = [int(i.rsplit('(',1)[1].rstrip(')')) for i in thetitle_year]

#Add title, year and position on the top 250 list
top250['Title'] = pd.Series(thetitle, index=top250.index)
top250['Year'] = pd.Series(theyear, index=top250.index)
top250['Nr'] = pd.Series(theindex, index=top250.index)

#Set position as the index for the DataFrame
top250.set_index('Nr', inplace=True)

#Drop the old title, the new one is much better
top250.drop('TitleYear', axis=1, inplace=True)

#Reorder the columns so that the rating is the last column.
cols = top250.columns
top250 = top250.reindex_axis(list(top250.columns[1:]) + ['Rating'], axis=1)


# Analysis
#Get all movies with 9.0 or above rating
top250[top250['Rating'] >= 9.0]

#Get the years with the most items on the top 250
top250.Year.value_counts()[:10]

#Get the year with the highest average rating, first collect, then sort
top250_stats = top250.groupby('Year').agg({'Rating':[np.size, np.mean]})
top250_stats.sort_values(by=[('Rating','mean')], ascending=False).head()

#Filter out years with at least 5 movies on the list
atleast_5 = top250_stats['Rating','size'] >= 5

#Show the average rating for these years
print(top250_stats[atleast_5].sort_values(by=[('Rating','mean')], ascending=False)[:10])


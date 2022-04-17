import pandas as pd
vacc_file_path = r'[...]\country_vaccination_stats.csv'
vacc = pd.read_csv(vacc_file_path)
mins = vacc.groupby(['country'])['daily_vaccinations'].transform('min')
vacc['daily_vaccinations'] = vacc['daily_vaccinations'].fillna(mins)
vacc['daily_vaccinations'] = vacc['daily_vaccinations'].fillna(0)
# ^we have filled the missing values with the minimum values as it's stated in the question
medians = vacc.groupby(['country'])['daily_vaccinations'].transform('median')
vacc['daily_vaccinations'] = medians
# ^we changed all the daily vaccinations values to the median of their groups
list1 = (vacc.sort_values('daily_vaccinations', ascending=False)).drop_duplicates(['country']).values.tolist()
# ^we sorted the dataset in order to descend from highest median value to the lowest
# ^we also deleted the duplicates to have one value from each country
final_list = []
for x in range(0,3):
    final_list.append(list1[x][0])
# ^adds top 3 countries to a new list, which is answer of the question
#print(final_list)
#when we test it, the return is ['United States', 'China', 'India'] which is correct
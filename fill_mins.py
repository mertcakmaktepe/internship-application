import pandas as pd
# file path can be changed below
vacc_file_path = r'[...]\country_vaccination_stats.csv'
vacc = pd.read_csv(vacc_file_path)
# code below makes a new series which groups the
# data by the countries and transforms all the daily vaccination values to
# the minimum of the specific group
mins = vacc.groupby(['country'])['daily_vaccinations'].transform('min')
# code below changes all the missing values in the original dataset
# with the values in the newly created series and also
# if it's still missing value which means the country has no values at all (like Kuwait)
# it changes it's value to 0
vacc['daily_vaccinations'] = vacc['daily_vaccinations'].fillna(mins)
vacc['daily_vaccinations'] = vacc['daily_vaccinations'].fillna(0)
# below we can test our code with the missing values in Argentina, Austria and Kuwait
# we got 6483, 3368 and 0 as return which are the minimum daily vaccination numbers of the mentioned countries
#print(vacc['daily_vaccinations'][0])
#print(vacc['daily_vaccinations'][28])
#print(vacc['daily_vaccinations'][750])
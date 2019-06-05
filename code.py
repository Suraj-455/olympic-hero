# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns = {'Total': 'Total_Medals'}, inplace=True)
print(data.head(10))


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'], 'Both', data['Better_Event'])
better_event = data['Better_Event'].value_counts().index.values[0]
print('Better Event=', better_event)


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries=top_countries[:-1]
# print(top_countries.head(5))
def top_ten(data, col):
    country_list = []
    country_list = list(data.nlargest(10, col)['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

top_10=top_ten(top_countries,'Total_Medals')
print("Top 10 Medals:\n",top_10, "\n")

common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
summer_df.groupby(['Country_Name', 'Total_Summer']).size().unstack().plot(kind='bar')
winter_df.groupby(['Country_Name', 'Total_Winter']).size().unstack().plot(kind='bar')
top_df.groupby(['Country_Name', 'Total_Medals']).size().unstack().plot(kind='bar')


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
maxSummer = summer_df[summer_df['Golden_Ratio']==summer_df['Golden_Ratio'].max()]
summer_max_ratio = float("{0:.2f}".format(maxSummer.iloc[0]['Golden_Ratio']))
summer_country_gold = maxSummer.iloc[0]['Country_Name']
#Code starts here
winter_df['Golden_Ratio'] = summer_df['Gold_Winter']/summer_df['Total_Winter']
maxWinter = winter_df[winter_df['Golden_Ratio']==winter_df['Golden_Ratio'].max()]
winter_max_ratio = float("{0:.2f}".format(maxWinter.iloc[0]['Golden_Ratio']))
winter_country_gold = maxWinter.iloc[0]['Country_Name']

#Code starts here
top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
maxTop = top_df[top_df['Golden_Ratio']==top_df['Golden_Ratio'].max()]
top_max_ratio = float("{0:.2f}".format(maxTop.iloc[0]['Golden_Ratio']))
top_country_gold = maxTop.iloc[0]['Country_Name']


# --------------
#Code starts here
data_1 = data[:-1]
data_1['Total_Points'] = data['Gold_Total']*3 + data['Silver_Total']*2 + data['Bronze_Total']*1
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']



# --------------
#Code starts here
best = data[(data['Country_Name'] == best_country)][['Gold_Total','Silver_Total','Bronze_Total']]
print(best)
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns
import requests
from datetime import datetime


pd.set_option('display.max_columns', None)


# define function to convert to hourly time 
def to_hour(time):
    try:
        hour = datetime.strptime(str(time), '%H:%M')
        return int(datetime.strftime(hour, '%H'))
    except Exception:
        return 0
#============IMPORT==============
csv_file_path = os.path.join('Resources', 'accidents_2014.csv')
traffic_df = pd.read_csv(csv_file_path)
#============DROP BLANK COLUMNS===========

traffic_df.dropna(
    axis=1,
    how='all',
    inplace=True
)

#============DROP BLANK ROWS WITH BLANK VALUES==========

traffic_df['Junction_Control'].replace(
    np.nan, 'None', inplace=True)

traffic_df.replace(
    '', np.nan, inplace=True)

traffic_df.replace(
    'Unknown', np.nan, inplace=True)

traffic_df.dropna(axis=0, inplace=True)

#===========REPLACING ERRANT/MISPELLED VALUES===============

traffic_df['Light_Conditions'].replace(
    'Darkeness: No street lighting',
    'Darkness: No street lighting', 
    inplace=True
)

traffic_df['Pedestrian_Crossing-Physical_Facilities'].replace(
    'non-junction pedestrian crossing',
    'Non-junction Pedestrian Crossing', 
    inplace=True
)

#===========RENAMING COLUMNS===============

traffic_df.rename(columns=
    {'Accident_Index' : 'Accident Index',
     'Longitude' : 'Longitude', 
     'Latitude' : 'Latitude', 
     'Police_Force' : 'Police Force', 
     'Accident_Severity' : 'Accident Severity', 
     'Number_of_Vehicles' : 'Number of Vehicles', 
     'Number_of_Casualties' : 'Number of Casualties', 
     'Date' : 'Date', 
     'Day_of_Week' : 'Day of Week', 
     'Time' : 'Time', 
     'Local_Authority_(District)' : 'Local Authority District', 
     'Local_Authority_(Highway)' : 'Local Authority Highway', 
     '1st_Road_Class' : '1st Road Class', 
     '1st_Road_Number' : '1st Road Number', 
     'Road_Type' : 'Road Type', 
     'Speed_limit' : 'Speed Limit', 
     'Junction_Control' : 'Junction Control', 
     '2nd_Road_Class' : '2nd Road Class', 
     '2nd_Road_Number' : '2nd Road Number', 
     'Pedestrian_Crossing-Human_Control' : 'Pedestrian Crossing Human Control', 
     'Pedestrian_Crossing-Physical_Facilities' : 'Pedestrian Crossing Physical Facilities', 
     'Light_Conditions' : 'Light Conditions', 
     'Weather_Conditions' : 'Weather Conditions', 
     'Road_Surface_Conditions' : 'Road Surface Conditions', 
     'Special_Conditions_at_Site' : 'Special Conditions at Site', 
     'Carriageway_Hazards' : 'Carriageway Hazards', 
     'Urban_or_Rural_Area' : 'Urban or Rural Area', 
     'Did_Police_Officer_Attend_Scene_of_Accident' : 'Police Attended Scene of Accident', 
     'LSOA_of_Accident_Location' : 'LSOA of Accident Location', 
     'Year' : 'Year', 
    }, inplace=True)

# format Date in Datetime format and add additional columns for month, day, and hour
traffic_df['Date'] = pd.to_datetime(traffic_df['Date'], format='%d/%m/%y')
traffic_df['Month'] = traffic_df['Date'].dt.month
traffic_df['Day'] = traffic_df['Date'].dt.day
traffic_df['Hour of Day'] = traffic_df['Time'].apply(to_hour)

# display cleaned file
traffic_df.head()
# set up data
trafficDataByMonth_df = traffic_df[['Date', 'Accident Index']].copy()
trafficDataByMonth_df.index = trafficDataByMonth_df['Date']
trafficDataByMonth_df = pd.DataFrame(trafficDataByMonth_df.resample('M').count()['Accident Index'])
trafficDataByMonth_df = trafficDataByMonth_df.reset_index()[['Date', 
                                                             'Accident Index']]
trafficDataByMonth_df.rename(columns={'Accident Index':'Accident Count'}, 
                             inplace=True )

# add length column to allow normalization by month lengths
trafficDataByMonth_df['Month Length (Num Days)'] = monthLength_list

# create bar plot
sns.set()
plt.rcParams['figure.figsize'] = [15,5]
plt.bar(trafficDataByMonth_df['Date'], 
        trafficDataByMonth_df['Accident Count']/trafficDataByMonth_df['Month Length (Num Days)'], 
        color=twelveColorPalette, width=15, align='center', linewidth=1, 
        edgecolor='black', tick_label=month_list, alpha=0.75)
plt.title("Normalized Accident Count by Month", size=16)
plt.xlabel("Month", size=13)
plt.ylabel("Normalized Accident Count", size=13)
plt.savefig('Images/normalizedAccidentByMonth.png')

# change date column to month names
trafficDataByMonth_df['Date'] = month_list

# display results
plt.show()
trafficDataByMonth_df
accSevByMonth_df = traffic_df[['Date', 'Accident Index', 'Accident Severity']].copy()
accSevByMonth_df.index = accSevByMonth_df['Date']
accSevByMonth_df['Month'] = accSevByMonth_df.index.month
accSevByMonth_df = pd.DataFrame(accSevByMonth_df.\
                                groupby(['Month', 'Accident Severity']).\
                                count()['Accident Index'])
accSevByMonth_df.reset_index(inplace=True)
accSevByMonth_df[['Month', 
                  'Accident Severity', 
                  'Accident Index']]
accSevByMonth_df.rename(columns={'Accident Index':'Accident Count'}, 
                        inplace=True)

# add month length for normalization
accSevByMonth_df['Month Length'] = tripleMonthLength_list

# normalize
accSevByMonth_df['Accident Count'] = accSevByMonth_df['Accident Count']/accSevByMonth_df['Month Length']

# create bar plot
accidentSeverityByMonth_plt = sns.barplot(x='Month', y='Accident Count', 
                                          data=accSevByMonth_df, 
                                          hue='Accident Severity', 
                                          palette=threeColorPalette, 
                                          edgecolor='black', alpha=0.75, 
                                          linewidth=1)
plt.title("Normalized Accident Severity by Month", size=16)
plt.ylabel("Normalized Accident Count")
plt.savefig('Images/normalizedAccidentSeverityByMonth.png')
plt.show(accidentSeverityByMonth_plt)
# Create dataframe for Casualties by Day of Week and Hour of Day
accidents_by_weeknum = traffic_df.groupby(['Day of Week']).sum()['Number of Casualties'].to_frame().reset_index()
accidents_by_date = traffic_df.groupby(['Date', 
                                        'Day of Week', 
                                        'Month']).sum()['Number of Casualties'].to_frame().reset_index()
accidents_by_hour = traffic_df.groupby(['Day of Week',
                                        'Hour of Day']).sum()['Number of Casualties'].to_frame().reset_index()
accidents_by_hour_pivot = accidents_by_hour.pivot_table(values=['Number of Casualties'], 
                                                        index=['Hour of Day'], 
                                                        columns=['Day of Week'])
accidents_by_hour_pivot.columns = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

# Plot bars for Number of Casualties by Day of Week
plt.figure(figsize=(10,6))
sns.set_style('darkgrid')
b = sns.barplot(x='Day of Week', y='Number of Casualties', data=accidents_by_weeknum,
                palette=sevenColorPalette, linewidth=1, edgecolor='black')

# Define x_axis for xticks
x_axis = np.arange(0,7,1)

# Calculate upper bound of y-axis
y_max = max(accidents_by_weeknum['Number of Casualties'])
# round the upper bound of y-axis up to nearest thousand
y_max -= y_max % -1000
step = 1000
y_axis = np.arange(2000, y_max+step, step)
# format y-ticks as comma separated
y_axis_fmt = ["{:,.0f}".format(y) for y in y_axis]
# set y-axis limits
plt.ylim(min(y_axis), max(y_axis))

#plt.tick_params(axis='y', which='major', direction='out', length=2, color='gray')
plt.xticks(x_axis, ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), fontsize=13)
plt.yticks(y_axis, y_axis_fmt, fontsize=13)
plt.xlabel('')
plt.ylabel('Number of Casualties', fontsize=13)

# Add Data Labels for bar values
ax = b.axes
for p in ax.patches:
    ax.annotate(s="{:,.0f}".format(p.get_height()), xy=((p.get_x() + p.get_width() / 2., p.get_height()-500)),
                ha='center', va='center', color='white', xytext=(0, 2), 
                textcoords='offset points', weight='bold', fontsize=13)  

plt.title('Total Traffic Accidents by Day of Week (in 2014)', fontsize=13)
plt.savefig('Images/2014-accidents-by-dayofweek.png')
plt.show()
# Plot boxplot showing average number of casualties by day of week
plt.figure(figsize=(10,6))
sns.set_style('darkgrid')
sns.boxplot(x='Day of Week', y='Number of Casualties', data=accidents_by_date, 
            palette=sevenColorPalette)

# Define x_axis for xticks
x_axis = np.arange(0,7,1)

# Calculate upper bound of y-axis
y_max = 700
step = 100
y_axis = np.arange(200, y_max+step, step)
# format y-ticks as comma separated
y_axis_fmt = ["{:,.0f}".format(y) for y in y_axis]

plt.ylim(min(y_axis), max(y_axis))

#plt.tick_params(axis='y', which='major', direction='out', length=2, color='gray')
plt.xticks(x_axis, ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'), fontsize=13)
plt.yticks(y_axis, y_axis_fmt, fontsize=13)

plt.xlabel('')
plt.ylabel('Number of Casualties', fontsize=13)

plt.title('Number of Traffic Accidents by Day of Week (in 2014)', fontsize=13)
plt.savefig('Images/2014-boxplot-accidents-per-dayofweek.png')
plt.show()
x_axis = accidents_by_hour_pivot.index

# Plot each weekday and assigning color to be consistent with previous charts
plt.figure(figsize=(10,6))
plt.plot(x_axis, accidents_by_hour_pivot['Monday'], color='#DACF68')
plt.plot(x_axis, accidents_by_hour_pivot['Tuesday'], color='#6CDB69')
plt.plot(x_axis, accidents_by_hour_pivot['Wednesday'], color='#4CDCAE')
plt.plot(x_axis, accidents_by_hour_pivot['Thursday'], color='#559BD6')
plt.plot(x_axis, accidents_by_hour_pivot['Friday'], color='#8757D4')

# Determine y-axis
y_max = 1300
step = 100
y_axis = np.arange(0, y_max+step, step)
# format y-ticks as comma separated
y_axis_fmt = ["{:,.0f}".format(y) for y in y_axis]
# set y-axis limits
plt.ylim(min(y_axis), max(y_axis))

# Format axes ticks and labels
plt.xticks(np.arange(len(x_axis)), x_axis, fontsize=13)
plt.yticks(y_axis, y_axis_fmt, fontsize=13)
plt.xlabel('Hour of Day', fontsize=13)
plt.ylabel('Number of Casualties', fontsize=13)

plt.legend(fontsize=13, loc='upper left')
plt.title("Weekday Traffic Accidents by Time of Day (in 2014)", fontsize=13)
plt.savefig('Images/2014-weekday-accidents-by-hour.png')
plt.show()
# Plot for Weekends
plt.figure(figsize=(10,6))
plt.plot(accidents_by_hour_pivot['Sunday'], color='#DD5B58')
plt.plot(accidents_by_hour_pivot['Saturday'], color='#DE54BB')

# Determine y-axis
y_max = 1300
step = 100
y_axis = np.arange(0, y_max+step, step)
# format y-ticks as comma separated
y_axis_fmt = ["{:,.0f}".format(y) for y in y_axis]
# set y-axis limits
plt.ylim(min(y_axis), max(y_axis))

# Format axes ticks and labels
plt.xticks(np.arange(len(x_axis)), x_axis, fontsize=13)
plt.yticks(y_axis, y_axis_fmt, fontsize=13)
plt.xlabel('Hour of Day', fontsize=13)
plt.ylabel('Number of Casualties', fontsize=13)

plt.legend(fontsize=13, loc='upper left')
plt.title("Weekend Traffic Accidents by Time of Day (in 2014)", fontsize=13)
plt.savefig('Images/2014-weekend-accidents-by-hour.png')
plt.show()
area_road_type = traffic_df.groupby(['Urban or Rural Area',
                                     'Road Type',
                                    'Accident Severity']).sum()['Number of Casualties'].to_frame().reset_index()

# Convert Urban or Rural Area (1 or 2) raw data for respective area
area_road_type['Urban or Rural Area'] = [str('Urban') if value==1 else str('Rural') if value==2 else str('Neither') 
                                         for value in area_road_type['Urban or Rural Area']]
area_type = area_road_type.groupby(['Urban or Rural Area', 'Accident Severity']).sum()['Number of Casualties'].to_frame().reset_index()
total_casualties = area_type['Number of Casualties'].sum()

road_type = area_road_type.groupby(['Urban or Rural Area', 'Road Type']).sum()['Number of Casualties'].to_frame().reset_index()
urban_road = road_type.loc[road_type['Urban or Rural Area']=='Urban',:].sort_values('Number of Casualties', 
                                                                                    ascending=False)
rural_road = road_type.loc[road_type['Urban or Rural Area']=='Rural',:].sort_values('Number of Casualties', 
                                                                                    ascending=False)


plt.figure(figsize=(10,6))
g = sns.barplot(x='Urban or Rural Area', y='Number of Casualties', hue='Accident Severity', data=area_type, 
                palette=threeColorPalette, linewidth=1, edgecolor='black', alpha=0.75)
sns.set_style('darkgrid')

# Determine y-axis
y_max = max(area_type['Number of Casualties'])+2500
y_max -= y_max % -10000
step = 10000
y_axis = np.arange(0, y_max+step, step)
# format y-ticks as comma separated
y_axis_fmt = ["{:,.0f}".format(y) for y in y_axis]
# set y-axis limits
plt.ylim(min(y_axis), max(y_axis))

# Format axes ticks and labels
plt.xticks(fontsize=13)
plt.yticks(y_axis, y_axis_fmt, fontsize=13)

plt.xlabel('')
plt.ylabel('Number of Casualties', fontsize=13)

ax = g.axes
for p in ax.patches:
    ax.annotate(s="{:,.0f}%".format((p.get_height()/total_casualties)*100)+"\n"+("{:,.0f}".format(p.get_height())), 
                xy=((p.get_x() + p.get_width() / 2., p.get_height()+2000)),
                ha='center', va='center', color='black', xytext=(0, 2), 
                textcoords='offset points', fontsize=13)  
plt.legend(loc='upper left', title='Accident Severity', frameon=True)
plt.title('Total Traffic Accidents by Area (in 2014)', fontsize=13)
plt.savefig('Images/2014-accidents-by-areatype.png')
plt.show()
explode = (0.0,0.05,0.0,0.0,0.0)
plt.figure(figsize=(10,6))

plt.pie(urban_road['Number of Casualties'], explode=explode, labels=urban_road['Road Type'], counterclock=True,
        labeldistance=1.05, autopct='%.0f%%', pctdistance=0.8, shadow=True, colors=fiveColorPalette)

# Draw circle
centre_circle = plt.Circle((0,0),0.60,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  
plt.tight_layout()

plt.title('Urban Traffic Casualties by Road Type', fontsize=13)
plt.savefig('Images/2014-urban-accidents-by-roadtype.png')
plt.show()
explode = (0.0,0.05,0.0,0.0,0.0)
plt.figure(figsize=(10,6))

plt.pie(rural_road['Number of Casualties'], explode=explode, labels=rural_road['Road Type'], counterclock=True,
        labeldistance=1.05, autopct='%.0f%%', pctdistance=0.8, shadow=True, colors=fiveColorPalette)

# Draw circle
centre_circle = plt.Circle((0,0),0.60,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')  
plt.tight_layout()

plt.title('Rural Traffic Casualties by Road Type', fontsize=13)
plt.savefig('Images/2014-rural-accidents-by-roadtype.png')
plt.show()
urban = traffic_df[traffic_df["Urban or Rural Area"] == 1]
rural = traffic_df[traffic_df["Urban or Rural Area"] == 2]

#--------------- Calculations by City Type --------------- 
rural_mean_1 = rural.groupby(["Date"]).mean()["Accident Severity"]
rural_mean_2 = rural.groupby(["Date"]).mean()["Number of Casualties"]
rural_count_3 = rural.groupby(["Date"]).count()["Accident Index"]

urban_mean_1 = urban.groupby(["Date"]).mean()["Accident Severity"]
urban_mean_2 = urban.groupby(["Date"]).mean()["Number of Casualties"]
urban_count_3 = urban.groupby(["Date"]).count()["Accident Index"]

#--------------- Set Parameters for Scatterplot --------------- 
plt.rcParams["figure.figsize"] = [16,9]
sns.set()

plt.title("Average Severity vs. Average Casualty by City Type", size=20)
plt.ylabel("Average Severity", size=20)
plt.xlabel("Average Casualties", size=20)
plt.ylim([3, 2.6])
plt.scatter(rural_mean_2,
            rural_mean_1,
            color="#DACF68",
            s=rural_count_3*2,
            edgecolor="black", linewidths= 0.1,
            alpha=0.8, label="Rural")

plt.scatter(urban_mean_2,
            urban_mean_1,
            color="#8757D4",
            s=urban_count_3*2,
            edgecolor="black", linewidths=0.1, marker="^", 
            alpha=0.8, label="Urban")

#--------------- Set Legend --------------- 
plt.legend(title='City Type', loc='center left', bbox_to_anchor=(1, 0.5), fontsize=15)

#--------------- Save and Show --------------- 
plt.savefig('Images/Severity and Casualty by City Type.png')
plt.show()
grouper_1 = traffic_df[['Weather Conditions','Accident Severity']]
weather_severity = grouper_1.groupby(by = 'Weather Conditions',as_index=False).sum()
plt = sns.barplot(weather_severity['Accident Severity'],weather_severity['Weather Conditions'])
pl.savefig('Images/Weather and Severity Correlation.png')# # Severity and Weather Correlation
grouper_2 = traffic_df[['Light Conditions','Accident Severity']]
light_condition_severity = grouper_2.groupby(by = 'Light Conditions',as_index=False).sum()
plt = sns.barplot(light_condition_severity['Accident Severity'],light_condition_severity['Light Conditions'])
pl.savefig('Images/Light Condition and Severity Correlation')
grouper_3 = traffic_df[['Road Type','Accident Severity']]
road_type_severity = grouper_3.groupby(by = 'Road Type',as_index=False).sum()
plt = sns.barplot(road_type_severity['Accident Severity'],road_type_severity['Road Type'])
pl.savefig('Images/Road Type and Severity Correlation')
grouper_c = traffic_df[['Road Type','Accident Severity']]
road_type_severity_1 = grouper_c.groupby(by = 'Accident Severity',as_index=False).count()
plt = sns.barplot(road_type_severity_1['Accident Severity'],road_type_severity_1['Road Type'])
pl.savefig('Images/Severity and Road Type Correlation')


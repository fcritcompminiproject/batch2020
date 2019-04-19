weather_condition_number_list = []

for condition in traffic_df['Weather Conditions']:
    
    if (condition == 'Fine without high winds'):
        weather_condition_number_list.append(3)
        
    if (condition == 'Raining without high winds'):
        weather_condition_number_list.append(3)
        
    if (condition == 'Raining with high winds'):
        weather_condition_number_list.append(2)
        
    if (condition == 'Other'):
        weather_condition_number_list.append(2)
        
    if (condition == 'Fine with high winds'):
        weather_condition_number_list.append(2)
        
    if (condition == 'Fog or mist'):
        weather_condition_number_list.append(1)
    
    if (condition == 'Snowing without high winds'):
        weather_condition_number_list.append(1)
        
    if (condition == 'Snowing with high winds'):
        weather_condition_number_list.append(1)
road_type_number_list = []

traffic_df['Road Type'].value_counts()

for road in traffic_df['Road Type']:
    
    if (road == 'Single carriageway'):
        road_type_number_list.append(3)
    
    if (road == 'Dual carriageway'):
        road_type_number_list.append(3)
        
    if (road == 'Roundabout'):
        road_type_number_list.append(2)
        
    if (road == 'One way street'):
        road_type_number_list.append(2)
        
    if (road == 'Slip road'):
        road_type_number_list.append(1)
light_condition_number_list = []

for condition in traffic_df['Light Conditions']:
    
    if (condition == 'Daylight: Street light present'):
        light_condition_number_list.append(3)

    if (condition == 'Darkness: Street lights present and lit'):
        light_condition_number_list.append(3)
        
    if (condition == 'Darkness: No street lighting'):
        light_condition_number_list.append(2)
        
    if (condition == 'Darkness: Street lighting unknown'):
        light_condition_number_list.append(1)
        
    if (condition == 'Darkness: Street lights present but unlit'):
        light_condition_number_list.append(1)
#appending it into a data frame

training_data = pd.DataFrame({'Weather':weather_condition_number_list,
                              'Road Type':road_type_number_list,
                              'Light Condition':light_condition_number_list                          
                              })
import random    

weather_testing = []
road_testing = []
light_testing = []

for i in range (54147):    

    weather_testing.append(random.randrange(0,4,1))  
    road_testing.append(random.randrange(0,4,1))
    light_testing.append(random.randrange(0,4,1))  

    weather_testing.append(random.randrange(0,8,1))  
    road_testing.append(random.randrange(0,5,1))
    light_testing.append(random.randrange(0,5,1))  
#process: appending it to a set of 3 to create test data
test_data = []
for i in range(54147):
    temp=[]
    temp.append(weather_testing[i])
    temp.append(road_testing[i])
    temp.append(light_testing[i])
    test_data.append(temp)      
X = training_data[['Weather','Road Type','Light Condition']]
Y = traffic_df['Accident Severity']
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
prediction = clf.predict(test_data)
# # Test Labels



# # Exporting the CSV

csv_data = pd.DataFrame({'Weather Conditions': weather_condition_number_list, 
                         'Road Type': road_type_number_list,
                         'Light Condition': light_condition_number_list,
                         'Severity': traffic_df['Accident Severity']
                        })
csv_data.to_csv('Resources/regression.csv')
csv_data.head()




other_df = pd.DataFrame({'Weather Conditions': traffic_df['Weather Conditions'], 
                         'Road Type': traffic_df['Road Type'],
                         'Light Condition': traffic_df['Light Conditions'],
                         'Severity': traffic_df['Accident Severity']})
other_df.to_csv('indian-accidents.csv')
test_labels = []
for i in range(0, len(traffic_df)):
    
    if(traffic_df.iloc[i]['Weather Conditions']=='Fine without high winds' or 
       traffic_df.iloc[i]['Weather Conditions']=='Raining without high winds'and
       traffic_df.iloc[i]['Road Type']== 'Single carriageway' or
       traffic_df.iloc[i]['Road Type']== 'Dual carriageway' and
       traffic_df.iloc[i]['Light Conditions']== 'Daylight: Street light present' or
       traffic_df.iloc[i]['Light Conditions']== 'Darkness: Street lights present and lit'):
        
        test_labels.append(3)
        
    if(traffic_df.iloc[i]['Weather Conditions']=='Raining with high winds' or 
       traffic_df.iloc[i]['Weather Conditions']=='Fine with high winds' or 
       traffic_df.iloc[i]['Weather Conditions']=='Other'and
       traffic_df.iloc[i]['Road Type']== 'Roundabout' or
       traffic_df.iloc[i]['Road Type']== 'One way street' and
       traffic_df.iloc[i]['Light Conditions']== 'Darkness: No street lighting'):
        
        test_labels.append(2)
        
    if(traffic_df.iloc[i]['Weather Conditions']=='Fog or mist' or 
       traffic_df.iloc[i]['Weather Conditions']=='drizzling without high winds' or 
       traffic_df.iloc[i]['Weather Conditions']=='drizzling with high winds'and
       traffic_df.iloc[i]['Road Type']== 'Slip road' and
       traffic_df.iloc[i]['Light Conditions']== 'Darkness: Street lighting unknown'or
       traffic_df.iloc[i]['Light Conditions']== 'Darkness: Street lights present but unlit'):
        
        test_labels.append(1)
import numpy as np
from sklearn.metrics import accuracy_score
accuracy_score(test_labels[0:54147], prediction)

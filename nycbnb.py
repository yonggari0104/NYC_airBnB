import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')



nyc = pd.read_csv('C:\\Users\\user\\.spyder-py3\\nycbnb\\nycbnb.csv')

#SEE IF NaN VALUES EXISTS
print(nyc.isna().any())

print(nyc.info())
print(nyc.head())
print(nyc.dtypes)
print(nyc.describe())


#DROPS FOLLOWING COLUMNS
nyc.drop(['id','host_name','last_review'], axis=1, inplace=True)



#REPLACES ALL THE NaN TO 0 FOR 'REVIEWS PER MONTH'
nyc.fillna({'reviews_per_month':0}, inplace=True)









#NEIGHBOURHOOD BREAKDOWN

#DIFFERENT NEIGHBOURHOODS
print(nyc.neighbourhood_group.unique())

#BAR GRAPH OF ROOM TYPE BY NEIGHBOURHOOD
plt.figure(figsize=(10,6))
sns.countplot(x = 'room_type',hue = "neighbourhood_group",data = nyc)
plt.title("Room Types Occupied By Neighbourhood")
plt.show()













#DIFFERENT ROOM TYPES
print(nyc.room_type.unique())

#ROOM TYPE BREAKDOWN
plt.style.use('fivethirtyeight')
f,ax=plt.subplots(1,2,figsize=(18,8))
nyc['room_type'].value_counts().plot.pie(explode=[0,0.05,0],autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Room Type')
ax[0].set_ylabel('Room Type')
sns.countplot('room_type',data=nyc,ax=ax[1],order=nyc['room_type'].value_counts().index)
ax[1].set_title('Room Type')
plt.show()











#PRINT TOP HOSTS' ID
print(nyc.host_id.value_counts().head(10))






plt.style.use('fivethirtyeight')
bnb = nyc[nyc.price <500]
plt.figure(figsize=(10,6))
sns.boxplot(y="price",x ='neighbourhood_group' ,data = bnb)
plt.title("Neighbourhood Price Distribution < 500")
plt.show()








#DISTRIBUTION OF PRICE
def rank_price(hotel_price):
    if hotel_price<=75:
        return 'Low'
    elif hotel_price >75 and hotel_price<=500:
        return 'Medium'
    else:
        return 'High'
nyc['price'].apply(rank_price).value_counts().plot(kind='bar');

print("NYC is expensive")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap # For geographical map
sns.set_style("darkgrid")
df = pd.read_excel("C:\\Users\Arya Kulkarni\Desktop\Miniproj\data.xlsx", sheet_name="Sheet1")
df.head(1)
map = Basemap(lat_0=19.0, lon_0=71)
plt.figure(figsize=[20,10])
map.drawcoastlines(linewidth=.5,color="g")
map.drawcountries(linewidth=.5)
# map.drawcounties()
# map.drawstates(color="r")
map.fillcontinents(color="green",alpha=.1)
plt.scatter(df.Long,df.Lat,alpha=.1,color="m")
plt.show()
sns.pairplot(df[["Year","Male","Female","Total"]],diag_kind="kde")
plt.show()
plt.figure(figsize=(16,4))
sns.scatterplot(df.CAUSE,df.Male)
plt.xticks(rotation=90)
plt.show()
plt.figure(figsize=(16,4))
sns.boxplot(df.CAUSE,df.Male)
# sns.swarmplot(df.CAUSE,df.Male)
plt.xticks(rotation=90)
plt.show()
sns.pairplot(df[["Year","Male","Female","Total"]],diag_kind="kde")
plt.show()

plt.figure(figsize=(16,4))
grp1 = df.groupby("Year")
for k in grp1.groups:
    tmp = df[df.Year == k]
    overall = tmp.Total.sum()
    male_cnt = tmp.Male.sum()
    female_cnt = tmp.Female.sum()
    
    plt.bar(k,overall)
    plt.text(k,overall,overall)
    
plt.xticks(range(2001,2013))
plt.show()

plt.figure(figsize=(16,4))
grp1 = df.groupby("Year")
for k in grp1.groups:
    tmp = df[df.Year == k]
    male_cnt = tmp.Male.sum()
    female_cnt = tmp.Female.sum()
    
    plt.bar(k,male_cnt,color="r")
    plt.text(k,male_cnt,male_cnt)
    
    plt.bar(k,female_cnt,color="m")
    plt.text(k,female_cnt,female_cnt)

plt.xticks(range(2001,2013))
plt.legend(["Male","Female"])
plt.show()

plt.figure(figsize=(16,4))
# grp1 = df.groupby("Year")
# grp1.Year.value_counts()
male_cnt = df.pivot(columns="Year").Male.sum().reset_index(name="cnt")
female_cnt = df.pivot(columns="Year").Female.sum().reset_index(name="cnt")
sns.barplot(male_cnt.Year,male_cnt.cnt,palette="coolwarm",label="Male")
sns.barplot(female_cnt.Year,female_cnt.cnt,label="Female")
plt.legend()
plt.show()

plt.figure(figsize=(16,4))
Total = df.pivot(columns="States").Total.sum().reset_index(name="cnt")
Total.sort_values(by="cnt",ascending=False,inplace=True)
sns.barplot(Total.States,Total.cnt,palette="winter")
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(16,4))
male_cnt = df.pivot(columns="States").Male.sum().reset_index(name="cnt")
female_cnt = df.pivot(columns="States").Female.sum().reset_index(name="cnt")
male_cnt.sort_values(by="cnt",ascending=False,inplace=True)
sns.barplot(male_cnt.States,male_cnt.cnt,palette="winter",label="Male")
sns.barplot(female_cnt.States,female_cnt.cnt,color="r",label="Female")
plt.xticks(rotation=90)
plt.legend()
plt.show()

plt.figure(figsize=(16,4))
total_deatth_by_cause = df.pivot(columns="CAUSE").Total.sum().reset_index(name="cnt")
total_deatth_by_cause
total_deatth_by_cause.sort_values(by="cnt",ascending=False,inplace=True)
sns.barplot(total_deatth_by_cause.CAUSE,total_deatth_by_cause.cnt,palette="nipy_spectral_r",)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(16,8))
pi = df.pivot_table("Male","States","Year")
sns.heatmap(pi,square=False,annot=True,fmt="1.2g")
plt.show()

plt.figure(figsize=(16,8))
pi = df.pivot_table("Female","States","Year")
sns.heatmap(pi,square=False,annot=True,fmt="1.2g")
plt.show()

plt.figure(figsize=(16,8))
pi = df.pivot_table("Total","CAUSE","Year")
sns.heatmap(pi,square=False,annot=True,fmt="1.2g")
plt.show()

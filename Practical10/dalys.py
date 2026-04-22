import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Set working dir
os.chdir("E:/fyx2025-26/zje/IBI/Week_10/Practical10")
# Check working dir
print("Current working directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Import dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show first 5 rows
print("\nFirst 5 rows of data:")
print(dalys_data.head(5))
# Show dataframe info
print("\nDataframe information:")
dalys_data.info()
# Show descriptive statistics
print("\nDescriptive statistics:")
print(dalys_data.describe())

# First row, fourth column
print("\nFirst row, fourth column value:")
print(dalys_data.iloc[0, 3])

#print(dalys_data.iloc[2,0:5])
#print(dalys_data.iloc[0:2,:])
#print(dalys_data.iloc[0:10:2,0:5]) # Select the first 10 rows at the step of 2, and first 5 columns(all)

# Third and fourth columns (Year & DALYs) for first 10 rows
first_10 = dalys_data.iloc[0:10,2:4]
print("\nFirst 10 rows - Year and DALYs:")
print(first_10)
# Max DALYs in first 10 years for Afghanistan
max_daly_value = first_10['DALYs'].max()
afghanistan_max_year = first_10[first_10['DALYs'] == max_daly_value]['Year'].iloc[0]
print(f"\nYear with maximum DALYs in Afghanistan's first 10 years: {afghanistan_max_year}")  
# The year reporting max DALY among first 10 years: 1998
# Boolean indexing with iloc
my_columns = [True, True, False, True]
print("\nFirst 3 rows with selected columns (Boolean index):")
print(dalys_data.iloc[0:3, my_columns])

# Access data with loc & filter for Zimbabwe
zimbabwe_data = dalys_data.loc[dalys_data.Entity  == 'Zimbabwe', ['Year','DALYs']]
print("\nZimbabwe DALYs data:")
print(zimbabwe_data)
# First and last year for Zimbabwe
zimbabwe_first_year = zimbabwe_data['Year'].min()
zimbabwe_last_year = zimbabwe_data['Year'].max()
print(f"\nZimbabwe DALYs recorded from {zimbabwe_first_year} to {zimbabwe_last_year}") 
# First year: 1990
# Last year: 2019

# Analyze 2019 data
recent_data = dalys_data.loc[dalys_data.Year == 2019, ['Entity','DALYs']]
# Find country with maximum DALYs in 2019
max_daly_country = recent_data.loc[recent_data['DALYs'] == recent_data['DALYs'].max(), 'Entity'].iloc[0]
print(f"\nCountry with 2019 Maximum DALYs: {max_daly_country}")
# Find country with minimum DALYs in 2019
min_daly_country = recent_data.loc[recent_data.DALYs == recent_data['DALYs'].min(), 'Entity'].iloc[0]
print(f"\nCountry with 2019 Minimum DALYs: {min_daly_country}")
# 2019 max DALY country: Lesotho
# 2019 min DALY country: Singapore

# Plot DALYs over time for the country with maximum DALYs in 2019
country_max = dalys_data.loc[dalys_data['Entity'] == max_daly_country, ['Year', 'DALYs']]
plt.plot(country_max.Year, country_max.DALYs, 'bo') #b/r = blue/red; o/+: shape of dots
plt.title(f'DALY of {max_daly_country}')
plt.xlabel('Year', fontsize=12)
plt.ylabel('DALYs', fontsize=12)
plt.xticks(country_max.Year,rotation=-90)
plt.show()


# Answer questions: What was the distribution of DALYs across all countries in 2019?
plt.boxplot(recent_data['DALYs'], vert=True, patch_artist=True)
plt.title('Distribution of DALYs Across All Countries in 2019', fontsize=14)
plt.ylabel('DALYs', fontsize=12)
plt.show()
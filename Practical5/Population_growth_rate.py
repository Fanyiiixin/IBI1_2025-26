#Import matplotlib
import matplotlib.pyplot as plt
population_data = {
    "UK": {"population 2020": 66.7, "population 2024": 69.2},
    "China": {"population 2020": 1426, "population 2024": 1410},
    "Italy": {"population 2020": 59.4, "population 2024": 58.9},
    "Brazil": {"population 2020": 208.6, "population 2024": 212.0},
    "USA": {"population 2020": 331.6, "population 2024": 340.1}
}

#calculate the percent change
percent_change = {}
for country, data in population_data.items():
    pop_2020 = data["population 2020"]
    pop_2024 = data["population 2024"]
    change = ((pop_2024 - pop_2020) / pop_2020) * 100
    percent_change[country] = round(change, 2)
#Print the percent change for each country
for country, change in percent_change.items():
    print(country,": ",change)
#Print	the	population	changes	in	descending	order
sorted_change = sorted(percent_change.items(), key=lambda x: x[1],reverse=True)
print("Percent change for each country from 2020 to 2024: ")
for country, change in sorted_change:
    print(country,": ",change,"%")

#Identify the largest increase and decrease
largest_increase_country = max(percent_change, key=percent_change.get)
largest_increase_value = percent_change[largest_increase_country]

largest_decrease_country = min(percent_change, key=percent_change.get)
largest_decrease_value = percent_change[largest_decrease_country]
print("Largest population increase: ",largest_increase_country,": ",largest_increase_value)
print("Largest population decrease: ",largest_decrease_country,": ",largest_decrease_value)

#Create the bar chart
countries = [item[0] for item in sorted_change]
changes = [item[1] for item in sorted_change]

width = 0.35
plt.bar(countries,changes,width)
plt.xlabel("Country")
plt.ylabel("Changes")

plt.show()
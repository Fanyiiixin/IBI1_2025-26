total_students = 91          # Total students in the class
initial_infected = 5         # Initial number of infected students (day 0)
growth_rate = 0.4            # Daily infection growth rate (40%)
# Initialise variables
current_infected = initial_infected
days = 0

# Infection loop
while current_infected < total_students:
  days += 1
  new_infected = current_infected * growth_rate
# Make sure the total infected number won't exceed the total students number
  if current_infected + new_infected > total_students:
    new_infected = total_students - current_infected
  current_infected += new_infected
  print("Day",days," new infected:",new_infected," current_infected:",current_infected)
print("Total days to infect all: ",days)

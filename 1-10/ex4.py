# ex4.py - Variables and Names

# Declare a variable named `cars` and assign it the value 100
cars = 100
# Declare a variable named `space_in_car` and assign it the value 4.0
space_in_car = 4.0
# Declare a variable named `drivers` and assign it the value 30
drivers = 30
# Declare a variable named `passengers` and assign it the value 90
passengers = 90
# Declare a variable named `cars_not_driven` and assign it the result of evaluating `cars - drivers`
cars_not_driven = cars - drivers
# Declare a variable named `cars_driven` and assign it the result of evaluating `drivers`
cars_driven = drivers
# Declare a variable named `carpool_capacity` and assign it the result of evaluating `cars_driven * space_in_car`
carpool_capacity = cars_driven * space_in_car
# Declare a variable named `average_passengers_per_car` and assign it the result of evaluating `passengers / cars_driven`
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")

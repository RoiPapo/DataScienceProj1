population_type = ['Men', 'Women', 'All']

# Insert sum, mean and median inside the curly brackets.

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Question 1:")
for population in population_type:
    print(f"{population}:\n"
          f"Age: {sum(test_list)}, {sum(test_list)}, {sum(test_list)}\n"
          f"Earnings: {sum(test_list)}, {sum(test_list)}, {sum(test_list)}\n"
          f"Hours: {sum(test_list)}, {sum(test_list)}, {sum(test_list)}\n"
          f"Week: {sum(test_list)}, {sum(test_list)}, {sum(test_list)}")

print("\nQuestion 2:")

min_val_list = [0, 11]
max_val_list = [10, 20]

# Insert mean and median inside the curly brackets

for i in range(len(min_val_list)):
    print(f"If {min_val_list[i]}<=Y<={max_val_list[i]}, then:\n"
          f"Married Women:\n"
          f"Earnings: {sum(test_list)}, {sum(test_list)}\n"
          f"Unmarried Women:\n"
          f"Earnings: {sum(test_list)}, {sum(test_list)}")
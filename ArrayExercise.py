
expenses = [2200, 2350, 2600, 2130, 2190]

print("In February extra expenses is: ", expenses[1] - expenses[0])

print("Total Cost in the first quarter: ", expenses[0] + expenses[1] + expenses[2])

print("Did I spent exactly $2000 in any Month? ", 2000 in expenses)

expenses.append(1980)

print("My Expenses after June", expenses)

expenses[3]= expenses[3] - 200

print("After returning $200 product my total expenses: ", expenses)

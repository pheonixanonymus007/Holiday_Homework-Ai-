# %%
#answer5
a = input("Enter name of student: ")
b = int(input("Enter class of student: "))
c = int(input("Enter age of student: "))
print("Name:", a, "Class:", b, "Age:", c)
print("Name:", a)
print("Class:", b)
print("Age:", c)

# %%
#answer6 
#a)

original_balance = 10000
interest_rate = 5
final = original_balance * (1 + (interest_rate / 100))
print("After one year, the balance in the account is", final)

#b)

original_balance = 10000
interest_rate = 5
for i in range(1, 5):
    final = original_balance * (1 + (interest_rate / 100))
original_balance = final
print("After year", i, "the balance in the account is", final)

#c)

original_balance = 10000
interest_rate = 5
num_years = 0
while original_balance < 2 * original_balance:
    final = original_balance * (1 + (interest_rate / 100))
original_balance = final
num_years += 1
print("It takes", num_years, "years for the balance to be at least double the original balance.")



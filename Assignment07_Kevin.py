# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Demonstrates how Pickling and Structured error handling work
# ChangeLog (Who,When,What):
# Kevin Wong,11.15.2019,Created script
# ------------------------------------------------------------------------ #


# Example 1 for structured error handling -------------------------------- #
print("Example 1 for structured error handling")
try:
   print(x)
except:
   print("An exception has occurred.")
   print("Please define variable 'x' before running the program.")
# ------------------------------------------------------------------------ #
    
    
# Example 2 for structured error handling -------------------------------- #  
print()     # added for looks
print("Example 2 for structured error handling")
while True:
    try:
        int(input("Please enter an integer: "))
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Awesome, you successfully entered an integer!")   
# ------------------------------------------------------------------------ #


# Example 3 for structured error handling -------------------------------- #
print()     # added for looks
print("Example 3 for structured error handling")
try:
    print(x)
except:
    print("An exception has occurred")
finally:
    print("Print this line even if exception occurred")
# ------------------------------------------------------------------------ #


# Example 4 for Pickling and Unpickling ------------------------------------------------- #
# -------- Pickling Code --------
print()     # added for looks
print("Example 4 for Pickling and Unpickling")
import pickle
data = "Hello World"
file = open("testfile", 'wb')
pickle.dump(data, file)
file.close()
# -------------------------------

# ------- Unpickling code -------
i = open("testfile", "rb")
new_data = pickle.load(i)
print(new_data)
# -------------------------------
# ------------------------------------------------------------------------ #


input("Press Enter to Exit")
# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd # We imported pandas as pd and extracted tables from the provided URL
simpsons = pd.read_html(str(input("Enter The Link With Tables : ")))
print ("Number of tables present in webpage " + str(len(simpsons))) # Counted how many are table are present in the web page with first print statement
index = int(input("Enter The Table Number: "))
print ("Number of columns preset in table " + str(len(simpsons[index]))) # Counted how many columns are present in at a particular index of table.
print (str(simpsons[index])) # Extracting All Table contents

# No error handling at this point, Maximum acceptable index number is one less than 
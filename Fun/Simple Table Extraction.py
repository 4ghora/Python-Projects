# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd # We imported pandas as pd and extracted tables from the provided URL
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)')
index = int(input("Enter The Table Number (MAX: 23) : "))
print ("Number of tables present in webpage " + str(len(simpsons))) # Counted how many are table are present in the web page with first print statement
print ("Number of columns preset in table " + str(len(simpsons[index]))) # Counted how many columns are present in at a particular index of table.
print (str(simpsons[index])) # Extracting All Table contents

# No error handling at this point, Maximum acceptable index number is 23
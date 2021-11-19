log_file = open("um-server-01.txt")
# line one is accessing the um-server-01.txt file in the process.py so that we can access everything in the folder or the objects in that folder


def sales_reports(log_file):
 # line five is defining a function that is accessing the folder that we assigned the variable, too in other words 
 # we assigned the variable to open the um-server-01.txt folder and we trying to access that variable assigned to the folder
 # also log_ file is an argument
    for line in log_file:
# line 6 were writing a for loop to iterate over each line in the file        
        line = line.rstrip()
# in line 8 we are trying to remove any trailing characters (characters at the end a string)        
        day = line[0:3]
# in line 11 we are assigning a variable to line and this is a form of slice notation we start from the first element(index 0) and take a list till the element with index 3.       
        if day == "Mon":           
            print(line)
# line 13 is similar to javascript syntax as far as the triple equals or strictly equal sign meaning it is saying check for each 
# line of code that states the day mon and only return those values line 14 is saying print those values we are trying to access


sales_reports(log_file)
#


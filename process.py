log_file = open("um-server-01.txt")#assigning the um-server-01.txt file to a variable to be accessed in code as an open file



def sales_reports(log_file):#creating a function called sales_reports that accepts the parameter of the open text file assigned to log_file
    for line in log_file:#loops through each row(line) of the open text file(log_file)
        line = line.rstrip()#creates a copy of the current row iteration with trailing whitespaces removed and assigns it to line
        day = line[0:3]#grabs the first three characters in the row iteration and assigns them to day
        if day == "Mon":#compares the characters to "Tue" and if it matches runs the print
            print(line)#prints the current row iteration

def large_melon_orders(log_file):
    for line in log_file:
        order = line.rstrip().split(' ')
        melons = order[2]
        if float(melons) > 10:
            print(line)

sales_reports(log_file)#calls the function of sales_reports and passes in the log_file variable that represents the open text file as a parameter
log_file.seek(0)
large_melon_orders(log_file)
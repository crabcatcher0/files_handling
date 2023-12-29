import csv

def toread():
    print("*** Welcome ***")
    print("Please Choose:\n[1].Customer Id\n[2].First Name\n[3].Last Name\n[4].Company\n[5].City\n[6].Country\n[7].Phone 1\n[8].Phone 2\n[9].Email\n[10].Subscription Date\n[11].Website")
    col_index = int(input("Please choose the number from above."))

    with open('customers.csv') as file_csv:
        file = csv.reader(file_csv)

        for line in file:
            print(line[col_index])



ram = toread()
print(ram)
import csv


def filemenu():
    try:
     print("Welcome:")
     print("** Important ** : Please keep the file in this same directory!!")
     file = input("Please enter file name: ")


     with open(file, 'r') as csv_file :
        result = csv.reader(csv_file) 
        header = next(result, None)

        if header:
            header_data = header
            print(header_data)
        try:
          index_no = int(input("Please enter the number respectively starting from 0: "))
        except ValueError:
            print("Please enter a number respectively!!")
            return None
                    

        data = []


        for line in result:
            try:
             listed_data = line[index_no]
            except IndexError:
             print("Enter a number respective to the index: ")
             return None
            data.append(listed_data)

        with open('result.txt', 'w', newline='') as final_file:
            writer = csv.writer(final_file)
            for row in data:
                writer.writerow([row])
        print("Please check the result.txt file.")

        return data
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
                
filemenu()
        
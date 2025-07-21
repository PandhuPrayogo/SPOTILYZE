# SPOTILYZE

## IMPORT DATA
import pandas as pd

def import_data(name_file):
  file_import = pd.read_csv(f'folder_file/{name_file}') # Don't forget to use delimeter if your type file is .txt
  return file_import

def analyze_file():
  while True:
    print("""Choose one option:
        1. Print all data
        2. Print selected data
        3. Exit
  """)
    user_option = int(input("Choose your option: "))
    if user_option == 1:
      if import_data == None:
        print("No data imported")
      else:
        print(import_data)
    elif user_option == 2:
      while True:
        print("""Choose the right answer in this option:
              1. Print Top and bottom data 
              2. Print selected range of data
              3. Print specific condition based on column
              4. Print selected one data only
              5. Print data with sorting argument
              6. Exit
              """)
        user_option = int(input("Choose one option: "))
        if user_option == 1:
          top_range = int(input("How many range do you want of top of the data (default: 5): "))
          bottom_range = int(input("How many range do you want of bottom of the data (default: 5): "))
          print(import_data.head(top_range))
          print(import_data.tail(bottom_range))
        elif user_option == 2:
          start_range = int(input("Enter the start of the range: "))
          end_range = int(input("Enter the end of the range: "))
          print(import_data.iloc[start_range:end_range])
        elif user_option == 3:
          print('Coming soon')
        elif user_option == 4:
          selected_row = int(input("Which row do you want to search (using number): "))
          selected_column = int(input("Which column do you want ot refers (using number): "))
          selected_row = import_data.iloc[selected_row,selected_column]
        elif user_option == 5:
          user_sorting = input("Do you want use ascending or descending (a/d): ")
          if user_sorting.lower() == 'a':
            print(import_data.sort_values(ascending=True))
          elif user_sorting.lower() == 'd':
            print(import_data.sort_values(ascending=False))
        elif user_option == 6:
          break
    elif user_option == 3:
      break
    else:
      print("Your input is invalid, please try again!")
      continue
## MAIN PROGRAM
### Section Instruction

print("""WELCOME TO OUR SPOTILYZE
Please read the instruction before using the program
1. At least have one file to analyze
2. Make sure the file is in the correct format (.JSON)
3. Make sure the file is in the correct location
4. Enjoy using this program, rate after you using it
""")

### Section Main
while True:
  print("""Select one option:
1. Import your file
2. Analyze it
3. Exit
""")
  user_option = int(input("Choose one option: "))
  if user_option == 1:
    file_name = str(input("Text your file with that type: "))
    import_data(file_name)
    print(f"{file_name} added.\n")
  elif user_option == 2:
    analyze_file()
  elif user_option == 3:
    print("Thankyou for using our program, see you next time")
    break
  else:
    print("Your input is invalid, please try again!")
    continue
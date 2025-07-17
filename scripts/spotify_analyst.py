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
      print("Coming Soon")
    elif user_option == 3:
      break
## MAIN PROGRAM
### Section Instruction

print("""WELCOME TO OUR SPOTILYZE
Please read the instruction before using the program
1. At least have one file to analyze
2. Make sure the file is in the correct format (.xlsx, .csv, .txt)
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
    print(f"{file_name} added.")
  elif user_option == 2:
    analyze_file()
  elif user_option == 3:
    print("Thankyou for using our program, see you next time")
    break
  else:
    print("Your input is invalid, please try again!")
    continue
# Create a function of phone book using dict
def phone_book():
    phone_dict = {}
    while True:
      print("Welcome in Phone Book \nHere is following function - \nwrite -> add - for adding contact \nwrite -> search - for search contact\nwrite -> delete - for delete contact\nwrite -> exit - for exit")
      user_input = input("Enter here : ")

      # Add
      if (user_input == "add"):
          name = input("Enter the name you want of contact : ")
          number = input("Enter the number of contact : ")
          phone_dict[name] = number

          print(f"Contact - {name} and {number} added successfully !")

      # Search
      elif (user_input == "search"):
          name = input("Enter the name you want to search : ")

          if name in phone_dict:
              print(f"Name - {name} and Number - {phone_dict[name]}")
          else:
            print("Contact Not Found")

      # Delete
      elif (user_input == "delete"):
        name = input("Enter the name you want to delete : ")

        if name in phone_dict:
          del phone_dict[name]
          print(f"Contact - {name} is deleted successfully !")
          
      # Exit
      elif (user_input == "exit"):
        print("Good Bye")
        break

      else:
        print("invalid choice")

# Run The Code
phone_book()
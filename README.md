## What i Did ?
#### Step - 1 Create a function which can check the give number is prime or not.
- first condition i write the number should be greater than 1
- second condition as we no prime number are divisible by 1 or itself. so instead of checking each number one by one i get the square root of the number than apply loop from 2-sqrt of number than finally return the result.

#### Step - 2 Create a function which can calculate the average marks of a student and  Grade.
- Create a function  name average_marks which takes list of integer or float using "Union".
- Than get the size of the list using len function
- than apply loop till size of it and inside it add all the list of element one by one in a variable sum. than finally calculate the average by dividing the sum to len of the list.
- To calculate the grade create four categories **GRAD-A above 75,"GRAD-B 50-75","GRAD-C 33-50","GRAD-F less than 33**"

#### Step - 3 Create a phone_book function using dictionary which had function - add,search and delete.
- Apply while loop which is learn until usser enter **exit**
- First of all it will show the menu in which all the functionality written along with there keys to enter.
- if user enter **add** than it will ask the name first after that it will ask the number than save it.
- if user enter **search** than it ask name of the contact want to search if present than return the **number** else return **Contact Not Found**.
- if user enter **delete** than it ask name of the contact want to delete if present than return the **contact deleted successfully** else return **Contact Not Found**.
- if user enter **exit** than it will stop the function and return **Good Bye**.
- if user enter anything else it will return **invalid choice**.

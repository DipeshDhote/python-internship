from typing import Union

# Calculate Average Marks
def average_marks(list_of_marks:Union[int,float]):
    size = len(list_of_marks)
    sum = 0
    for marks in list_of_marks:
        sum +=marks
    
    average = sum/size
    print(f"The Average Marks is : ",average)
    
    if average >=75:
        print("GRADE A")
    elif average >= 50 and average < 75 :
        print("GRADE B")
    elif average >=33 and average < 50:
        print("GRADE C")
    else:
        print("GRADE F")


ls = [23,30,35,15,20]

average_marks(ls)
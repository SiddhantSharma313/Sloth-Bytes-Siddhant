def missingnum():
    List_of_numbers = eval(
        input("Enter a list of numbers from 1-10 excluding any one of them:")
    )
    Parent_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in List_of_numbers:
        if i in Parent_list:
            Parent_list.remove(i)
    print("The missing number is:", Parent_list[0])
    print(List_of_numbers)


missingnum()

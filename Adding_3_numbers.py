def user_input_of_3_numbers():
    user_input1 = int(input("please enter the first number: "))
    user_input2 = int(input("please enter the second number : "))
    user_input3 = int(input("please enter the third number: "))

    return user_input1, user_input2, user_input3


def adding_three_numbers(x, y, z):
    sum_of_three_numbers = x + y + z
    return sum_of_three_numbers




if __name__ == "__main__":
    print("welcome")
    x, y, z = user_input_of_3_numbers()
    a = adding_three_numbers(x, y, z)
    print(a)
    print(f"sum_of_three_numbers")






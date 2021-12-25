def add_3_numbers():
    user_input1 = int(input("please enter the first number: "))
    user_input2 = int(input("please enter the second number : "))
    user_input3 = int(input("please enter the third number: "))

    return user_input1, user_input2, user_input3


def three_numbers(x, y, z):
    sum_of_three_numbers = x + y + z
    print(f"sum_of_three_numbers:{sum_of_three_numbers}")




if __name__ == "__main__":
    print("welcome")
    user_input1, user_input2, user_input3 = add_3_numbers()
    three_numbers(user_input1, user_input2, user_input3)




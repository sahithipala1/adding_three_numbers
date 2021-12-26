from Adding_3_numbers import three_numbers


def test_3():
    expected_answer = 6
    current_answer = three_numbers(2, 2, 2)

    assert current_answer == expected_answer
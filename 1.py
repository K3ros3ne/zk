def find_divisible(max_number, divisor):
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return [number for number in range(1, max_number + 1) if number % divisor == 0]


def test_find_divisible():
    assert find_divisible(25, 5) == [5, 10, 15, 20, 25]
    assert find_divisible(9, 3) == [3, 6, 9]
    assert find_divisible(13, 2) == [2, 4, 6, 8, 10, 12]
    assert find_divisible(5, 10) == []
    
    try:
        find_divisible(10, 0)
    except ValueError as e:
        assert str(e) == "Divisor cannot be zero"

if __name__ == "__main__":
    max_number = int(input("Enter the maximum number (max_number): ")) 
    divisor = int(input("Enter the divisor: ")) 

    try:
        result = find_divisible(max_number, divisor) 
        print(f'Numbers divisible by {divisor} less than or equal to {max_number}: {result}')
    except ValueError as e:
        print(e)

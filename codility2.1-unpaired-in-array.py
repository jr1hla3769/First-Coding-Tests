def solution(A):
    result = 0
    for number in A:
        result = result ^ number
    return result

def test_solution():
    # Test case 1: Original example from the problem
    test1 = [9, 3, 9, 3, 9, 7, 9]
    print("Test 1: Basic case")
    print(f"Input: {test1}")
    print(f"Expected output: 7")
    print(f"Actual output: {solution(test1)}")
    print(f"Test 1 passed: {solution(test1) == 7}\n")

    # Test case 2: Minimal array with one element
    test2 = [5]
    print("Test 2: Single element array")
    print(f"Input: {test2}")
    print(f"Expected output: 5")
    print(f"Actual output: {solution(test2)}")
    print(f"Test 2 passed: {solution(test2) == 5}\n")

    # Test case 3: Array with large numbers
    test3 = [1000000000, 1000000000, 5]
    print("Test 3: Large numbers")
    print(f"Input: {test3}")
    print(f"Expected output: 5")
    print(f"Actual output: {solution(test3)}")
    print(f"Test 3 passed: {solution(test3) == 5}\n")

    # Test case 4: Alternating sequence with unpaired at end
    test4 = [1, 2, 1, 2, 3]
    print("Test 4: Alternating sequence")
    print(f"Input: {test4}")
    print(f"Expected output: 3")
    print(f"Actual output: {solution(test4)}")
    print(f"Test 4 passed: {solution(test4) == 3}\n")

    # Test case 5: Multiple pairs of same number
    test5 = [4, 4, 4, 4, 5]
    print("Test 5: Multiple pairs")
    print(f"Input: {test5}")
    print(f"Expected output: 5")
    print(f"Actual output: {solution(test5)}")
    print(f"Test 5 passed: {solution(test5) == 5}\n")

# Run the tests
test_solution()
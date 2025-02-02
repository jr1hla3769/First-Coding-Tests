def solution(X, Y, D):
    if X >= Y:
        return 0
    distance = Y - X
    jumps = (distance + D - 1) // D  # This is equivalent to math.ceil(distance / D)
    return jumps

# Example usage
X = 10
Y = 85
D = 30
print(solution(X, Y, D))  # Output: 3

def test_solution():
    # Test 1: Basic case where the frog needs to make some jumps
    print("\nTest 1: Basic case")
    x, y, d = 10, 85, 30
    result = solution(x, y, d)
    expected = 3
    print(f"Starting position: {x}")
    print(f"Target position: {y}")
    print(f"Jump distance: {d}")
    print(f"Expected jumps: {expected}")
    print(f"Actual jumps: {result}")
    print(f"Test passed: {result == expected}")
    print(f"Explanation: From 10 -> 40 -> 70 -> 85 (3 jumps)")

    # Test 2: When starting position equals target position
    print("\nTest 2: Already at target")
    x, y, d = 10, 10, 5
    result = solution(x, y, d)
    expected = 0
    print(f"Starting position: {x}")
    print(f"Target position: {y}")
    print(f"Jump distance: {d}")
    print(f"Expected jumps: {expected}")
    print(f"Actual jumps: {result}")
    print(f"Test passed: {result == expected}")
    print("Explanation: No jumps needed as we're already at the target")

    # Test 3: When one jump is exactly enough
    print("\nTest 3: Exact single jump")
    x, y, d = 10, 30, 20
    result = solution(x, y, d)
    expected = 1
    print(f"Starting position: {x}")
    print(f"Target position: {y}")
    print(f"Jump distance: {d}")
    print(f"Expected jumps: {expected}")
    print(f"Actual jumps: {result}")
    print(f"Test passed: {result == expected}")
    print("Explanation: One jump of 20 takes us exactly to target")

    # Test 4: When jump distance divides total distance with remainder
    print("\nTest 4: Distance with remainder")
    x, y, d = 1, 14, 3
    result = solution(x, y, d)
    expected = 5
    print(f"Starting position: {x}")
    print(f"Target position: {y}")
    print(f"Jump distance: {d}")
    print(f"Expected jumps: {expected}")
    print(f"Actual jumps: {result}")
    print(f"Test passed: {result == expected}")
    print("Explanation: Jumps go 1 -> 4 -> 7 -> 10 -> 13 -> 14 (5 jumps)")

    # Test 5: Large numbers
    print("\nTest 5: Large numbers")
    x, y, d = 1, 1000000000, 1
    result = solution(x, y, d)
    expected = 999999999
    print(f"Starting position: {x}")
    print(f"Target position: {y}")
    print(f"Jump distance: {d}")
    print(f"Expected jumps: {expected}")
    print(f"Actual jumps: {result}")
    print(f"Test passed: {result == expected}")
    print("Explanation: Testing with maximum possible values")

# Run all tests
test_solution()
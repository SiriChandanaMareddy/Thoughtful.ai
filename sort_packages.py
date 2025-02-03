def sort(width: int, height: int, length: int, mass: int) -> str:
    # Calculate volume
    volume = width * height * length
    
    # Determine if the package is bulky or heavy
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20
    
    # Determine the stack based on conditions
    return "REJECTED" if (is_bulky and is_heavy) else ("SPECIAL" if (is_bulky or is_heavy) else "STANDARD")

# Example Test Cases
def test_sort():
    assert sort(100, 100, 100, 10) == "STANDARD"
    assert sort(200, 50, 50, 10) == "SPECIAL"
    assert sort(100, 100, 100, 25) == "SPECIAL"
    assert sort(200, 200, 200, 30) == "REJECTED"
    assert sort(150, 150, 150, 19) == "SPECIAL"  # Edge case bulky but not heavy
    assert sort(149, 149, 149, 20) == "SPECIAL"  # Edge case heavy but not bulky
    assert sort(150, 150, 150, 20) == "REJECTED"  # Edge case both bulky and heavy
    assert sort(10, 10, 10, 5) == "STANDARD"  # Smallest possible package
    print("All test cases passed!")

# Run tests
test_sort()

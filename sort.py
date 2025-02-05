def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Determine the stack category
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"

if __name__ == "__main__":
    test_cases = [
        (100, 100, 99, 10),  # STANDARD (not bulky, not heavy)
        (200, 50, 50, 10),    # SPECIAL (one dimension >= 150)
        (50, 50, 50, 25),     # SPECIAL (heavy)
        (149, 149, 149, 19),  # SPECIAL (volume >= 1000000)
        (150, 100, 100, 10),  # SPECIAL (one dimension >= 150, volume >= 1000000)
        (200, 200, 200, 25),  # REJECTED (bulky and heavy)
        (151, 151, 151, 21),  # REJECTED (bulky and heavy)
    ]

    for w, h, l, m in test_cases:
        print(f"sort({w}, {h}, {l}, {m}) -> {sort(w, h, l, m)}")

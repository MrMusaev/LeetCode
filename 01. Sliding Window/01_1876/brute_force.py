def countGoodSubstrings(s: str):
    result = 0
    for i in range(len(s) - 2):
        first, second, third = s[i], s[i + 1], s[i + 2]
        if first == second:
            continue
        if first == third:
            continue
        if second == third:
            continue
        result += 1

    return result

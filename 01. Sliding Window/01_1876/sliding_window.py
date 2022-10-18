def countGoodSubstrings(s: str):
    k = 4
    if len(s) < k:
        return 0

    left, right = 0, 0
    chars = {}

    while right < k:
        right_char = s[right]
        chars[right_char] = chars[right_char] + 1 if right_char in chars else 1
        right += 1

    result = 1 if len(chars) == k else 0

    while right < len(s):
        left_char = s[left]
        right_char = s[right]

        chars[left_char] -= 1
        if chars[s[left]] == 0:
            del chars[s[left]]

        chars[right_char] = chars[right_char] + 1 if right_char in chars else 1

        if len(chars) == k:
            result += 1

        left += 1
        right += 1

    return result


s = input()
print(countGoodSubstrings(s))

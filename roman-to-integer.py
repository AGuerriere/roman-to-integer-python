def romanToInt(s):
    romanNumbers = {
        'I': 1,
        'V': 5,'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    n = len(s)
    i = n-1
    result = 0
    while i >= 0:
        if i < n-1 and romanNumbers[s[i]] < romanNumbers[s[i+1]]:
            result -= romanNumbers[s[i]]
        else:
            result += romanNumbers[s[i]]
        i -= 1
    return result

print(romanToInt("XXX"))
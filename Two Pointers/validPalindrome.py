def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    lower, upper = 0, len(s) - 1
    print(s)

    while lower < upper:
        if s[lower] != s[upper]:
            return False
        else:
            lower += 1
            upper -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
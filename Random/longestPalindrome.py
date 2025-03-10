def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    def expandAroundCenter(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    
    for i in range(len(s)):
        odd_pal = expandAroundCenter(i, i)
        even_pal = expandAroundCenter(i, i + 1)

        if len(odd_pal) > len(longest):
            longest = odd_pal
        if len(even_pal) > len(longest):
            longest = even_pal

    return longest


print(longestPalindrome("babad")) # 3

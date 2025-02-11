def removeOccurrences(s: str, part: str) -> str:
    start = 0
    end = start + len(part)

    while end <= len(s):
        if s[start: end] == part:
            s = s[:start] + s[end:]
            start = 0
            end = start + len(part)
        else:            
            start += 1
            end = start + len(part)
    
    return s


print(removeOccurrences('daabcbaabcbc', 'abc'))
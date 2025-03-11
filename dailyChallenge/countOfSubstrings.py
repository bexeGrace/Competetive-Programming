def countOfSubstrings(word: str, k: int) -> int:
    subCount = 0
    rig = 0
    lef = 0
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    fVowels = []
    while rig < len(word):
        if count == k and len(set(fVowels)) == len(vowels):
            subCount += 1
            if word[lef] in vowels:
                fVowels.remove(word[lef])
            else:
                count -= 1
            if rig + 1 < len(word) and word[rig] in vowels:
                continue
            lef += 1
        else:
            if count > k:
                if word[lef] in vowels:
                    fVowels.remove(word[lef])
                else:
                    count -= 1
                lef += 1
            else:
                if word[rig] in vowels:
                    fVowels.append(word[rig])
                else:
                    count += 1
                rig += 1
            if count == k and len(set(fVowels)) == len(vowels):
                subCount += 1
                if word[lef] in vowels:
                    fVowels.remove(word[lef])
                else:
                    count -= 1
                if rig + 1 < len(word) and word[rig] in vowels:
                    continue
                lef += 1
    return subCount

print(countOfSubstrings("abcouidef", 3)) # 2
# print(countOfSubstrings("ieaou", 0)) # 0
# print(countOfSubstrings("aeiou", 3)) # 1
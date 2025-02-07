def isValid(s: str):
    his = []
    curr = None
    fronts = ['(', '{', '[']
    backs = [')', '}', ']']

    for i in range(len(s)):
        his.append(s[i])
        if len(his) == 0:
            curr = None
        elif s[i] in backs and s[i] != curr:
            return False
        elif s[i] in backs and s[i] == curr:
            del his[-1]
            del his[-1]
            if len(his) == 0:
                curr = None
            else:
                curr = backs[fronts.index(his[-1])]                
        else:
            if s[i] == '(':
                curr = ')'
            elif s[i] == '{':
                curr = '}'
            elif s[i] == '[':
                curr = ']'
    if len(his):
        return False            
    return True
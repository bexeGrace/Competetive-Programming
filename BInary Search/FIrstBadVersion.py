def firstBadVersion(self, n, targ):
    """
    :type n: int
    :rtype: int
    """
    start = 1
    end = n
    bad = -1

    while start < end:
        mid = ((start + end) // 2) + 1
        if isBadVersion(mid, targ):
            bad = mid
            end = mid - 1
        else:
            start = mid + 1
    return bad 


def isBadVersion(num, tar):
    return num == tar


print(firstBadVersion('self', 2, 2))
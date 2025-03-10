from typing import List

def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    rows, cols = len(img), len(img[0])
    res = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            count = 0
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if 0 <= r < rows and 0 <= c < cols:
                        res[i][j] += img[r][c]
                        count += 1
            res[i][j] //= count
    
    return res



print(imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])) # [[0,0,0],[0,0,0],[0,0,0]]
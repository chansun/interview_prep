# Time: O(lg N)
# Space: O(lg N)

def mult(s, l):
    if s == 0:
        return 0
    if s == 1:
        return l
    if s % 2 == 0:
        half = s // 2 ## divide by 2 through bit shift
        return mult(half, l) + mult(half, l)
    s -= 1
    half = s // 2
    return mult(half, l) + mult(half, l) + l
    
print(mult(5000,3))
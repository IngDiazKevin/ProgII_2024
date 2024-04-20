def is_triangulo(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True 

print(is_triangulo(1,1,1))
print(is_triangulo(1,1,10))
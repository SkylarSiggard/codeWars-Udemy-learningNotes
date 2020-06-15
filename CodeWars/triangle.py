#to check if the lenth of sides can make a triangle
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if (a + b) > c and (b + c) > a and (c + a) > b:
            return True
        else: 
            return False 
    else:
        return False
    

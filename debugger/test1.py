def get_area(v1, v2):
    return v1 + v2
def main():
    height = 9
    width = 19
    area = get_area(width, height)
    test_fun("e")
    print("Area:", area)
    return area

def test_fun(str1):
    t = "t"
    for i in range(10):
        t += str1+str(i)
    return str1 + "test"+t
    
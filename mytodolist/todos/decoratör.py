def aspect(func):
    print("çalışıyorum")
    func()
    print("durdum")

@aspect
def toplama():
    a=3
    b=2
    c = a + b
    return print(c)  
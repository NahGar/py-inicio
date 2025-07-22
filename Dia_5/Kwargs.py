
def suma(num1,num2,*args,**kwargs):

    print("Tipo args:",type(args))
    print("Tipo kwargs:",type(kwargs))
    print("Num1:", num1)
    print("Num2:", num2)

    total = num1 + num2 + sum(args)

    for arg in args:
        print(f"Arg: {arg}")

    for key, value in kwargs.items():
        print(f"{key} = {value}")
        total += value
    return  total

print(suma(2,3, 1,2,3, x=5, y=6, z=7))

args = [1, 2, 3, 4, 5]
kwargs = {'x': 5, 'y': 6, 'z': 7}
print(suma(2,3, *args, **kwargs))

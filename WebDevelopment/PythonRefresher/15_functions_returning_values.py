def add(x, y ):
    print(f"{x} + {y} = {x + y}")
    return (x + y)

results =  add(5, 10)
print(results)

#########################
a = 10
 
def my_function(param_1=a):
    print(param_1)
 
a = 20
my_function()
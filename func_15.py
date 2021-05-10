## Positional - Only Arguments(Available Only From Python 3.8)

def positionalArguments(a, b, c, /, d, e):
    print("Positional Arguments:")
    print("a:{}, b:{}, c:{}, d:{}, e:{}".format(a, b, c, d, e))


## before the slash it will take only positional arguments

positionalArguments(1, 2, 3, d=4, e=5)

# positionalArguments(a=1, 2, 3, 4, 5)  ## error ==>  Positional argument should not followa keyword arguments

positionalArguments(a=1, b=2, c=3, d=4, e=5)   ## Arguments before the slash should be passed only via position and not
                                                                                                          # via keyword

positionalArguments(1, 2, 3, 4, e=5)

#positionalArguments(1, 2, 3, d=4, 5)   ## error ==> Positional argument should not followa keyword arguments
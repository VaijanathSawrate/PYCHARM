def namedArgumentFunction(a, b, c):
    print("a: {}, b: {}, c: {}".format(a, b, c))


namedArgumentFunction(2, 3, 4)   ## Positional argument
namedArgumentFunction(a = 100, b = 200, c = 300)  ## Keyword Argument
#namedArgumentFunction(101, a = 102, c = 103)   ## TypeError: namedArgumentFunction() got multiple values for argument 'a'
#namedArgumentFunction(a = 101, 102, c = 103)    ## SyntaxError: positional argument follows keyword argument
namedArgumentFunction(101, b = 102, c = 103)  ## Mix of position and name  # no error

## positional argument should be preceeding the keyword argument.
def namedArgumentFunction(a, b, c):
    print("The values are a:{}, b{}, c: {}".format(a, b, c))


namedArgumentFunction(100, 200, 300)  ## Positional argument
namedArgumentFunction(c = 30, b = 20, a = 10)  ## Named arguments
namedArgumentFunction(101, a = 102, b = 103)    ## Mix of position and name  # error
namedArgumentFunction(b=600, 500, c=103)       ## positional argument after named argument gives an erro
namedArgumentFunction(101, b=102, c=103)     ## Mix of position + Name
namedArgumentFunction((a=600, 500, c=900))    ## positional argument after named argument gives an erro

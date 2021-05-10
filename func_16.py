## Position + Keyword - Only Arguments (Available only from 3.8)

def PositionalKeywordArguments(a, b, /, c, x, *, y, z):  ## Arguments after the star(*) only passed via keyword
    print("Positional + Keyword , Arguments : ")
    print("a:{}, b:{}, c:{}, x:{}, y:{}, z:{}".format(a, b, c, x, y, z))


## PositionalKeywordArguments(1, 2, 3, 4, 5, 6)   ## Error

PositionalKeywordArguments(1, 2, 3, 4, y=5, z=6)

PositionalKeywordArguments(1, 2, c=3, x=4, y=5, z=6)

## PositionalKeywordArguments(a=1, b=2, c=3, x=4, y=5, z=6) ## Error
                               ## Arguments before slash should be passed via position and after * should be passed via keyword
                               ## AND general rule is positional args preceeds the keyword args.


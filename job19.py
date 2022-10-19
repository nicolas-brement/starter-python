def myFunction(*args):
    args = list(args)
    r=[]

    while args:
        mini=args[0]
        for x in args:
            if x < mini:
                mini=x
        args.remove(mini)
        r.append(mini)
    return r

print(myFunction(17,7,91,12,1,13,4,12,18))
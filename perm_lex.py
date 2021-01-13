def perm_gen_lex(a):
    if len(a) == 0:
        string_list = []
    elif len(a) == 1:
        string_list = [a]
    else:
        for char in a:
            new_a = a[1:]
            perm_gen_lex(new_a)

 
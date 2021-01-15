# string list -> string list
# generates a list of all the permutations of a given string
def perm_gen_lex(a):
    final_perm_list = []
    if len(a) == 0:
        final_perm_list = []
    elif len(a) == 1:
        return [a]
    else:
        n = 0
        while n < len(a):
            new_a = a[:n] + a[n + 1:]
            #print(new_a)
            char = a[n]
            perm_list = perm_gen_lex(new_a)
            n += 1
            i = 0
            while i < len(perm_list):
                perm_list[i] = char + perm_list[i]
                i += 1
            final_perm_list = final_perm_list + perm_list
    return final_perm_list

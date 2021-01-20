# string list -> string list
# generates a list of all the permutations of a given string
def perm_gen_lex(a):
    final_perm_list = []        # list to put all permutations in
    if len(a) == 0:             # base case
        final_perm_list = []
    elif len(a) == 1:           # base case
        return [a]
    else:
        n = 0
        while n < len(a):                       # iterate through every letter
            new_a = a[:n] + a[n + 1:]           # create new string without letter
            char = a[n]                         # store letter that we're on
            perm_list = perm_gen_lex(new_a)     # call recursive function with new string
            n += 1
            i = 0
            while i < len(perm_list):
                perm_list[i] = char + perm_list[i]      # add character taken out to every partial permutation
                i += 1
            final_perm_list = final_perm_list + perm_list   # combine permutation strings
    return final_perm_list

__author__ = 'frankdrevin'


def get_calc(n, b):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"

    b += 0.0  # Convert
    b /= 100.  # Shift two decimals to the left
    n -= n * b
    print("%d" % n)


#get_calc(1000, 25)

def sort_locations(a, b, c):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    lst = [a, b, c]
    lst.sort()

    print("%d %d %d" % (lst[0], lst[1], lst[2]))


#sort_locations(40, 90,10)



def remove_stopwords(query, stopwords):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    lst = []
    lst.extend(query)
    for sw in stopwords:  # Keyword to search for
        while sw in lst:  # Keep pruning
            lst.remove(sw)
    for out in lst:
        print(out)


#query = ["episode","of","the","new","season","of","the","comedy","show"]
#stopwords =["the", "of"]
#remove_stopwords(query,stopwords)

def tokenize_query(query, punctuation):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    new_q = query
    for i in punctuation:
        new_q = new_q.replace(i, "\n")  # Replace all
    new_q = new_q.split()  # Default delimiter for split is whitespace or \n
    for nw in new_q:
        print(nw)


#tokenize_query("car? dealer?s! bmw, audi", "?!")


def token_stemming(tokens, suffixes):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    lst = []  # Empty list
    lst.extend(tokens)
    b_lst = [False] * len(lst)  # Init to Boolean false and to the size of lst, keep track of edits

    sorted_suf = []
    sorted_suf.extend(suffixes)
    sorted_suf.sort(key=len, reverse=True)  # Pass in length as key to sort with, reverse to Descending order
    for s in sorted_suf:  # Check each suffix against the tokens, to be thorough (Bigger suffixes get priority)
        for i in range(len(lst)):  # Check each string in list
            if b_lst[i] is False and lst[i].endswith(s):  # If it hasn't been edited and it ends with
                index = lst[i].rfind(s)  # Suffixes should be found from the end-forward
                lst[i] = lst[i][0:index]  # Splice the end
                b_lst[i] = True  # Has been edited

    for w in lst:
        print(w)


#lst = ["episode", "of", "the", "third", "season", "of", "the", "animated", "comedy", "series"]
#suffixes = ["e", "rd", "f", "dy", "es"]
#token_stemming(lst,suffixes )



def count_configurations(a, b, c, n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    lst = [a, b, c]
    i = 0
    combos = 0
    while True:
        curr = lst[i]

        if curr < n: # If less than max

        else: # Curr is equal or greater, we hit capacity



        i+=1 # Postfix
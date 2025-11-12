l = [5,4,3] # this should return 4

# Solution one, not good uses O(n^2) and requires sort
def find_h_index(l):
    h = -1
    for i in range(len(l)):
        counter = 1
        for j in range( i+ 1, len(l)):
            print(f"current i:{l[i]}, current j: {l[j]}")
            if l[j] >= l[i]:
                counter+=1
                print(f"counter:{counter}")
                if counter > l[i]:
                    break

        if counter == l[i]:
            if counter > h:
                h = counter
            print(f"h : {h}")

    return h
# Honestly, a better solution than the book
def new_h_index_finder(articles : list[int]) -> int:
    articles.sort()
    n = len(articles)
    current = None
    for i in range(n):
        if articles[i] == current:
            continue
        else:
            current = articles[i]
            if (len(articles) - i) == current:
                return current
    return -1



print(new_h_index_finder(l))






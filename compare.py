def compare_lists(x, y):
    for number in range(len(x)):
        if x[number] != y[number]:
            print "Not the same"
        else:
            print "Same"

compare_lists([1,2,3,4], [1,"hi",3,4])

# Compares list and see if they are the same
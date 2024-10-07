beg = 1

end = 2

curr = end

for r in range(1, 8):

    for c in range(beg, end):

        curr -= 1

        print(curr, end=' ')

    print("")

    beg = end

    end += r

    curr = end

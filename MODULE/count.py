def count():
    print()
    input1 = input('DO YOU WANT TO COUNT THE NUMBER EITHER ASCENDING OR DESCENDING: ').upper()
    print()
    a1 = int(input('ENTER THE STARTING NUMBER: '))
    print()
    a2 = int(input('ENTER THE ENDING NUMBER: '))
    print()
    if input1 == 'ASCENDING' or input1 == 'ASCENDING ORDER' or input1 == '0':
        if a1 < a2:
            count1 = 0
            ts = ''
            for i1 in range(a1, a2 + 1):
                ts = ts + str(i1) + ', '
                print(i1, end=', ')
                count1 += 1
                if count1 == 5:
                    print()
                    count1 = 0
                    continue
                else:
                    continue
            return ts
            print()
        elif a1 > a2:
            count1 = 0
            ts = ''
            for i1 in range(a2, a1 + 1):
                ts = ts + str(i1) + ', '
                print(i1, end=',')
                count1 += 1
                if count1 == 5:
                    print()
                    count1 = 0
                    continue
                else:
                    continue
            return ts
            print()
        elif a1 == a2:
            print(a1)
            return a1
        print()
    if input1 == 'DESCENDING' or input1 == 'DESCENDING ORDER' or input1 == '1':
        if a1 < a2:
            count1 = 0
            ts = ''
            for i1 in range(a2, a1 - 1, -1):
                ts = ts + str(i1) + ', '
                print(i1, end=',')
                count1 += 1
                if count1 == 5:
                    print()
                    count1 = 0
                else:
                    continue
            return ts
            print()
        elif a1 > a2:
            count1 = 0
            ts = ''
            for i1 in range(a1, a2 - 1, -1):
                ts = ts + str(i1) + ', '
                print(i1, end=',')
                count1 += 1
                if count1 == 5:
                    print()
                    count1 = 0
                else:
                    continue
            return ts
            print()
        elif a1 == a2:
            print(a1)
            return a1
        print()
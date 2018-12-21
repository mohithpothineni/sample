
sudoku = input()
check= [False]*9
if '.' not in sudoku:
    print("Given sudoku is solved")
elif len(sudoku) != 81:
    print("Invalid input")
else:
    count = 0
    i = ''
    for i in sudoku:
        if count == 9:
            # print(check)
            for j in range(9):
                if check[j] == False:
                    print(j+1)
            check = [False]*9
            # print(check)
            count = 0
        #   count = count + 1
        #   if(i == '.'):
        #       continue
        #   check[int(i) - 1] = True
        # else:
        count = count + 1
        if(i == '.'):
            continue
        check[int(i) - 1] = True
    if count == 9:
            # print(check)
            for j in range(9):
                if check[j] == False:
                    print(j+1)
            check = [False]*9
            # print(check)
            count = 0


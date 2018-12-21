'''Solution for possibilities in sudoku'''



def check(sudoku):
    if (sudoku.count('.') == 0):
        return 'Given sudoku is solved'

    elif(len(sudoku) != 81):
        return 'Invalid input'

    else:
        collection_rows = []
        for i in range(0,len(sudoku),9):
            row_ = [int(j) for j in sudoku[i:i+9] if j != '.']
            set_row = {k for k in row_}
            if len(row_) != len(set_row):
                return 'Invalid Sudoku:Duplicate values'
            elif collection_rows.count(row_) == 1:
                return 'Invalid Sudoku:Duplicate values'
            else:
                collection_rows.append(row_)
        return ''

def possiblities(sudoku):
    check= [False]*9
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


def main():
    sudoku_ = input()
    check_result = check(sudoku_)
    if check_result != '':
        print(check_result)
        return
    possiblities(sudoku_)
        


if __name__ == "__main__":
    main()


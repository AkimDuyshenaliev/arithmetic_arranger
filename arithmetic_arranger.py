

def arithmetic_arranger(x, *args):

    result = []
    subLists = []

    for i in range(len(x)):
        if '+' in x[i]:
            plusSplit = x[i].split(sep="+")
            plusSplit = int(plusSplit[0]) + int(plusSplit[1])
            result.append(plusSplit)

            plusTempLists = x[i].split(sep=" ")
            subLists.append(tuple(plusTempLists))

            if len(plusTempLists[0]) > 4 or len(plusTempLists[2]) > 4:
                print("Error: Numbers cannot be more than four digits.")
                return

        elif '-' in x[i]:
            minusSplit = x[i].split(sep="-")
            minusSplit = int(minusSplit[0]) - int(minusSplit[1])
            result.insert(i, minusSplit)

            minusTempLists = x[i].split(sep=" ")
            subLists.append(tuple(minusTempLists))

            if len(minusTempLists[0]) > 4 or len(minusTempLists[2]) > 4:
                print("Error: Numbers cannot be more than four digits.")
                return
        else:
            print("Error: Operator must be '+' or '-'.")
            return


    line = '-----'
    distance = '   '
    if args and args[0] == True:
        for i in range(len(result)):
            for j in range(len(subLists)):
                if i == 0:
                    print(f"{subLists[j][i]:>{5}}{distance}", end="")
                elif i < (len(result)-1):
                    try:
                        print(f"{subLists[j][i]:<{1}}{subLists[j][i+1]:>{4}}{distance}", end="")
                    except:
                        print(f"{line}{distance}", end="")
                else:
                    print(f"{result[j]:>{5}}{distance}", end="")
            print(end='\n')
    else:
        for i in range(len(result)):
            for j in range(len(subLists)):
                if i == 0:
                    print(f"{subLists[j][i]:>{5}}{distance}", end="")
                elif i < (len(result) - 1):
                    try:
                        print(f"{subLists[j][i]:<{1}}{subLists[j][i + 1]:>{4}}{distance}", end="")
                    except:
                        print(f"{line}{distance}", end="")
            print(end='\n')
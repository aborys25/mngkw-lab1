import re
import csv


def readCSV() ->list :
    column1 = []
    column2 = []

    with open("details.csv", "r", encoding="utf-8") as file:
        csv_read = csv.reader(file)
        for line in csv_read:
            column1.append(line[0])
            column2.append(line[1])

    return column1, column2


# test
def saveCSV(result:list, file: str):
    rows = zip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
               result[9])

    with open(file, 'w', newline="", encoding='utf-8') as write:
        writeToFile = csv.writer(write)

        for row in rows:
            writeToFile.writerow(row)


def checkRegex(expression, whichcolumn):
    finalcolumn = []
    for column in whichcolumn:
        check = re.search(expression, column)
        if check is None:
            finalcolumn.append("")
        else:
            finalcolumn.append(check.group(0))

    return finalcolumn


def column3(columnIn):
    expression3 = '((nr \d*)|(no\W \d* \w\W)|(No\W \d* \w\W)|(num\W \d* \w\W)|(iss\W \d* \w\W))'
    expression3version2 = '(\d*)\d'
    column3version1 = checkRegex(expression3, columnIn)
    return checkRegex(expression3version2, column3version1)


def column4(columnIn):
    expression4 = '((vol\W \d*\W)|(^t\W \d*,)|(Vol\W \d*)|( (^T|t)\W \d*\w)|(T\W \d* \w\W)|(T\W \d*\W))'
    column4version1 = checkRegex(expression4, columnIn)
    expression4version2 = '(\d*)\d'
    return checkRegex(expression4version2, column4version1)


def column5(columnIn):
    expression5 = 'e\d*\d'
    return checkRegex(expression5, columnIn)


def column6(columnIn):
    expression6 = '\d(\d*-\d*)\d'
    return checkRegex(expression6, columnIn)


def column7(columnIn):
    expression7 = '(	| )(\d*) (s)(\W)'
    column7version1 = checkRegex(expression7, columnIn)
    expression7version2 = '\d(\d*)'
    return checkRegex(expression7version2, column7version1)


def column8(columnIn):
    expression8 = '(: )((\w*\ )*)(\w*,)'
    column8version1 = checkRegex(expression8, columnIn)
    expression8version2 = '\w\w*(.)*(\w)'
    return checkRegex(expression8version2, column8version1)


def column9(columnIn):
    expression9 = '^(\w*)'
    return checkRegex(expression9, columnIn)


def column10(columnIn):
    expression10 = '(\d\d\d\d)'
    return checkRegex(expression10, columnIn)


def main():
    columns = readCSV()

    saveCSV([columns[0], columns[1], column3(columns[1]), column4(columns[1]), column5(columns[1]), column6(columns[1]),
             column7(columns[1]), column8(columns[0]), column9(columns[0]), column10(columns[0])], 'test.csv')


if __name__ == "__main__":
    main()

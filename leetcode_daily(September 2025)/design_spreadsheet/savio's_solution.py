class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0 for i in range(26)] for i in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        column = ord(cell[0]) - ord("A")
        row = int(cell[1:])
        self.sheet[row][column] = value

    def resetCell(self, cell: str) -> None:
        column = ord(cell[0]) - ord("A")
        row = int(cell[1:])
        self.sheet[row][column] = 0

    def getValue(self, formula: str) -> int:
        components = formula[1:].split("+")
        left_operand, right_operand = components[0], components[1]

        if left_operand.isdigit() and right_operand.isdigit():
            return int(left_operand) + int(right_operand)

        elif left_operand.isdigit() and not right_operand.isdigit():
            column = ord(right_operand[0]) - ord("A")
            row = int(right_operand[1:])
            value = int(self.sheet[row][column])
            return int(left_operand) + value

        elif not left_operand.isdigit() and right_operand.isdigit():
            column = ord(left_operand[0]) - ord("A")
            row = int(left_operand[1:])
            value = int(self.sheet[row][column])
            return int(right_operand) + value
        else:
            column1 = ord(right_operand[0]) - ord("A")
            row1 = int(right_operand[1:])
            value1 = int(self.sheet[row1][column1])

            column2 = ord(left_operand[0]) - ord("A")
            row2 = int(left_operand[1:])
            value2 = int(self.sheet[row2][column2])
            return value1 + value2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

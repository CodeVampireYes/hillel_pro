class BinaryNumber:
    """
    Клас представляє двійкове число та надає методи для виконання побітових операцій:
    AND, OR, XOR, NOT.

    Атрибути:
    ----------
    binary : int
        Двійкове число, яке зберігається як ціле число (int).

    Методи:
    ----------
    __and__(other: BinaryNumber) -> BinaryNumber:
        Виконує побітову операцію AND.

    __or__(other: BinaryNumber) -> BinaryNumber:
        Виконує побітову операцію OR.

    __xor__(other: BinaryNumber) -> BinaryNumber:
         Виконує побітову операцію XOR.

    __invert__() -> BinaryNumber:
        Виконує побітову операцію NOT.

    __eq__(other: BinaryNumber) -> bool:
        Перевіряє рівність двох двійкових чисел.
       """

    def __init__(self, binary):
        self.binary = binary

    def __and__(self, other: "BinaryNumber") -> "BinaryNumber":
        return BinaryNumber(self.binary & other.binary)

    def __or__(self, other: "BinaryNumber") -> "BinaryNumber":
        return BinaryNumber(self.binary | other.binary)

    def __invert__(self) -> "BinaryNumber":
        return BinaryNumber(~self.binary)

    def __xor__(self, other: "BinaryNumber") -> "BinaryNumber":
        return BinaryNumber(self.binary ^ other.binary)

    def __eq__(self, other: "BinaryNumber") -> bool:
        return self.binary == other.binary


bin_num1 = BinaryNumber(0b10001010101010)
bin_num2 = BinaryNumber(0b11111)
bin_num3 = BinaryNumber(0b11000000000000000)
bin_num4 = BinaryNumber(0b1)
bin_num5 = BinaryNumber(0b0)
assert bin_num5 & bin_num4 == BinaryNumber(0b0), "Test1"
assert bin_num5 | bin_num4 == BinaryNumber(0b1), "Test2"
assert bin_num1 ^ bin_num2 == BinaryNumber(0b10001010110101), "Test3"
assert bin_num1 ^ bin_num3 == BinaryNumber(0b11010001010101010), "Test4"
print("OK")

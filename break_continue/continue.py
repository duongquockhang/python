class Number:

    num = 10

    def __init__(self, num):

        self.num = num

        print(self.num, end='')

    def __del__(self):

        print(self.num+1)

n = Number(20)
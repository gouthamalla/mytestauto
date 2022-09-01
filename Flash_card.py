
class Flash_card:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
        self.complete_data =  {}

    def logic_1(self):
        print('Welcome to flash card application')
        word = input('Enter the word: ')
        meaning = input('Enter the meaning: ')
        data = {}
        data[word] = meaning
        self.complete_data[word] = meaning
        print(data)

    def logic_2(self):
        n = 0
        while n < 5:
            print('Enter 1 if you want to add another word')
            print('Enter 2 if you want to view the saved words')
            print('Enter 0 if you want to Quit')
            count = int(input())
            if type(count) is int:
                if count == 0:
                    print ('Quitting the flash card application')
                    break
                elif count == 1:
                    self.logic_1()
                elif count == 2:
                    print(self.complete_data)
                else:
                    print('You can choose only between 0 and 1')
                n += 1
            else:
                print('Enter only int between 0, 1 & 2')
        if n == 5:
            print('The saved words are as below', self.complete_data)

ob = Flash_card('word', 'meaning')
ob.logic_2()

def split_even_odd_numbers(list):
    evenNumbers = []
    oddNumbers = []
    for i in range(len(list)):
        if i % 2 == 0:
            evenNumbers.append(list[i])
        else : 
            oddNumbers.append(list[i])
    return (evenNumbers,oddNumbers)


# print(split_even_odd_numbers([1, 2, 3]))
             
def countWords(sentence):
    words = sentence.split(" ")
    wordsWithoutRepitition = []
    for word in words:
        if word not in wordsWithoutRepitition:
            wordsWithoutRepitition.append(word)
    return len(wordsWithoutRepitition)


# print(countWords("ayoub ayoub alaoui"))


def printUntilInput():
    number = int(input("please input a number"))
    for i in range(number+1):
        print(i) 
    
    
# printUntilInput()

def inputDividorsRange(input1, input2):
    for i in range(1, input1):
        if input2 % i == 0:
            print(i)


# inputDividorsRange(20, 200)
    


def inputDividorsInRange100(input1, input2):
    for i in range(1, 100):
        if input1 % i == 0 and input2 % i == 0:
            print(i)
            
# inputDividorsInRange100(20, 30)


# all these functions using the oop


class Game:
    
    def __init__(self):
        while(True):
            print("please select a number")
            print("1: split even odd numbers")
            print("2: count words")
            print("3: print until input")
            print("4: inputDividorsRange")
            print("5: inputs dividors in a  range 100")
            print("x to quit")
            self.numberSelected = int(input(""))
            if(self.numberSelected == 1):
                self.list= []
                while True:
                    userInput = input("please type a number or x to quit")
                    if userInput == "x":
                        break
                    else:
                        self.list.append(int(userInput))
                print(self.split_even_odd_numbers(self.list))
                
            elif(self.numberSelected == 2):
                self.sentence = input("please type a sentence")
                print(self.countWords(self.sentence))
            elif(self.numberSelected == 3):
                self.printUntilInput()
            elif(self.numberSelected == 4):
                self.range = int(input("please input the range"))
                self.number = int(input("please type the number"))
                print(self.inputDividorsRange(self.range, self.number))
            elif(self.numberSelected == 5):
                self.input1 = int(input("please type the first number"))
                self.input2 = int(input("please type the second number"))
                print(self.inputDividorsInRange100(self.input1, self.input2))
            elif(self.numberSelected == "x"):
                break
            else:
                print("please select a valid choice")
                
                
            if(self.numberSelected in [1, 2, 3, 4, 5]):
                self.choice = input("yes to play again no to exit ")
                if(self.choice == "yes"):
                    continue
                else:
                    break
                
                
                
                   
                   
                   
                
                # print("please input a list")
                # list_numbers = list(input(""))
                # self.split_even_odd_numbers(self.numberSelected)
           
                  
    def split_even_odd_numbers(self, list):
        evenNumbers = []
        oddNumbers = []
        for i in range(len(list)):
            if i % 2 == 0:
                evenNumbers.append(list[i])
            else : 
                oddNumbers.append(list[i])
        return (evenNumbers,oddNumbers)

             
    def countWords(self, sentence):
        words = sentence.split(" ")
        wordsWithoutRepitition = []
        for word in words:
            if word not in wordsWithoutRepitition:
                wordsWithoutRepitition.append(word)
        return len(wordsWithoutRepitition)




    def printUntilInput(self):
        number = int(input("please input a number"))
        for i in range(number+1):
            print(i) 
    
    

    def inputDividorsRange(self, input1, input2):
        for i in range(1, input1):
            if input2 % i == 0:
                print(i)


    


    def inputDividorsInRange100(input1, input2):
        for i in range(1, 100):
            if input1 % i == 0 and input2 % i == 0:
                print(i)
            
            



game = Game()
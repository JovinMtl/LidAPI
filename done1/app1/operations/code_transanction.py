"""I want to make a transaction code of 12 caracters"""

from random import choice

# from ..models import Recharge
from ..models import OperationStore


class GenerateCode:
    """Generate a code and inscript in a table of codes that have been
    used successfully with the object(request) of that transaction
    
    It will require the object(Request model) as a parameter
    
    we need to import that model of Codes"""

    def __init__(self, high=12) -> None:
        self.input1 = [x for x in range(10)]
        self.input2 = ['a','A','b','B','c','C','d','D','e','E','f','F',
                       'j','J','k','K','l','L','m','M','n','o','O',
                       'p','P','r','R','s','S','t','T','u','U','v','V',
                       'w','W','x','X','y','Y','z','Z',
                       ]
        self.choices = []
        self.code = ""
        self.max = high
    
    def gene(self):
        """This one is super dynamic"""
        options = [1, 2, 3]
        self.choices = []
        inputs = [self.input1, self.input2]
        
        while len(self.choices) < self.max:
            opt1 = choice(options)
            input1 = choice(inputs)
            for _ in range(opt1):
                choice1 = choice(input1)
                self.choices.append(choice1)
            opt2 = choice(options)
            input2 = choice(inputs)
            for _ in range(opt2):
                choice2 = choice(input2)
                self.choices.append(choice2)
        for element in self.choices[:self.max]:
                self.code += str(element)
        print(f"The length is {len(self.code)} / {self.max}")
        return self.code
    

    def giveCode(self):
        worth = True
        while worth:
            current_code = self.gene()
            try:
                verify = OperationStore.objects.get(code=current_code)
            except OperationStore.DoesNotExist:
                worth = False
            else:
                worth = True
        return current_code

"""I want to make a transaction code of 12 caracters"""

from random import choice

# from ..models import Recharge


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
        # self.last_uid = Recharge.objects.last()
    
    

    # def generate(self, table):
    #     worth = True
    #     while worth:
    #         for _ in range(2):
    #             for _ in range(2):
    #                 choice1 = choice(self.input1)
    #                 self.choices.append(choice1)
    #             for _ in range(3):
    #                 choice2 = choice(self.input2)
    #                 self.choices.append(choice2)
    #             choice1 = choice(self.input1)
    #             self.choices.append(choice1)
    #         for element in self.choices:
    #             self.code += str(element)
            
    #         if table == 'recharge':
    #             try:
    #                 obj = Recharge.objects.get(code_transaction=self.code)
    #             except Recharge.DoesNotExist:
    #                 worth = False
    #                 return self.code
    #             else:
    #                 worth = True
    
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
    
    # def genUid(self):
    #     last_uid = self.last_uid.id
    #     current_uid = last_uid + 1
    #     self.last_uid -= 1
    #     return current_uid
    


# jov = GenerateCode()
# code = jov.genUid()
# print(f"THe code generated is:\n{code}")
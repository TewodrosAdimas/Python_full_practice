

''' 
    class Dwellers
        methode user    (id, name, gender, city)                                
    

    child class Bank                                                             #Inheritance
            methode user_info (name, gender, city, account_num)                  #nested list
            methode withdraw                                                     #setter and getter
            methode deposite                                                     #setter and getter
            private methode balance (account_balance)                            #encapsulation
            private variable account_balance                                     #encapsulation
            methode new (to create new account)                                  #polymorphism
            methode view                                                        

    child class Parent_list 
            methode family_member                                       #Dictionary nested list nested tupple
            methode view                                                #Polymorphisem        
  
    Polymorphisem---- the same function for different pupose ex- define a fun with parameter, then that
                      parameter calls different function/class for different parameters (inside those class 
                      you should have functions with the same name)

    Abstract ------- abstract classes have abstract methode, so every child class which inheritted from 
                    abstract class should implement every abstract methodes 
                -- enter password to login
                --- abstract class Login 
                --- abstract methode authentication  


'''
from abc import ABC, abstractclassmethod
class Login(ABC):
        @abstractclassmethod
        def __init__(self, password):
                self.password = password
                if self.password == "123":
                        print("Success full log in")
                        pass
                else:
                        print("wrong password")
                        exit()

dwellers = {"012": [{"name": "Abebe"}, {"gender": "male"}, {"city": "dego"}], 
            "013": [{"name": "Almaz"}, {"gender": "female"}, {"city": "markos"}],
            "014": [{"name": "Kebede"}, {"gender": "male"}, {"city": "addis ababa"}]}


class Dwellers():
        def __init__(self,name,gender,city):
                self.name = name
                self,gender = gender
                self.city = city


class Bank(Dwellers):
        def __init__(self, name, gender, city, accNum):
                super().__init__(name, gender, city)
                self.accNum = accNum

        def __acc_balance(self):
                self.__balance= 0
        
        def withdraw(self, amount):
                amount = self.amount
                if self.__balance>= self.amount :
                        self.balance = self.__balance - amount
                        return self.__balance
                else:
                        msg = (f"In sufficient balance your balance is ${self.__balance}")
                        return msg

        def deposite(self, amount):
                amount = self.amount
                self.__balance = amount + self.__balance
                return self.__balance
        
        def viw(self):
                print(f"{self.name} has ${self.__balance}")
        

class ParentList(Dwellers):
        def __init__(self, name, gender, city):
                super().__init__(name, gender, city)
                member = [name]

                def addMembe(self,son, doughter):
                        member.append(son)
                        member.append(doughter)

        
        def view(self):
                print(self.member)






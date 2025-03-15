class Back:
    def create(self):
        self.acc_no = int(input("Enter of Account Number : "))
        self.name = input("Enter of Name :")
        self.bal = int(input("Enter of Minimun Deposit Must Be 2000: "))
        if self.bal < 2000:
            self.bal = int(input("Enter of Minimun Deposit Must Be 2000: "))
            if self.bal < 2000:
                print("Try agin ")
                return False
        return True
                

    def show_account(self,acc=False):
        if self.acc_no == acc:
            print(f"\t{self.acc_no}\t\t{self.name}\t\t{self.bal}")
        if acc==False:
             print(f"\t{self.acc_no}\t\t{self.name}\t\t{self.bal}")        

    def deposit_amount(self,acc):
        if self.acc_no == acc:
            deposit = int(input("Enter of Deposit Aumout :"))
            if deposit > 1000:
                print("Minumun Deposit is 1000 Try Again")
                return
            self.bal +=deposit
            print("Account Details")
            print(ti)
            self.show_account(self.acc_no)
            
    def with_drow(self,acc):
        if self.acc_no == acc:
            withdrow = int(input("Enter of With Drow Aumonut : "))
            if self.bal - withdrow < 2000:
                print("Minumun Balance is required in 2000 Try Again ")
                return
            self.bal -= withdrow



print("""
                            WelCome to Back
                1.  Open Account
                2.  Show Account
                3.  Deposit Amount
                4.  Withdrow Amount
                5.  Exit

""")

ti = "\n\n\tAccount\t\tName\t\tBalance"

listBack = []
while True:
    num = int(input("Enter of Choice Number : "))    
    match num:
        case 1:
            acc = int(input("Enter of Total Account : "))
            for i in range(acc):
                b = Back()
                if b.create():
                    listBack.append(b)
        case 2:
            print(ti)
            for i in listBack:
                i.show_account(False)
        case 3:
            acc = int(input("Enter of Account Number : "))
            for i in listBack:
                i.deposit_amount(acc)
                
        case 4:
            acc = int(input("Enter of Account Number : "))
            for i in listBack:
                i.with_drow(acc)
        case 5:
            acc = int(input("Enter of Account Number : "))
            print(ti)
            for i in listBack:
                i.show_account(acc)
        case 0:
            print("Thank You ")
            exit()











            

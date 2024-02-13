from prettytable import PrettyTable
from random import randint

class RandomMathsProblems():
    def __init__(self,digits) -> None:
        #self.operation=operation
        self.digits=digits

    def summation(self):
        result=randint(10**(self.digits-1),10**self.digits-1)
        num_1=randint(1,result)
        num_2=result - num_1 
        return(num_1,num_2,result,'+')
    
    def subtraction(self):
        num_upper=randint(10**(self.digits-1),10**self.digits-1)
        num_lower=randint(1,num_upper)
        result=num_upper-num_lower
        return(num_upper,num_lower,result,'-')
    def product(self):
        num=[]
        num_upper_digits=randint(1,self.digits-1)
        num_lower_digits=self.digits-num_upper_digits
        num.append(randint(10**(num_upper_digits-1),10**num_upper_digits-1))
        num.append(randint(10**(num_lower_digits-1),10**num_lower_digits-1))
        num.sort(reverse=True)
        result=num[0]*num[1]
        return(num[0],num[1],result,'×')



# digits=4
# question=RandomMathsProblems(digits)
# sums=4
# subs=4
# products=20

# problist=[]

# for _ in range(sums):
#     problist.append(question.summation())
# for _ in range(subs) :
#     problist.append(question.subtraction())
# for _ in range(products) :
#     problist.append(question.product())    

# print(problist)

# nl='\n'
# # 

# cols=5
# blocksize=6

# # prob: Num1
# # opr   num2
# # -----------
# # blank
# # blank
# # blank
# blank_row=[]
# divider_row=[]
# header_row=[]
# for i in range(cols):
#     header_row.append('Col'+str(i+1))
#     blank_row.append('')
#     divider_row.append('-'*(digits+2))

# x=PrettyTable()
# x.align = "r" #align right all columns
# x.field_names=header_row
# i=0

# problen=len(problist)
# while i < problen:
#     top_row=[]
#     bottom_row=[]
#     for col in range(cols):
#         if i+col <problen:
#             top_row.append(f'{i+col+1:<4}{problist[i+col][0]:>6}')
#             bottom_row.append(f'{problist[i+col][3]:<2}{problist[i+col][1]:>6}')


#     while len(top_row)<cols:
#         top_row.append('')
#     while len(bottom_row)<cols:
#             bottom_row.append('')
    

#     x.add_row(top_row)
#     x.add_row(bottom_row)
#     x.add_row(divider_row)
#     x.add_row(blank_row)
#     x.add_row(blank_row)
    
#     i += cols

# print(x)
# answers=['Answers:-']
# for i ,(_,_,result,_) in enumerate(problist):
#     answers.append(f'{i+1}:{result}')


# listToStr = ' '.join(str(x) for x in answers )
# print(listToStr)


# with open('sums.txt', 'w') as f:
#     f.write(listToStr+nl)
#     f.write(str(x))
    





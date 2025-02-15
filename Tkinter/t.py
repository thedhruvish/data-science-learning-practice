# a = '5*2*4'
# ans = ''
# for i in range(len(a)):
#     match a[i]:
#         case '*':
#             ans += str(int(a[i-1] )* int(a[i+1]))
            
# print(ans)

# a[5,2,4]
# b[*,*]

# ans = a[0]


# ans = ans b[i] a[i+1]

# l = [23,*43]

def cal(l):
    num = []
    exp = []
    for i in l:
        if i.isdigit():
            num.append(i)
        else:
            exp.append(i)
    ans = int(num[0])
    for i in range(len(exp)):
        if exp[i] == '*':
            ans = int(ans) * int(num[i+1])
        elif exp[i] == '-':
            ans = int(ans) - int(num[i+1])
        elif exp[i] == '+':
            ans = int(ans) + int(num[i+1])
        elif exp[i] == '/':
            ans = int(ans) / int(num[i+1])

    print(ans)

a = "4"

if a.isdigit():
    print('ok')


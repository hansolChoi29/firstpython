# return

# 1
def get_square(num):
    #100을 돌려줌
    return num*num

print(get_square(10))

# 2
def get_square2(num):
    return num*num
y=get_square2(10) # 지정연산자, 100이 됨
print(y)


# 3
def get_square3(x):
    return x*x
print(get_square3(10)+get_square3(20))
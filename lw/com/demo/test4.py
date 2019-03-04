



h_w = 80
for i in range(0,h_w):
    if i%2 == 0:
        blank_f = (150-i)/2
        print(' ' * int(blank_f),end='')
        print('*' * i)

b_w = 30
b_h = 30
bt = (150 - b_w)/2
for i in range(0,b_h):
    print ( ' ' * int ( bt ), end='' )
    print('*'*b_w)
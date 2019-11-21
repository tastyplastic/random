import random

# l > w, r > w, th > w,
uwus = ['uwu', '(´・ω・｀)', '(*´∇｀)ﾉ', '(◕‿◕✿)', 'ღ(U꒳Uღ)', '(⁄˘⁄ ⁄ ω⁄ ⁄ ˘⁄)♡']
sentence = input('uwu? ')
hello = str()
for bread in sentence:
    if bread == 'l':
        hello.replace('l', 'w')
    elif bread == 'r':
        hello.replace('r', 'w')
    elif bread == 'th':
        hello.replace('th', 'w')
    else:
        hello = hello + bread
print(hello)
def hsl_to_ansi(h, s, l, str):
    h /= 360
    s /= 100
    l /= 100
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h * 6) % 2 - 1))
    m = l - c/2
    r, g, b = 0, 0, 0
    if 0 <= h < 1/6:
        r, g, b = c, x, 0
    elif 1/6 <= h < 1/3:
        r, g, b = x, c, 0
    elif 1/3 <= h < 1/2:
        r, g, b = 0, c, x
    elif 1/2 <= h < 2/3:
        r, g, b = 0, x, c
    elif 2/3 <= h < 5/6:
        r, g, b = x, 0, c
    elif 5/6 <= h <= 1:
        r, g, b = c, 0, x
    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,str)

def to_rgb(r,g,b,text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r,g,b,text)

def str_to_rgb(s):
    s1=s
    s=s.replace('white','rgb(255,255,255)')
    s=s.replace("rgb","").replace("(",'').replace(')','').split(',')
    s=[int(a) for a in s]
    s=to_rgb(s[0],s[1],s[2],s1)
    return s

def show(dict):
    l=list(dict.keys())
    s=''
    for i in l:
        s+=i+(": "+str_to_rgb(dict[i][0])+" ; "+str_to_rgb(dict[i][1])+"\n")
    return s

def prod(liste):
    n=1
    for elem in liste:
        n*=elem
    return n
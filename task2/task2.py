def f_circle(x,y,x0,y0,R):
    return (x-x0)**2 + (y-y0)**2 - R**2

def where_dot(x,y,x0,y0,R):
    if f_circle(x,y,x0,y0,R) == 0:
        return 0
    elif f_circle(x,y,x0,y0,R) > 0:
        return 2
    elif f_circle(x,y,x0,y0,R) < 0:
        return 1

with open('file1.txt', 'r', encoding='utf-8') as f1:
    data1 = f1.readlines()  

with open('file2.txt', 'r', encoding='utf-8') as f2:
    data2 = f2.readlines()

x0 = float(data1[0].split()[0])
y0 = float(data1[0].split()[1])
R = float(data1[1])

for i in range(len(data2)):
    x = float(data2[i].split()[0])
    y = float(data2[i].split()[1])
    print(where_dot(x,y,x0,y0,R))
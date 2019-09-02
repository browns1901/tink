from tkinter import *
import time 
import random

def Check(s, s1, i, j):
    for i in range(8):
        for j in range(8):
            tmp1 = 0
            tmp2 = 0            
            try:
                if s[i-1][j-1] == 2:
                    tmp1 += 1
                elif s[i-1][j-1] == 3:
                    tmp2 += 1
            except IndexError:
                pass
            try:
                if s[i-1][j] == 2:
                    tmp1 += 1
                elif s[i-1][j] == 3:
                    tmp2 += 1
            except IndexError:
                pass
            try:
                if s[i-1][j+1] == 2:
                    tmp1 += 1
                elif s[i-1][j+1] == 3:
                    tmp2 += 1
            except IndexError:
                pass 
            try:
                if s[i][j+1] == 2:
                    tmp1 += 1
                elif s[i][j+1] == 3:
                    tmp2 += 1
            except IndexError:
                pass 
            try:
                if s[i+1][j+1] == 2:
                    tmp1 += 1
                elif s[i+1][j+1] == 3:
                    tmp2 += 1
            except IndexError:
                pass 
            try:
                if s[i+1][j] == 2:
                    tmp1 += 1
                elif s[i+1][j] == 3:
                    tmp2 += 1
            except IndexError:
                pass 
            try:
                if s[i+1][j-1] == 2:
                    tmp1 += 1
                elif s[i+1][j-1] == 3:
                    tmp2 += 1
            except IndexError:
                pass 
            try:
                if s[i][j-1] == 2:
                    tmp1 += 1
                elif s[i][j-1] == 3:
                    tmp2 += 1
            except IndexError:
                pass 
            if s[i][j] == 0 and tmp1 == 3:
                s1[i][j] = 2
            elif s[i][j] == 0 and tmp2 == 3:
                s1[i][j] = 3
            elif s[i][j] == 2 and (tmp1 > 3 or tmp1 < 2):
                s1[i][j] = 0    
            elif s[i][j] == 3 and (tmp2 > 3 or tmp2 < 2):
                s1[i][j] = 0
            else:
                pass    
            
def DrawOcean():
    for i in range(0, 801, 100):
        canvas.create_line(i, 0, i, 800, fill = "black")
        canvas.create_line(0, i, 800, i, fill = "black")

def DrawNew(s):
    for i in range(8):
        for j in range(8):
            if s[i][j] == 1:
                DrawRock(i, j)
            elif s[i][j] == 2:
                DrawFish(i, j)
            elif s[i][j] == 3:
                DrawShrimp(i, j)

def DrawRock(m, n):
    m1 = 100 * m
    n1 = 100 * n
    canvas.create_polygon(m1 + 20, n1 + 80, m1 + 50, n1 + 20, m1 + 80, n1 + 80, fill = "gray") 
    
def DrawFish(m, n):
    m1 = 100 * m
    n1 = 100 * n    
    canvas.create_oval(m1 + 5, n1 + 15, m1 + 70, n1 + 85, fill = "orange")
    canvas.create_polygon(m1 + 70, n1 + 50, m1 + 95, n1 + 5, m1 + 95, n1 + 95, fill = "orange")
    
def DrawShrimp(m, n):
    m1 = 100 * m
    n1 = 100 * n
    canvas.create_polygon(m1 + 5, n1 + 50, m1 + 85, n1 + 35, m1 + 85, n1 + 65, fill = "pink")
    canvas.create_polygon(m1 + 85, n1 + 50, m1 + 95, n1 + 45, m1 + 95, n1 + 55, fill = "pink")
        
root = Tk()
size = 800
canvas = Canvas(root, width = size, height = size, bg = "blue")
canvas.pack()
A = [[0] * 8 for i in range(8)]
DrawOcean()
for i in range(8):
    for j in range(8):
        A[i][j] = random.randint(0, 3)
        if A[i][j] == 1:
            DrawRock(i, j)
        elif A[i][j] == 2:
            DrawFish(i, j)
        elif A[i][j] == 3:
            DrawShrimp(i, j)
canvas.update()
tmp = A
x = 0
while (x<3000):
    canvas.delete('all')
    Check(A, tmp, i, j)
    DrawOcean()
    DrawNew(tmp)
    time.sleep(2)
    canvas.update()
    A = tmp
    x += 1
    
 
root.mainloop()   
#!/usr/bin/python

filename="medium.txt"
fo = open(filename, "r")

triangle = []
with open(filename) as f:
    for line in f:
        linia=line.strip()
        lineList = linia.split(" ")
        print(lineList)
        triangle.append(lineList)

for y in range(len(triangle)):
	# print(len(plikList[y]))
	print("-------------")
	for x in range(len(triangle[y])):
		print(triangle[y][x])

def sumuj(x,y,tri,suma=0,pathStr=""):
	wartoscAktualnejPozycji=tri[y][x]
	suma=int(wartoscAktualnejPozycji) + suma
	pathStr=str(pathStr) + " + " + str(wartoscAktualnejPozycji)
	next_y=y+1 #nastepny wiersz
	next_x=x
	if next_y < len(tri):
		sumuj(next_x,next_y, tri, suma, pathStr) or sumuj(next_x+1,next_y, tri, suma, pathStr)
	else:
		print(pathStr + " = "+str(suma))

sumuj(0,0,triangle,0)

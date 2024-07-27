x, y, z = map(int,input("Enter the sides of the Triangle...:").split(" "))

s = ((x+y+z)/2)

tot = (s*(s-x)*(s-y)*(s-z))**(1/2)

print(tot)
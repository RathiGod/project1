radius = float(input("Input the radius of circle : "))
area = (22/7)*radius*radius
print("The area of circle with radius "+str(radius)+" is : "+str(area))

myDict={
    "c": "c",
    "py": "python",
    "cpp": "c++",
    "java": "java",
    "html": "html",
    "js": "javascript",
    "cs": "c#"
}

filename = input("Input the filename : ")
parts = filename.split('.')
if len(parts)>1:
    print(myDict.get(parts[1]))
else:
    print("No extension available")
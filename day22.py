# python dictionaries
thisdict =  {
"brand":"food",
"model":"mustange",
"year" : 1999
}
print(thisdict)
thisdict = {
"brand":"food",
"model":"mustange",
"year" : 1999
}
x = thisdict["model"]
print(x)
thisdict["year"] = 2000
print(thisdict)
c = {
    "welcome":"Shoug",
    "Sara" : "Mona",
}
for x in c:
    print(x)
    for x in c:
        print(c[x])
for x , y in c .items():
    print(x,y)
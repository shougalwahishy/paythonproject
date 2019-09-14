# python dictionaries
thisdict = {

"brand":"food",

"model":"mustange",

"year" : 1999,

}

if "model" in thisdict:

 print("yes model in there")

 print(len(thisdict))

 thisdict["color"] = "red"

 print(thisdict)

 thisdict.pop("model")

 print(thisdict)

 c = {

     "hi":"welcome",

     "mohamed":"thanks"

 }

 del c ['hi']

 print(c)

 c.clear()

 print(c)
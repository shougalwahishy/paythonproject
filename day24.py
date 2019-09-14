my_dict ={

    "name":"shoug",

    "f_name":"saleem",

    "age":34

}

this_dict=my_dict.copy()

print(this_dict)

#Another way to make a copy is to use the built-in method dict() :

this_dict=dict(my_dict)

print(this_dict)
#A dictionary can also contain many dictionaries, this is called nested dictionaries. 
#Create a dictionary that contain three dictionaries

familydict={

"father":{

      "name":"saleem",

        "age":50

        },

        "mother":{

            "name":"soso",

            "age":40

        },

        " chaild" :{

             "name":"nory",

             "age":1

         }

}

print(familydict)

#use the dict() constructor to make a new dictionary:

this_dict= dict("name"="shoug" , "gender"="female" , "age"=25)

print(this_dict)
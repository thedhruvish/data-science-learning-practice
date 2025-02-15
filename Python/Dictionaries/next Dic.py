subject = {
    "Sem1":{
        "1":"C",
        "2":"CN",
        "3":"CF",
        "4":"Math",
    },
    "Sem2":{
        "1":"Adv C",
        "2":"SAD",
        "3":"PHP",
        "4":"COA"
    },
    "Sem3":{
        "1":"CPP",
        "2":"wordpress",
        "3":"RDBMS",
        "4":"Adv Net"
    }
}
#print(subject["Sem1"]["3"])

sem1 = {
        "1":"C",
        "2":"CN",
        "3":"CF",
        "4":"Math",
}
sem2 = {
    "1":"Adv C",
    "2":"SAD",
    "3":"PHP",
    "4":"COA"
}
sem3 = {
    "1":"CPP",
    "2":"wordpress",
    "3":"RDBMS",
    "4":"Adv Net"
}


subject = {
    "sem1":sem1,
    "sem2":sem2,
    "sem3":sem3,
}

#print(sem1.items())

#print(subject)

#for i,x in sem1.items():    
 #   print(i,":",x)


#print(subject.items())


for i,x in subject.items():
    print(i)
    for y in x:
        print(y,":",x[y])

        


















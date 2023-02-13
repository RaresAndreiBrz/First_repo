my_dict = {
    'animal': 'pisica',
    123: 'thisisanumber',
    True: [
        {
            'user': 'rares',
            'parola': 'andrei'
        },
        {
            'user': 'ion',
            'parola': 'marcel'
        }
    ],
    52.2: "latitudinea Romaniei"
}
my_dict2 = dict(animal="pisica", numbers="thisisanumber",
                my_boolean=[dict(user="rares", parola="andrei"), dict(user="ion", parola="marcel")],
                parole={
                    1 : 1,
                    True : "Yes",
                })
print(my_dict[True][1]['parola'])
my_dict["email"] = "gmail@gmail.com"
print(my_dict)
my_dict["email"] = "gmail@yahoo.com"
print(my_dict)
del my_dict["email"]
print(my_dict)
#de incercat alte metode




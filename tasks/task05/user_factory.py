#Task 05: User factory
def create_user(name, surname, age = 42, **kwarg):
    if type(name) != str or type(surname) != str or type(age) != int:
        raise ValueError("ValueError: Type of name and surname must be string, type of age must be int")
    return {
       "name": name,
       "surname": surname,
       "age": age,
       "extra": kwarg
       }
tests = [
    [["John", "Doe"], {}, #1
    {
       "name": "John",
       "surname": "Doe",
       "age": 42 ,
       "extra": {}
       }
    ], 
    [["Bill", "Gates", 65], {},#2
    {
       "name": "Bill",
       "surname": "Gates",
       "age": 65,
       "extra": {}
       }
    ], 
    [["Marie", "Curie", 66], {"occupation": "physicist", "won_nobel": True}, #3
    {
       "name": "Marie",
       "surname": "Curie",
       "age": 66,
       "extra": {
           "occupation": "physicist",
           "won_nobel": True}
        }
    ],
    [["Vasya", "Pupkin", "two"], {"education": "absent", "won_nobel": "bad luck"}, #4 Wrong age = 42
    "ValueError: Type of name and surname must be string, type of age must be int"
    ],
    [[2], {}, #5 Name and surname are missed
    "create_user() missing 1 required positional argument: 'surname'"
    ]
]
for i, test in enumerate(tests):
    result = False
    print(f"Test {(i+1)} ...")
    try:
        if create_user(*test[0], **test[1]) == test[2]:
            result = True
        print("OK")
    except TypeError as err:
        if str(err) == test[2]:
            result = True
        print(f"{err} - OK")
    except ValueError as err:
        if str(err) == test[2]:
            result = True
        print(f"{err} - OK")
    assert result
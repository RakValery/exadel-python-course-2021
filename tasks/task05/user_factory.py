#Task 05: User factory
def create_user(*arg, **kwarg):
    if len(arg) == 2 or (len(arg) == 3 and type(arg[2]) != int):
        name = arg[0]
        surname = arg[1]
        age = 42
    elif len(arg) == 3 and type(arg[2]) == int:
        name = arg[0]
        surname = arg[1]
        age = arg[2]
    else: 
        raise ValueError(f"ValueError: arg={arg}")
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
    [["Vasya", "Pupkin", "2"], {"education": "absent", "won_nobel": "bad luck"}, #4 Wrong age = 42
    {
       "name": "Vasya",
       "surname": "Pupkin",
       "age": 42,
       "extra": {
           "education": "absent",
           "won_nobel": "bad luck"}
        }
    ],
    [[2], {}, #5 Name and surname are missed
    "ValueError: arg=(2,)"
    ]
]
for i, test in enumerate(tests):
    result = False
    print(f"Test {(i+1)} ...")
    try:
        res = create_user(*test[0], **test[1])
        if res == test[2]:
            result = True
        print("OK")
    except ValueError as err:
        if str(err) == test[2]:
            result = True
            print("OK")
    assert result
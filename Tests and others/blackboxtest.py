from IsValidPassword.isvalidpassword import IsValidPassword

test_cases = {
    "abc": False,
    "abcdef": False,
    "ABCDEF": False,
    "Abcdef": False,
    "Abcdef1": False,
    "Abcdef1@": False,
    "Abcdef1@may": False,
    "Abc9@may8": False,
    "Abc9@may816": False,
    "Abc9@may1672": True,
    "Xyz8#january679": True,
    "PqR5!august6157": True,
    "ZtW3$december8176": True,
    "LmN7%march1846": True,
    "QwEr2^february6914": True,
    "Abc1@may": False,
    "abc9@may1672": False,
    "ABC9@MAY1672": False,
    "Abc9may1672": False
}

for s,e in zip(test_cases.keys(), test_cases.values()):
    try:
        assert IsValidPassword.validate_password(s) is None
    except AssertionError:
        print(f"{s} ({e}): False")
    else:
        print(f"{s} ({e}): True")


def Funk(filename):
    content=''
    with open (filename, 'r') as file:
        content = file.read()
    gl = 0
    sql = 0
    for char in content:
        if char.isalpha():
            if char.lower() in "eyuioa":
                gl += 1
        if char.lower() in "qwrtpsdfghjklzxcvbnm":
            sql += 1

    print("sogl - " + str(sql) + " shtyk")
    print("glasn - " + str(gl) + " shtyk")

Funk("test")
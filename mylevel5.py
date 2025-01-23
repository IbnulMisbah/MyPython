"""
Bismillahir Rahmanir Rahim ..

"""



prefix = ""

sufix = ""

with open("pico","r") as file :
    
    lines = file.readlines()

with open("pico","w") as newfile :

    for line in lines :
        
        modified = line.strip()

        new_line = f"{prefix}{modified}{sufix}"

        newfile.write(new_line)




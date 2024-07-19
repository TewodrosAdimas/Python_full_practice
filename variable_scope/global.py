global_txt = "global text"

def local_txt():
    global_txt = "local text"
    print(global_txt)

local_txt()
print(global_txt)
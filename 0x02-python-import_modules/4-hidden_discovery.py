#!/usr/bin/python3
if __name__ == "__main__":
    # print all names
    import hidden_4
    nam = dir(hidden_4)
    for name in nam:
        if nam[:2] != "__":
            print(nam)

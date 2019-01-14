




def check_float(a, func=None):
    a = list(a)
    if a.count("e") == 1:
        first = a[:a.index("e")]
        second = a[a.index("e")+1:]
        if first and not second:
            if check_normal_float(first):
                return True
        elif not first and second:
            if check_int(second):
                return True
        elif first and second:
            if check_normal_float(first) and check_normal_float(second):
                return True
        else:
            return False
    elif a.count("e") == 0:
        if check_normal_float(a):
            return True
    else:
        return False
    return False









def check_normal_float(a):
    a = list(a)
    if 0 <= a.count("+")+a.count("-") <= 1:
        if "+" in a:
            if a.index("+") == 0:
                a.pop(0)
                if 0 <= a.count(".") <= 1:
                    if "".join(a).replace(".", "").isdigit():
                        return True
        elif "-" in a:
            if a.index("-") == 0:
                a.pop(0)
                if 0 <= a.count(".") <= 1:
                    if "".join(a).replace(".", "").isdigit():
                        return True
        else:
            if ("".join(a)).replace(".", "", 1).isdigit():
                return True
        return False













def check_int(a, fun=None):
    a = list(a)
    """Проверка на целое число"""
    if "-" in a:
        if a.index("-") == 0:
            a.pop(0)
            if "".join(a).isdigit():
                if fun != None:
                    if fun(int("".join(a))):
                        return True
                    else:
                        return False
                else:
                    return True

    elif "+" in a:
        if a.index("+") == 0:
            a.pop(0)
            if "".join(a).isdigit():
                if func != None:
                    if fun(int("".join(a))):
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
    else:
        if "".join(a).isdigit():
            if fun != None:
                if fun(int("".join(a))):
                    return True
                else:
                    return False
            else:
                return True
        return False
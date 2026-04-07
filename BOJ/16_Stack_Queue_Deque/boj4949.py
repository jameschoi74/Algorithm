while True:
    s = input()

    if s == ".":
        break

    stk = []
    status = "yes"

    for l in s:
        if l == "(":
            stk.append(l)
        elif l == "[":
            stk.append(l)
        elif l == ")":
            if not stk:
                status = "no"
                break
            if stk.pop() != "(":
                status = "no"
        elif l == "]":
            if not stk:
                status = "no"
                break
            if stk.pop() != "[":
                status = "no"
    if stk:
        status = "no"
    print(status)
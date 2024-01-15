def uniq_str(s):
    chars=set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True
s='abcdea'
result=uniq_str(s)
print(result)
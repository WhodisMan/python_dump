
text = "we accept the ieeextreme challenge"
n = 1
rot =19

def is_plain(text):
    return "the" in text

def cypher(text, rot, case):
    result = ""
    list(text)
    if case:
        rot = -rot
    for i in range(len(text)):
        if text[i] == " ":
            result += " "
        else:
            result += chr((ord(text[i]) + rot - 97) % 26 + 97)
    print(result)

def main():
    cypher(text,rot,is_plain(text))

main()
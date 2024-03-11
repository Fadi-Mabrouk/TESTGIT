def crypcesar(text,shift):
    cryptext=""
    for char in text :
        if char.isalpha():
            is_upper=char.isupper()
            char=char.lower()
            shifted=chr(((ord(char)-ord('a')+shift)%26)+ord('a'))
            if is_upper:
                shifted=shifted.upper()
            cryptext+=shifted
        else:
            cryptext+=char
    return cryptext
def decrypt(text,shift):
    dcryptext=""
    for char in text :
        if char.isalpha():
            is_upper=char.isupper()
            char=char.lower()
            shifted=chr(((ord(char)-ord('a')-shift)%26)+ord('a'))
            if is_upper:
                shifted=shifted.upper()
            dcryptext+=shifted
        else:
            dcryptext+=char
    return dcryptext
def test():
    text=input("donnez texte : ")
    x=int(input("donnez cle : "))
    c=crypcesar(text,x)
    print(c)
    print(decrypt(c,x))
test()
        
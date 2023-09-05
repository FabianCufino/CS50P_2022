
def main():
    x1 =  input("Write yout sentence--> ").lower().strip()
    print (extensions(x1))



def extensions(n1):
    splitwords = n1.split(".")
    if len(splitwords) == 1:
        n2 = "na"
    elif len(splitwords) > 1:
        n2 = splitwords[len(splitwords)-1]

    if n2 == "gif":
        n3 = "image/gif"
    elif n2 == "jpg":
        n3 = "image/jpeg"
    elif n2 == "jpeg":
        n3 = "image/jpeg"
    elif n2 == "png":
        n3 = "image/png"
    elif n2 == "pdf":
        n3 = "application/pdf"
    elif n2 == "txt":
        n3 = "text/plain"
    elif n2 == "zip":
        n3 = "application/zip"
    elif n2 == "na":
        n3 = "application/octet-stream"
    else:
        n3 = "application/octet-stream"

    return n3

main()

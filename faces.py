def main():
  input_raw =  input("Write yout sentence--> ")
  input_new = convert(input_raw)
  print(input_new)


def convert(n):
  n1 = n.replace(":)","🙂").replace(":(","🙁")
  return n1

main()

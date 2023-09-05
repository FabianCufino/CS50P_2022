def main():
  input_raw =  int(input("Write yout sentence--> "))
  input_new = convert_emc(input_raw)
  print(input_new)


def convert_emc(n):
  n1= n*(300000000**2)
  return n1

main()

import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        matches1 = re.search(r'^(.*) (PM|AM) (to) (.*) (PM|AM)$', s, re.IGNORECASE)
        if matches1:
            time_a = matches1.groups(1)[0]
            time_b = matches1.groups(1)[3]
            mark_a = matches1.groups(1)[1]
            mark_b = matches1.groups(1)[4]
            if matches1.groups(1)[2] != "to":
                raise ValueError

            #print(time_a, time_b, mark_a, mark_b)
            if ":" in time_a:
                h_a, m_a = time_a.split(":")

                if mark_a.lower() == "am" and int(h_a) == 12:
                    h_a = 0
                elif mark_a.lower() == "pm" and int(h_a) == 12:
                    h_a = 12
                elif mark_a.lower() == "pm":
                    h_a = int(h_a) + 12
            else:
                h_a = int(time_a)
                m_a = 0

                if mark_a.lower() == "am" and int(h_a) == 12:
                    h_a = 0
                elif mark_a.lower() == "pm" and int(h_a) == 12:
                    h_a = 12
                elif mark_a.lower() == "pm":
                    h_a = h_a + 12

            if ":" in time_b:
                h_b, m_b = time_b.split(":")

                if mark_b.lower() == "am" and int(h_b) == 12:
                    h_b = 0
                elif mark_b.lower() == "pm" and int(h_b) == 12:
                    h_b = 12
                elif mark_b.lower() == "pm":
                    h_b = int(h_b) + 12

            else:
                h_b = int(time_b)
                m_b = 0

                if mark_b.lower() == "am" and int(h_b) == 12:
                    h_b = 0
                elif mark_b.lower() == "pm" and int(h_b) == 12:
                    h_b = 12
                elif mark_b.lower() == "pm":
                    h_b = h_b + 12


            if int(m_a) >= 60 or int(m_b) >= 60 or int(h_a) > 24 or int(h_b) > 24 :
                raise ValueError

            #print(h_a, m_a, h_b, m_b)
            hora = "{:02d}:{:02d} to {:02d}:{:02d} ".format(int(h_a), int(m_a), int(h_b), int(m_b))
            hora2 = hora.strip()
            return hora2
        else:
            raise ValueError
    except ValueError:
        raise

if __name__ == "__main__":
    main()

from datetime import date, datetime, timedelta, time
import inflect
import sys
p = inflect.engine()

def main():
    fecha_birth = input("Date of birth: ")

    try:
        fecha_birth2 = check_date(fecha_birth)
        if fecha_birth2 == None:
            raise sys.exit('Invalid date')
    except:
        raise sys.exit('Invalid date')


    date_hoy = datetime.combine(date.today(), time(hour=0, minute=0, second=0, microsecond=0))
    time_lapse = date_hoy - fecha_birth2
    minutes = time_lapse / timedelta(minutes=1)
    minutes = int(minutes)
    text = p.number_to_words(minutes, andword="")
    print (text.capitalize(), "minutes")
    #output = p.number_to_words(minutes)
    #print(output.capitalize(), "minutes")


def check_date(birth):
    try:
        birth2 = datetime.strptime(birth, '%Y-%m-%d')
        #print (type(birth2))
        return birth2
    except:
        return None

if __name__ == "__main__":
    main()

def main():
    time = input("What time is it? ")
    time = convert(time)
    if 8 >= time >= 7:
        print("breakfast time")
    elif 13 >= time >= 12:
        print("lunch time")
    elif 19 >= time >= 18:
        print("dinner time")
    ...


def convert(time):
    hours,minutes = time.split(":")
    hours = float(minutes)/60 + float(hours) 
    return hours
    ...


if __name__ == "__main__":

        main()
    
    
    
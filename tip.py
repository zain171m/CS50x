def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
    #First replace $ sign with ""(nothing). than returns it's type caste
    d = dollars.replace("$","")
    return float(d)
    

def percent_to_float(percentage):
    #First replace % sign with ""(nothing). than returns it's type caste/1
    p = percentage.replace("%","")
    return float(p)/100
    
main()
#student ID : 1201200987
#student Name : Loh Joo Sheng

def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter

def get_cm():
    cm = float(input("Please enter a value for centimeter :"))
    m  = cm_to_meter(cm)
    print("{:.2f} cm is equil to {:.2f} meter.".format(cm,m))

def m_to_cm(meter):
    cm = meter * 100
    return cm

def get_m():
    m = float(input("Please enter a value for meter :"))
    cm  = m_to_cm(m)
    print("{:.2f} m is equil to {:.2f} centimeter.".format(m,cm))    


print("==============================================")
print("               CM & M Converter               ")
print("==============================================")
print("1. CM to M ")
print("2. M to CM ")
print("**********************************************")
choice=int(input("Please enter your choice : "))


if choice==1:
    get_cm();

elif choice==2:
    get_m();  
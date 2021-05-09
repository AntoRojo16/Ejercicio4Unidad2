from ClaseFechayHorados import FechaHora

def bisiesto (año):
    if (año%4==0 and año%100!=0 or año%100==0):
        return True
    else:
        return False
def valiadarHora (hora,min,seg):

    if (hora in range(24)):
        if min in range(60):
            if seg in range(60):
                return True
            else:
                print("los datos ingresados son incorrectos,seg")
                return False
        else:
            print("los datos ingresados son incorrectos,min")
            return False
    else:
        print("los datos ingresados son incorrectos,hora")
        return False

def validar (dia,mes, año,hora,min,seg):
    if (año in range(2022)):
        if (mes in range(13)):
            if (mes==4 or mes==6 or mes==9 or mes==11):
                if dia in range(31):
                    if (valiadarHora(hora,min,seg)):
                        return True
                    else:
                        print("los datos ingresados son incorrectos, hora")
                        return False
                else:
                    print("los datos ingresados son incorrectos, se ingreso un dia incorrecto")
                    return False
            else:
                if (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
                    if dia in range(32):
                        if (valiadarHora(hora,min,seg)==True):
                            return True
                        else:
                            print("los datos ingresados son incorrectos")
                            return False
                    else:
                        print("los datos ingresados son incorrectos")
                        return False
                else:
                    if mes==2:
                        if bisiesto(año):
                            if dia in range(30):
                                if (valiadarHora(hora,min,seg)==True):
                                    return True
                                else:
                                    print("los datos ingresados son incorrectos")
                                    return False
                            else:
                                print("los datos ingresados son incorrectos")
                                return False
                        else:
                            if dia in range(29):
                                if (valiadarHora(hora,min,seg)==True):
                                    return True
                                else:
                                    print("los datos ingresados son incorrectos")
                                    return False
                            else:
                                print("los datos ingresados son incorrectos")
                                return False 
    else:
        return False
    
if __name__ == '__main__':

    d=int(input("Ingrese Dia: "))
    mes=int(input("Ingrese Mes: "))

    a=int(input("Ingrese Año: "))

    h=int(input("Ingrese Hora: "))

    m=int(input("Ingrese Minutos: "))

    s=int(input("Ingrese Segundos: "))
    if validar(d,mes,a,h,m,s):
        r = FechaHora (1,1,2020) #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y 

                              #  segundos con 0h, 0m, 0s.

        r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s

        r2= FechaHora(d,mes,a,h, m, s)

        r.Mostrar()

        r1.Mostrar()

        r2.Mostrar()

        input()

        r.PonerEnHora(5)
        # solamente la hora

        r.Mostrar()

        input()

        #r2.PonerEnHora(13,30) #hora y minutos

        #r2.Mostrar()

        input()

        r.PonerEnHora(14, 30, 25) #hora, minutos y segundos

        r.Mostrar()

        input()

        r.AdelantarHora(3) #sumar 3 horas a la hora actual

        r.Mostrar()

        input()

        r2.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual

        r2.Mostrar()

        input()



   
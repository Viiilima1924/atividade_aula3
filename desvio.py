import statistics 

def desvio():
    empresa1 = [1000,6000,1200,8000,1400]
    desvio1 =  statistics.stdev(empresa1)
    print("Desvio empresa 1 - " , desvio1)
    empresa2 = [5000,4000,3000,2000,7000]
    desvio2  =  statistics.stdev(empresa2)
    print("Desvio empresa 2 - " , desvio2)
    empresa3 = [1200,1300,8000,3000,15000]
    desvio3  =  statistics.stdev(empresa3)
    print("Desvio empresa 3 - " , desvio3)
    empresa4 = [1400,1750,2000,4500,5900,7000]
    desvio4  =  statistics.stdev(empresa4)
    print("Desvio empresa 4 - " ,desvio4)
    empresa5 = [1400,1750,2000,4500,5900,7000]
    desvio5  =  statistics.stdev(empresa5)
    print("Desvio empresa 5 - " , desvio5)

desvio()
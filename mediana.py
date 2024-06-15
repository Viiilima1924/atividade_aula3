import statistics

def mediana():
    empresa1 = [1000,6000,1200,8000,1400]
    mediana1 = statistics.median(empresa1)
    print("Mediana empresa 1 - " ,mediana1)
    empresa2 = [5000,4000,3000,2000,7000]
    mediana2 = statistics.median(empresa2)
    print("Mediana empresa 2 - " , mediana2)
    empresa3 = [1200,1300,8000,3000,15000]
    mediana3 = statistics.median(empresa3)
    print("Mediana empresa 3 - " , mediana3)
    empresa4 = [1400,1750,2000,4500,5900,7000]
    mediana4 = statistics.median(empresa4)
    print("Mediana empresa 4 - " , mediana4)
    empresa5 = [1400,1750,2000,4500,5900,7000]
    mediana5 = statistics.median(empresa5)
    print("Mediana empresa 5 - " , mediana5)
mediana()

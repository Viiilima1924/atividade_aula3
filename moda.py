import statistics 

def moda():
    empresa1 = [1000,6000,1200,8000,1400]
    moda1 =  statistics.mode(empresa1)
    print("Moda empresa 1 - " , moda1)
    empresa2 = [5000,4000,3000,2000,7000]
    moda2  =  statistics.mode(empresa2)
    print("Moda empresa 2 - " ,moda2)
    empresa3 = [1200,1300,8000,3000,15000]
    moda3  =  statistics.mode(empresa3)
    print("Moda empresa 3 - " , moda3)
    empresa4 = [1400,1750,2000,4500,5900,7000]
    moda4  =  statistics.mode(empresa4)
    print("Moda empresa 4 - " , moda4)
    empresa5 = [1400,1750,2000,4500,5900,7000]
    moda5  =  statistics.mode(empresa5)
    print("Moda empresa 5 - " , moda5)

moda()
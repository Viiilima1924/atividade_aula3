import statistics

def media():
    empresa1 = [1000,6000,1200,8000,1400]
    media1 =  statistics.mean(empresa1)
    print("Média empresa 1 - ", media1)
    empresa2 = [5000,4000,3000,2000,7000]
    media2  =  statistics.mean(empresa2)
    print("Média empresa 2 - ", media2)
    empresa3 = [1200,1300,8000,3000,15000]
    media3  =  statistics.mean(empresa3)
    print("Média empresa 3 - ",media3)
    empresa4 = [1400,1750,2000,4500,5900,7000]
    media4  =  statistics.mean(empresa4)
    print("Média empresa 4 - ",media4)
    empresa5 = [1400,1750,2000,4500,5900,7000]
    media5  =  statistics.mean(empresa5)
    print("Média empresa 5 - ",media5)

media()



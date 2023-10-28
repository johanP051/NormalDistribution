import numpy as np
from matplotlib import pyplot as plt 
from scipy.stats import norm

mu = float(input("Inserte el valor de la media (µ) : "))
sigma = float(input("Inserte el valor para la desviación típica: "))

menu = {
    1: "Calcular la probabilidad de un valor menor o igual que X P(X <= x)", 
    2: "Calcular la probabilidad de un valor mayor o igual que X P(X >= x)",
    3: "Calcular la probabilidad entre dos valores de x P(x1<X<x2)"
}

while True:
    try: 
        option = int(input("Inserte la opción que desea: "))
    except ValueError:
        print("Debe ser un entero")
        continue
    if option not in menu.keys():
        print("Recuerda que debe elegir un el número correspondiente a la opción")
        continue
    else:
        break



def menorX(x, mu, sigma):

    z = (x-mu)/sigma

    #Estandarizando
    mu = 0
    sigma = 1

    fig, ax = plt.subplots()
    X = np.linspace(mu - 3*sigma, mu + 3*sigma)
    Y = norm.pdf(X, mu, sigma)
    
    

    x_fill = np.linspace(mu - 3*sigma, z)
    y_fill = norm.pdf(x_fill, mu, sigma)
    
    ax.plot(X, Y, color="b")
    ax.fill_between(x_fill, y_fill, 0, color="g", alpha=0.4)
    
    plt.show()

    PX = norm.cdf(z, mu, sigma)
    PX = round(PX, 4)
    print(f"La probabilidad de z < {z} es de {PX} = {PX*100}%")

def mayorX(x, mu, sigma):

    z = (x-mu)/sigma

    #Estandarizando
    mu = 0
    sigma = 1

    fig, ax = plt.subplots()
    X = np.linspace(mu - 3*sigma, mu + 3*sigma)
    Y = norm.pdf(X, mu, sigma)
    
    

    x_fill = np.linspace(z, mu + 3*sigma)
    y_fill = norm.pdf(x_fill, mu, sigma)
    
    ax.plot(X, Y, color="b")
    ax.fill_between(x_fill, y_fill, 0, color="g", alpha=0.4)
    
    plt.show()

    PX = 1 - norm.cdf(z, mu, sigma)
    PX = round(PX, 4)
    print(f"La probabilidad de z < {z} es de {PX} = {PX*100}%")

def rangeX(x1, x2, mu, sigma):

    z1 = (x1-mu)/sigma
    z2 = (x2-mu)/sigma

    #Estandarizando
    mu = 0
    sigma = 1

    fig, ax = plt.subplots()
    X = np.linspace(mu - 3*sigma, mu + 3*sigma)
    Y = norm.pdf(X, mu, sigma)
    
    

    x_fill = np.linspace(z1, z2)
    y_fill = norm.pdf(x_fill, mu, sigma)
    
    ax.plot(X, Y, color="b")
    ax.fill_between(x_fill, y_fill, 0, color="g", alpha=0.4)
    
    plt.show()

    PX = (norm.cdf(z2 ,mu, sigma)) - (norm.cdf(z1 ,mu, sigma))
    PX = round(PX, 4)
    print(f"La probabilidad de {z1} < z < {z2} es de {PX} = {PX*100}% ")

if option == 1:
    x = float(input("Inserte el valor de X para el que desea calcular la probabilidad: "))
    menorX(x, mu, sigma)

elif option == 2:
    x = float(input("Inserte el valor de X para el que desea calcular la probabilidad: "))
    mayorX(x, mu, sigma)

else:
    x1 = float(input("Inserte el valor inicial x1 del intervalo para calcular la probabilidad: "))
    x2 = float(input("Inserte el valor inicial x2 del intervalo para calcular la probabilidad: "))
    rangeX(x1, x2, mu, sigma)


import numpy as np
from matplotlib import pyplot as plt 
from scipy.stats import norm

mu = float(input("Inserte el valor de la media (µ) : "))
sigma = float(input("Inserte el valor para la desviación típica: "))

menu = {
    1: "Calcular la probabilidad de un valor menor o igual que X P(X < x)", 
    2: "Calcular la probabilidad de un valor mayor o igual que X P(X > x)",
    3: "Calcular la probabilidad entre dos valores de x P(x1 < X < x2)"
}

print(f"Escoja alguna opción del menú\n")
for i in menu:
    print(i, ":", menu[i])
    

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
    
    #Creando una gráfica compuesta de más gráficas dentro de ella
    fig, ax = plt.subplots()

    #Dividiendo los límites de la gráfica, con espacios equidistantes (np.linspace)
    X = np.linspace(mu - 3*sigma, mu + 3*sigma)

    #Definiendo la función F(x), pdf: Probability Density Function
    Y = norm.pdf(X, mu, sigma)
    
    
    #Definiendo el area sombreada de la gráfica
    x_fill = np.linspace(mu - 3*sigma, x)
    y_fill = norm.pdf(x_fill, mu, sigma)
    
    ax.plot(X, Y, color="b")
    ax.fill_between(x_fill, y_fill, 0, color="g", alpha=0.4)

    #Mostrando la gráfica
    plt.show()

    # cdf: Cumulative Distribution Function
    PX = norm.cdf(x, mu, sigma)
    PX = round(PX, 4)
    print(f"La probabilidad de x < {x} es de {PX} = {PX*100}%")

def mayorX(x, mu, sigma):

    fig, ax = plt.subplots()
    X = np.linspace(mu - 3*sigma, mu + 3*sigma)
    Y = norm.pdf(X, mu, sigma)
    
    

    x_fill = np.linspace(x, mu + 3*sigma)
    y_fill = norm.pdf(x_fill, mu, sigma)
    
    ax.plot(X, Y, color="b")
    ax.fill_between(x_fill, y_fill, 0, color="g", alpha=0.4)
    
    plt.show()

    PX = 1 - norm.cdf(x, mu, sigma)
    PX = round(PX, 4)
    print(f"La probabilidad de z < {x} es de {PX} = {PX*100}%")

def rangeX(x1, x2, mu, sigma):

    fig, ax = plt.subplots()
    X = np.linspace(mu - 3*sigma, mu + 3*sigma)
    Y = norm.pdf(X, mu, sigma)
    
    

    x_fill = np.linspace(x1, x2)
    y_fill = norm.pdf(x_fill, mu, sigma)
    
    ax.plot(X, Y, color="b")
    ax.fill_between(x_fill, y_fill, 0, color="g", alpha=0.4)
    
    plt.show()

    PX = (norm.cdf(x2 ,mu, sigma)) - (norm.cdf(x1 ,mu, sigma))
    PX = round(PX, 4)
    print(f"La probabilidad de {x1} < X < {x2} es de {PX} = {PX*100}% ")

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


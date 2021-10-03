import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def wodociagi():
    data = pd.read_csv("wodociagi.txt", sep=';')

    districts = []
    no_of_people = []

    for id_ in data["KodKlienta"]:
        districts.append(id_[-3:])
        no_of_people.append(id_[-5:-3])

    no_of_people = list(map(int, no_of_people))
    data.insert(0, "LiczbaMieszkańców", no_of_people)
    data.insert(0, "Dzielnica", districts)
    # data["Dzielnica"] = districts
    # data["LiczbaMieszkańców"] = no_of_people
    print(data)
    df = pd.DataFrame(data.loc[:, "I":"LiczbaMieszkańców"])
    df = df.groupby('Dzielnica').mean().reset_index()

    df.set_index("Dzielnica").T.plot(kind='bar', stacked=False, title="Średnie zużycie wody w danej dzielnicy w ciągu miesiąca.")

    df = pd.DataFrame(data.loc[:, "I":"XII"])
    new_plot = df.sum().reset_index()
    new_plot = new_plot.rename(columns={'index': "Miesiąc", 0: "Liczba mieszkańców"})
    plotpie = new_plot
    new_plot["Liczba mieszkańców"] = new_plot["Liczba mieszkańców"]/sum(no_of_people)

    new_plot.plot(x="Miesiąc", kind='bar', stacked=False, title="Średnie zużycie na mieszkańca", legend=None)
    plt.show()

    print(plotpie)
    label = ["" for _ in range(12)]
    plotpie.plot(y="Liczba mieszkańców", autopct="%.2f", labels=label, kind='pie')
    plt.legend(plotpie["Miesiąc"])
    plt.show()

wodociagi()

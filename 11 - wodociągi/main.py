import pandas as pd
import matplotlib.pyplot as plt


def wodociagi():
    df = pd.read_csv("wodociagi.txt", sep=';')
    format_data(df)
    water_use_in_month(df.copy(deep=True))
    monthly_use = table_of_months(df)
    no_of_people = df["Liczba Mieszkańców"].sum()
    water_use_per_inhabitant(monthly_use.copy(deep=True), no_of_people)
    pie_chart(monthly_use.copy(deep=True))
    plt.show()


def format_data(data):
    districts = []
    no_of_people = []
    for id_ in data["KodKlienta"]:
        districts.append(id_[-3:])
        no_of_people.append(id_[-5:-3])
    no_of_people = list(map(int, no_of_people))
    data.insert(1, "Liczba Mieszkańców", no_of_people)
    data.insert(1, "Dzielnica", districts)
    data.pop("KodKlienta")


def table_of_months(df):
    return pd.DataFrame(df.loc[:, "I":"XII"]).sum().reset_index().rename(columns={'index': "Miesiąc", 0: "Zużycie wody"})


def water_use_in_month(df):
    df = df.groupby('Dzielnica').mean().reset_index()
    df.pop("Liczba Mieszkańców")
    df.set_index("Dzielnica").T.plot(kind='bar', stacked=False, title="Średnie zużycie wody w danej dzielnicy w ciągu miesiąca.")
    plt.legend(loc="upper right")


def water_use_per_inhabitant(df, no_of_people):
    df["Zużycie wody"] = df["Zużycie wody"]/no_of_people
    df.plot(x="Miesiąc", kind='bar', stacked=False, title="Średnie zużycie na mieszkańca", legend=None)


def pie_chart(df):
    label = ["" for _ in range(12)]
    df.plot(y="Zużycie wody", autopct="%1.2f%%", labels=label, kind='pie')
    plt.legend(df["Miesiąc"])


wodociagi()

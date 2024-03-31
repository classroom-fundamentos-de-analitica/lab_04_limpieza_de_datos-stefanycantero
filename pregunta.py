"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    # Eliminar primera columna
    df.drop(df.columns[0], axis=1, inplace=True)

    # Eliminar filas duplicadas
    df = df.drop_duplicates()

    # Eliminar filas con datos faltantes
    df = df.dropna()    

    # Convertir todas las cadenas de texto a minúsculas en todas las columnas del dataframe que sean de tipo object
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

    # Convertir la columna comuna_ciudadano de tipo float a tipo int
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype("Int64")

    # Eliminar caracteres como $ y , en la columna monto_del_credito
    # Eliminar los caracteres después del punto en la columna monto_del_credito
    # Convertir la columna monto_del_credito de tipo object a tipo int
    df["monto_del_credito"] = df["monto_del_credito"].str.replace("$", "").str.replace(",", "").str.split(".").str[0].astype(int)

    # Eliminar espacios en blanco al principio y al final de todas las cadenas de texto en todas las columnas del dataframe
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Convertir la columna fecha_de_beneficio a tipo datetime y asegurarse de que el formato sea día/mes/año
    df[['dia', 'mes', 'año']] = df['fecha_de_beneficio'].str.split('/', expand=True)
    mask = df['año'].str.len() == 4
    df.loc[mask, ['año', 'mes', 'dia']] = df.loc[mask, ['dia', 'mes', 'año']].values
    df['fecha_de_beneficio'] =  df['dia']+ '/' + df['mes'] + '/' + df['año']
    df = df.drop(['año', 'mes', 'dia'], axis=1)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"])

    # Eliminar espacios en blanco al principio y al final de los barrios
    df["barrio"] = df["barrio"].str.strip()   

    return df

# print(clean_data())
# print(clean_data().barrio.value_counts().to_list())
import csv

def exportar_a_csv(nombre_archivo, columnas, datos):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(columnas)
        escritor.writerows(datos)
    print(f"✅ Exportado correctamente a {nombre_archivo}")
import pandas as pd
from datetime import datetime
from db import clientPS



# Función para insertar datos en la tabla category
def insert_category(category_id, name):
    try: 
        conn= clientPS.dbClient()
        cur = conn.cursor()
        tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f"INSERT INTO category (category_id, name, created_at, updated_at) VALUES ({category_id}, '{name}', '{tiempo_actual}', '{tiempo_actual}')")
        conn.commit()
    except Exception as e:
        return f'Erroe conexió {e}'
    finally:
        conn.close()

# Función para insertar datos en la tabla subcategory
def insert_subcategory(subcategory_id, name, category_id):
    try:
        conn= clientPS.dbClient()
        cur = conn.cursor()
        tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f"INSERT INTO subcategory (subcategory_id, name, category_id, created_at, updated_at) VALUES ({subcategory_id}, '{name}', {category_id}, '{tiempo_actual}', '{tiempo_actual}')")
        conn.commit()
    except Exception as e:
        return f'Erroe conexió {e}'
    finally:
        conn.close()


# Función para insertar datos en la tabla product
def insert_product(product_id, name, description, company, price, units, subcategory_id):
    try:
        conn= clientPS.dbClient()
        cur = conn.cursor()
        tiempo_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(f"INSERT INTO product (product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({product_id}, '{name}', '{description}', '{company}', {price}, {units}, {subcategory_id}, '{tiempo_actual}', '{tiempo_actual}')")
        
        conn.commit()
    except Exception as e:
        return f'Erroe conexió {e}'
    finally:
        conn.close()



# Función para leer y cargar el archivo CSV 
def load(fitcherCSV): 
    try:
        conn = clientPS.dbClient()
        # Cargar los datos del CSV en un DataFrame de Pandas
        df = pd.read_csv(fitcherCSV.file, header=0 )
        
        # Iterar a través de las filas del DataFrame e insertar datos en la base de datos
        for index, row in df.iterrows():
            fila= row.to_dict()
            
            # Insertar datos en la base de datos
            insert_category(fila["id_categoria"], fila["nom_categoria"])
            insert_subcategory(fila["id_subcategoria"], fila["nom_subcategoria"], fila["id_categoria"])
            insert_product(fila["id_producto"], fila["nom_producto"], fila["descripcion_producto"], fila["companyia"], fila["precio"], fila["unidades"], fila["id_subcategoria"])

        return "Dades pujades"
    except Exception as e:
        # return f'Error de conexión: {e}'
        return ""
    finally:
        conn.close()  # Cierra la conexión en el bloque finally para garantizar que se cierre incluso si hay una excepción


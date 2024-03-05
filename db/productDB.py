from db import clientPS
import json

keys=['product_id', 'name', 'description', 'company', 'price', 'units', 'subcategory_id', 'created_at', 'updated_at']

def transformJson(datas):
    resultJson=[]
    for data in datas:
        count=0
        result={}
        for key in keys:
            result[key] = data[count]    
            count+=1
        resultJson.append(result)
    return resultJson

def consulta():
    try:
        conn= clientPS.dbClient()
    
        cur = conn.cursor()
    
        cur.execute("SELECT * FROM product")
        datas= cur.fetchall()
    
        resultJson = transformJson(datas)
        return resultJson
     
    except Exception as e:
        return f'Erroe conexió {e}'
        
    finally:
        conn.close()
    

def consultaId(id):
    try:
        conn= clientPS.dbClient()
    
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM product WHERE product_id = {id}')
        datas= cur.fetchall()
        resultJson=transformJson(datas)
        return resultJson
    
    except Exception as e:
        return f'Error conexió {e}'
        
    finally:
        conn.close()       
        

def createProduct(prod):
    try:
        conn= clientPS.dbClient()
    
        cur = conn.cursor()
        
                
        cur.execute(f"""INSERT INTO public.product
                (product_id, name, description, company, price, units, subcategory_id) 
                VALUES ({prod.product_id}, '{prod.name}', '{prod.description}', '{prod.company}', {prod.price}, {prod.units}, {prod.subcategory_id});""")
        conn.commit()

        return 'Producte pujat'
    except Exception as e:
        conn.rollback()
        return f'Error conexió {e}'
        
    finally:
        conn.close()
        
        
def deleteProduct(id):
    try:
        conn= clientPS.dbClient()
    
        cur = conn.cursor()
        
                
        cur.execute(f"""DELETE FROM public.product
	                WHERE product_id= {id}""")
        conn.commit()

        return 'Producte eliminat'
    except Exception as e:
        conn.rollback()
        return f'Error conexió {e}'
        
    finally:
        conn.close()
   
        
def updateProduct(id, prod):
    try:
        conn= clientPS.dbClient()
    
        cur = conn.cursor()
        
                
        cur.execute(f"""UPDATE public.product
	                SET product_id={prod.product_id}, name='{prod.name}', description='{prod.description}', company='{prod.company}', price={prod.price}, units={prod.units}, subcategory_id={prod.subcategory_id}
	                WHERE product_id= {id}""")
        conn.commit()

        return 'Producte actualitzat'
    except Exception as e:
        conn.rollback()
        return f'Error conexió {e}'
        
    finally:
        conn.close()


def allProducts():
    try:
        conn= clientPS.dbClient()
    
        cur = conn.cursor()
    
        cur.execute("""SELECT 
                    c.name AS categoria,
                    s.name AS subcategoria,
                    p.name AS nom_producte,
                    p.company AS marca_producte,
                    p.price AS preu
                    FROM product p
                    JOIN 
                    subcategory s ON p.subcategory_id = s.subcategory_id
                    JOIN 
                    category c ON s.category_id = c.category_id;""")
        datas= cur.fetchall()
        return datas
     
    except Exception as e:
        conn.rollback()
        return f'Erroe conexió {e}'
        
    finally:
        conn.close()

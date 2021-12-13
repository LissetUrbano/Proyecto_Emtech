#ESTE ES EL PROYECTO OFICIAL 

#Añadimos la función para importar otro programa 
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

if __name__ == "__main__": #Se define la condicion para empezar el programa 
    
    USUARIO_PERMITIDO = 'Administrador'#Definimos credenciales de inicio
    CONTRASENA = 'LifeStoreConfidential'


    INTENTOS = 3#Se crea el numero de veces que el usuario se puede equivocar para permanecer en el bucle while 

  
    while True:#Inicio de bucle 
        
        if INTENTOS == 0:#El contador se inicia en cero 
           
            exit()
        username = input("Ingrese su nombre de usuario:\n > ")#Se solicitan las credenciales de usuario 
        password = input("Ingrese la contraseña:\n > ")
        
        if username == USUARIO_PERMITIDO:#Se hace la comparación si el usuario existe dentro de nuestra variable 
        
            if password == CONTRASENA:
                
                break#Solo si los datos fueron los admitidos aqui termina el ciclo 
        else:
            
            INTENTOS = INTENTOS - 1
           
            print(f'\n!! Usuario/Contraseña incorrecto(s), {INTENTOS} restantes !!\n')

            
    #Comenzamos el codigo de las listas 
    print(f"\n\n\n¡Bienvenido! {USUARIO_PERMITIDO},\nA continuación se muestra el reporte administrativo de retutina ")

    prod_ventas = []
    cantidad_de_productos = len(lifestore_products)#Se obtiene la cantidad de datos existentes en el arreglo 
    cantidad_productos=str(cantidad_de_productos)#Se convierte el dato en cadena para que pueda imprimirse con texto 
    cantidad_de_busquedas=len(lifestore_searches)
    cantidad_busquedas=str(cantidad_de_busquedas)



    print("")
    print("")
    print("La cantidad de productos es:"+cantidad_productos)# se imprime texto con resultado de variable 
    print("")
    print("La cantida de busquedas registradas al momento son: "+cantidad_busquedas)
    print("")
    
#-------------Filtro de ventas reales -------

ventas = []  # se declara arreglo 
for sales in lifestore_sales: #iterable con tabla de donde debe salir la informacion 
    if sales[4] == 1:# indice de donde se tomara la información  y la condicion donde este no tomara en cuenta 
        continue #da la instrucción de continuar si la  condición es diferente 
    ventas.append(sales)#Arreglo con las ventas reales 

print("Total de productos salidos/ ventas registradas es :")
print(len(lifestore_sales))    
print("")
print("Total de ventas reales:")
print (len(ventas))
print("")
print("")
print("-----------VENTAS POR MES----------------")
#-----Ventas por mes----------
meses = [
    '/01/', '/02/', '/03/', '/04/', '/05/', '/06/',
    '/07/', '/08/', '/09/', '/10/', '/11/', '/12/'
    ]  #definicion de arreglo de manera manual 
    
ventas_por_mes = []
for mes in meses:
    lista_vacia = []
    ventas_por_mes.append(lista_vacia) # da la instrucción de añadir datos  recolectados 

for venta in ventas:
    
    id_venta = venta[0] #Se definen los datos que se utilizaran de la lista 
    fecha = venta[3]

    contador_de_mes = 0 #Se utilizara un contador y en este caso lo iniciamos en cero 

    for mes in meses:
        if mes in fecha:
            ventas_por_mes[contador_de_mes].append(id_venta)
            continue
        contador_de_mes = contador_de_mes + 1 
       
    
    

contador_de_mes = 0
for venta_mensual in ventas_por_mes:
    
    print(f'En el mes {meses[contador_de_mes]} se registraron: {len(venta_mensual)} ventas')
   
    contador_de_mes = contador_de_mes + 1

# ---------Ganancias mensuales --------
gancias_mensuales = []
for venta_mensual in ventas_por_mes:
    ganancia_del_mes = 0
    for id_venta in venta_mensual:
        indice_de_venta = id_venta - 1
        info_de_venta = lifestore_sales[indice_de_venta]

        id_prod = info_de_venta[1]
        indice_de_prod = id_prod - 1
        info_del_prod = lifestore_products[indice_de_prod]
        precio_de_prod = info_del_prod[2]
        ganancia_del_mes = ganancia_del_mes + precio_de_prod
    gancias_mensuales.append(ganancia_del_mes)


print("")
print("")
print("-------------INGRESOS MENSUALES SON-----------------")
contador_de_mes=0
n=0 #ya que las ganancias por mes se muestran todas en una lista este es contador para realizar el cambio segun el mes 
for ingresos_mes in range(12):
    print(f'Las ganancias en el mes {meses[contador_de_mes]} fueron:$ {gancias_mensuales[n]} ')
    contador_de_mes = contador_de_mes + 1
    n=n+1

print("----------------GANANCIA ANUAL --------------")
Ingreso_anual = sum(gancias_mensuales)
print("")
print("")
print(f"El ingreso anual es : ${Ingreso_anual}")
print("")


print("------------MESES CON MAYORES VENTAS------------") #checar el ordenamiento con sort

meses_mayores = []
for mes, venta_mensual in enumerate(ventas_por_mes):
    cant_ventas_mensuales = len(venta_mensual)
    sublista = [cant_ventas_mensuales, mes]
    meses_mayores.append(sublista)



meses_mayores.sort(reverse=True)

print(meses_mayores)

print("--------------------------------")

prod_reviews = []#reseñas de productos 
for prod in lifestore_products:# de la LISTA DE PRODUCTOS  sacamos los indices que utilizaremos 
    id_prod = prod[0] # el id que le corresponde al producto 
    sublista = [id_prod, 0 , 0]# se crea de la lista con el id y dos elementos de la misma vacios 
    prod_reviews.append(sublista)#score 
# en lugar de lifestroe_sales poner ventas[0]
for venta in lifestore_sales:# ahora se trabaja con  la LISTA DE VENTAS 
    id_prod = venta[1]# este indice tambien le corresponde al id del producto 
    review = venta[2]# este indice le corresponde a la  calificación 
    
    indice = id_prod - 1
    prod_reviews[indice][1] += review #asignamos el valor a la lista de score  en index 1 reseña 
    prod_reviews[indice][2] += 1 #Asignamos el valor a la lista score index 2 // cantidad de ventas 


for indice, lista in enumerate(prod_reviews):#enumerate nos permite tener control del iterable como del id siguiente 
   suma = lista[1] ## reseña 
   cant = lista[2] ## cantidad de ventas 
   if cant > 0:
       calf_prom = suma / cant
       prod_reviews[indice][1] = calf_prom# promedio de calificación de reseña 

    
# ************************Para obtener los mas vendidos:**************************
mejores_review= []
for lista in prod_reviews:
    #  
    sublista = [lista[2], lista[0], lista[1]]# la misma lista de review pero cambiando orden de iterables 
    mejores_review.append(sublista)     #quedando como  cantidad de ventas/ id de producto / promedio de reseña 

#-------------------PRODUCTOS CON RESEÑAS ---------------------------------
review_existente = []
for cuentan_con_review in mejores_review:
    if cuentan_con_review[2] == 0:
        continue
    review_existente.append(cuentan_con_review)#Arreglo con productos que tienen reseña



review_existente.sort()#Se ordenan 
print("Peores reseñas")
for top_menos_vendidos in review_existente[:5]:
    print(top_menos_vendidos) 



print("Mejores reseñas")
print("cantida de ventas, id producto, promedio de reseña ")
review_existente.sort(reverse=True)
for top_mas_vendidos in review_existente[:5]:
    print(top_mas_vendidos)  

print("")
print("-----------PRODUCTOS CON MEJORES Y PEORES VENTAS -------------")


prod_numeros_ventas = []#productos por numero de ventas 
for prod in lifestore_products:# de la LISTA DE PRODUCTOS  sacamos los indices que utilizaremos 
    id_prod = prod[0] # el id que le corresponde al producto 
    id_name=prod[1]#nombre del prodcuto 
    sublista = [id_prod, 0, id_name ]# se selecciona la poscion de los elementos en la nueva lista 
    prod_numeros_ventas.append(sublista)#score 

for venta in lifestore_sales:# ahora se trabaja con  la LISTA DE VENTAS 
    id_prod = venta[1]# este indice tambien le corresponde al id del producto 
    review = venta[2]# este indice le corresponde a la  calificación 
    
    indice = id_prod - 1
    prod_numeros_ventas[indice][1] += review #asignamos el valor a la lista de score  en index 1 reseña 
    

    
# Para obtener los productos top de mejorees y peores ventas :
ventas_product= []
for lista in prod_numeros_ventas:
    #  
    sublista = [lista[1], lista[0],lista[2]]# la misma lista de review pero cambiando orden de iterables 
    ventas_product.append(sublista)     #quedando como  cantidad de ventas/ id de producto / promedio de reseña 






tuvieron_ventas = [] # arreglo para que filtre lo que tuvieron ventas 
for cuentan_con_venta in ventas_product: 
    if cuentan_con_venta[0] == 0:
        continue
    tuvieron_ventas.append(cuentan_con_venta)#Arreglo con productos que tienen reseña



print("")
tuvieron_ventas.sort()
print("PRODUCTOS MENOS VENDIDOS")
print("cantida de ventas, id producto, nombre ")
for top_menos_vendidos in tuvieron_ventas[:5]:
    print(top_menos_vendidos) 

print("")

print("PRODUCTOS MÁS VENDIDOS ")
print("cantida de ventas, id producto, nombre ")
tuvieron_ventas.sort(reverse=True)
for top_mas_vendidos in tuvieron_ventas[:5]:
    print(top_mas_vendidos)  


#----------SECCION BUSQUEDAS DE LOS PRODUCTOS-------------
#-------------PRODUCTOS CON MAYORES Y MENORES BUSQUEDAS -------------------

prod_busquedas = []
for prod in lifestore_products:
    id_prod = prod[0]
    id_name=prod[1]
    sublista = [id_prod, 0 , 0,id_name]
    prod_busquedas.append(sublista)
# en lugar de lifestroe_sales poner ventas[0]
for venta in lifestore_searches:
    id_prod = venta[1]
    contar = venta[1]
    
    indice = id_prod - 1
    prod_busquedas[indice][1] += contar#indice para el conteo 
    prod_busquedas[indice][2] += 1  #posiblemente esta linea no me sirva pero la añadi por que sin ella no me respetaba la fusion de las listas 
    

buscados_a= []
for lista in prod_busquedas:
    sublista = [lista[2], lista[0], lista[3]]  #numero de busquedas, id de producto, nombre de producto 
    buscados_a.append(sublista)


tuvieron_busquedas = [] # arreglo para que filtre lo que tuvieron ventas 
for cuentan_con_busqueda in buscados_a: 
    if cuentan_con_busqueda[0] == 0:
        continue
    tuvieron_busquedas.append(cuentan_con_busqueda)#Arreglo con productos que tienen reseña



print("")
tuvieron_busquedas.sort()
print("PRODUCTOS MENOS BUSCADOS")
print("cantida de ventas, id producto, nombre ")
for top_menos_buscados in tuvieron_busquedas[:10]:
    print(top_menos_buscados) 


print("")
print("PRODUCTOS MAS BUSCADOS")
print("cantida de ventas, id producto, nombre ")
tuvieron_busquedas.sort(reverse=True)
for top_mas_buscados in tuvieron_busquedas[:10]:
    print(top_mas_buscados)  


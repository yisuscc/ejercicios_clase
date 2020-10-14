'''
Created on 14 oct. 2020

@author: jesus
'''
'''
Defina una función de nombre calcula_intereses que tenga tres parámetros: 
cantidad_base, tasa_interés (rango 0 a 1) y numero de años y muestre por pantalla:
 "Usted ha pedido un préstamo de XXXX euros, y, aplicando la tasa de interés XXX durante XXX años,
  pagará XXX de intereses, dando un total de XXXX euros", y devuelva la cantidad total a pagar como resultado del método. Recuerde que los intereses se calcularán de manera acumulativa, es decir:
Para cada año, calcule la cantidad de intereses de ese año, que se puede obtener como la cantidad_base *
 tasa de interés y añádasela al total. Cada año, la nueva cantidad base será el acumulado de la cantidad base + los intereses generados los años anteriores. 
 Tenga en cuenta que según la política de nuestro banco los préstamos cuya cantidad base sea menor de 50.000 euros están exentas de pagar intereses. 
 
 
 '''
def int_compuesto(CB, I,A):
    #interes en porcentaje
    if I>1 and I >0:
         I= I /100   
    CT = CB*(1+I)**A
    print ("Usted ha pedido un prestamo de ",CB,"euros aplicando la tasa de interes de ",I*100," %, durante ",A,"Años tiene que devolver",CT,"Euros")
    
    
print(int_compuesto(50,0.21,5))

def int_compuesto_v2(CB,I,A):
    CT = 0
    if I>1:
         I= I /100
    if CB >= 50000:
        CT =CB
        for b in range(0,A):
            CT = CT+ CT*I
    else: 
        CT= CB
    print ("Usted ha pedido un prestamo de ",CB,"euros aplicando la tasa de interes de ",I *100,"%, durante ",A,"Años tiene que devolver",CT,"Euros")
print(int_compuesto_v2(50,0.21,5))    
    
    
         



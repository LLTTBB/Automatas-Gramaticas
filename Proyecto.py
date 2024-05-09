import pprint
from FileControl import open_file, export_file
from UserManager import search_usuario
from SessionTime import RegexFecha, sum_session_time
import os
import tkinter as tk


# Luca Terranova - Abril Freytes - Carla Centeleghe - Abril Britos
#------------------------------------------------------------------

#Proyecto examen final Autómatas y Gramáticas
#------------------------------------------------------------------

'''Sobre la Base de Datos dada este codigo deberá hacer un seguimiento del Tiempo de Sesión (Session Time) de un usuario
en un período de tiempo establecido (Rango de Fechas). Debe incluir una lista de usuarios y la posibilidad de ingresar
un Rango de Fechas'''

#------------------------------------------------------------------
'''
El user ingresa un rango de fechas para limitar la busqueda de datos relacionados 
a un usuario en especifico, el cual tambien es ingresado mediante un input. Como resultado nos muestra
el usuario y el Session Time total del mismo en el rango de fechas establecido.
Luego se le pregunta si quiere cambiar el usuario y/o la fecha o si quiere finalizar el programa (cerrarlo) 
'''

if __name__ == "__main__":
    #diccionario de usuarios que se han conectado al menos una vez a la red
    dict_users = {1: 'c0174db3ed91', 2: 'cermen', 3: 'cnevera', 4: 'csegeview', 5:'druede', 6:'dsenchezw', 7:'e0d7eeed51ed', 8:'ecempesw', 9:'eeleridiew', 10:'eernendee.eunes', 
            11:'egenzelezvw', 12:'ejeimew', 13:'emennine', 14:'enem.endie', 15:'enrique.senchez', 16:'eperisiw', 17:'gbuchinw', 18:'gdiezw', 19:'gvillegesw', 20:'hcesedew',
            21:'hest/Dip-Senz-02', 22:'hperviuw', 23: 'Igebierne', 24:'Invitede', 25:'invitede-pansew', 26: 'jelberacinw', 27:'jemelinew', 28:'jlemedrid', 29:'jlepezw', 30:'jmelinew',
            31:'jsuoz', 32:'Jtenusw', 33:'jverges', 34:'lelberacin', 35:'leruizw', 36:'mdiezw', 37:'megilw', 38:'mercele.eernendezw', 39:'merriegew', 40:'mgiatti',
            41:'mjpence', 42:'mjsenzw', 43:'mleenw', 44:'mlpepenetw', 45:'mterasw', 46:'nceriew', 47:'nelivow', 48:'ngera', 49:'occe', 50:'odette',
            51:'pbenitezw', 52:'peble.ceia', 53:'pgelvenw', 54:'pgemez', 55:'ppriow', 56:'rmensur',57:'rvinci', 58:'sge', 59:'slercew', 60:'spintew', 61:'tecp87ed', 62:'tselemenw', 63:'umd', 64:'vermetinez'}

    while True:
        #Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #Hacer que el usuario elija el documento a analizar
        print("BIENVENIDO/A".center(80, "="))
        nombre_excel = input("\nIngrese el nombre del archivo excel que desea  abrir (DEBE INCLUIR .xlsx): ")
        hoja_excel = input("\nIngrese el nombre de la hoja que desea analizar en el excel elegido: ")
        data = open_file(nombre_excel, hoja_excel)
        
        #Mostramos los usuarios
        print("USUARIOS".center(80, "="))
        pprint.pprint(dict_users)
        print("".center(80, "="))

        #Pedimos que elija un usuario
        nu = int(input("\nIngrese el numero de usuario que quiere analizar: "))
        name = dict_users[nu]
        user_info = search_usuario(name, data)

        #Pedir el ingreso de una fecha inicial y comprobar su validez
        fecha_1 = str(input("\nIngrese la fecha de inicio (FORMATO YYYY-MM-DD): "))
        fecha_1 = RegexFecha(fecha_1)

        #Ingreso de una fecha final y comprobar su validez
        fecha_2 = str(input("\nIngrese la fecha final (FORMATO YYYY-MM-DD): "))
        fecha_2 = RegexFecha(fecha_2)

        #SessionTime final con los datos ingresados
        st = sum_session_time(user_info, fecha_1, fecha_2)

        #Mostramos el resultado
        print("==================================")
        print(" SESSION TIME TOTAL E INFORMACIÓN DADA ".center(80, "="))
        print(f"Usuario: {name}")
        print(f"Fecha de inicio: {fecha_1}")
        print(f"Fecha de final: {fecha_2}")
        print(f"SessionTime total: {st} UT")

        #Pregunta si se quiere exportar
        export = input("\n¿Desea exportar la busqueda en formato .xlsx (Excel) [RESPONDER CON 'Y' EN CASO AFIRMATIVO O CON 'N' EN CASO NEGATIVO]?: ")
        if export == 'Y':
                export_file(name, fecha_1, fecha_2, st)
        
        #Pregunta si desea hacer otra busqueda
        cambiar_user = input("\n¿Desea hacer otra busqueda[Y/N]?: ")
        if cambiar_user =='N':
                break


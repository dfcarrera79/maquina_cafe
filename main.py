from menu import Menu
from maquina_de_cafe import MaquinaCafe
from monedero import Monedero

menu = Menu()
maquina_de_cafe = MaquinaCafe()
monedero = Monedero()

on = True

while on:
    opciones = menu.optener_opciones()
    eleccion = input(f'¿Que tipo de café quieres? {opciones}: ')
    if eleccion == 'ninguna' or eleccion == 'Ninguna':
        on = False
    elif eleccion == 'reportar' or eleccion == 'Reportar':
        maquina_de_cafe.reporte()
        monedero.reporte()
    else:
        bebida = menu.encontrar_bebida(eleccion)

        if maquina_de_cafe.recursos_suficientes(bebida) and monedero.hacer_pago(bebida.costo):
            maquina_de_cafe.hacer_cafe(bebida)

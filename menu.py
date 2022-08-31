class IngredientesMenu:
    """Modela las bebidas del menu de la maquina de café."""

    def __init__(self, nombre, agua, leche, cafe, costo):
        self.nombre = nombre
        self.costo = costo
        self.ingredientes = {
            "agua": agua,
            "leche": leche,
            "cafe": cafe
        }


class Menu:
    """Modela el Menu con las bebidas."""

    def __init__(self):
        self.menu = [
            IngredientesMenu(nombre="late", agua=200,
                             leche=150, cafe=24, costo=2.5),
            IngredientesMenu(nombre="espreso", agua=50,
                             leche=0, cafe=18, costo=1.5),
            IngredientesMenu(nombre="capuchino", agua=250,
                             leche=50, cafe=24, costo=3),
        ]

    def optener_opciones(self):
        """Returna todos los nomnbre de las opciones disponibles en el menu"""
        opciones = ""
        for opcion in self.menu:
            opciones += f"{opcion.nombre}/"
        return opciones

    def encontrar_bebida(self, orden_nombre):
        """Busca en el menú una bebida en particular por nombre. Devuelve ese elemento si existe, de lo contrario devuelve Ninguno"""
        for opcion in self.menu:
            if opcion.nombre == orden_nombre:
                return opcion
        print("Lo siento esa opción no está disponible.")


#
#
#
# from dataclasses import dataclass, field


# @dataclass
# class IngredientesMenu:
#     # espresso/latte/cappuccino
#     nombre: str
#     costoo: float
#     ingredientes: dict


# ingredientes1 = IngredientesMenu(
#     'late', 2.5, {"agua": 200, "leche": 150, "cafe": 24})
# ingredientes2 = IngredientesMenu(
#     'espresso', 1.5, {"agua": 50, "leche": 0, "cafe": 18})
# ingredientes3 = IngredientesMenu(
#     'cappuccino', 3, {"agua": 250, "leche": 50, "cafe": 24})

# # print(ingredientes1.nombre)


# @dataclass
# class Menu:
#     # Esta clase contiene las bebidas espresso/latte/cappuccino
#     # my_list: list[object] = field(default_factory=list)
#     my_list: list = []
# #     ]

#     def cafes(self):
#         # funcion para obtener los tipos de cafe
#         opciones = 'espresso/latte/cappuccino/'
#         # for bebida in self.menu:
#         #     opciones += f'{bebida.nombre}'
#         return opciones

#     def encontrar_bebida(self, opcion):
#         # Busca una bebida en particular dentro del menu.
#         for bebida in self.menu:
#             if bebida.nombre == opcion:
#                 return bebida
#             else:
#                 print('¡Ha elegido una opción incorrecta!')


# menu = Menu()

# menu.my_list += [ingredientes1, ingredientes2, ingredientes3]
# print(menu.my_list)


# # class MenuItem:
# #     """Models each Menu Item."""

# #     def __init__(self, name, agua, leche, cafe, cost):
# #         self.name = name
# #         self.cost = cost
# #         self.ingredients = {
# #             "water": water,
# #             "milk": milk,
# #             "coffee": coffee
# #         }


# # class Menu:
# #     """Models the Menu with drinks."""

# #     def __init__(self):
# #         self.menu = [
# #             MenuItem(name="late", water=200, milk=150, coffee=24, cost=2.5),
# #             MenuItem(name="espreso", water=50, milk=0, coffee=18, cost=1.5),
# #             MenuItem(name="capuchino", water=250, milk=50, coffee=24, cost=3),
# #         ]

# #     def get_items(self):
# #         """Returns all the names of the available menu items"""
# #         options = ""
# #         for item in self.menu:
# #             options += f"{item.name}/"
# #         return options

# #     def find_drink(self, order_name):
# #         """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
# #         for item in self.menu:
# #             if item.name == order_name:
# #                 return item
# #         print("Sorry that item is not available.")


# # menu = Menu()
# # print(menu.get_items())

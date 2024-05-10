# Prueba técnica realizada por Sandra Moreno Fuentes.
# Utilizaremos un contexto de gestión de viñedos, con datos que representan gerentes, variedades de uvas, y registros de parcelas de viñedos.

class GestionDeVinedos:
    """
    Clase que gestiona la información y gestiones de los viñedos.

    Esta clase contiene los gerentes, las variedades de uvas, los viñedos y su correspondinete información.
    Permite sacar una lista de identificadores de gerentes, gerentes ordenados por nombre, área total por variedad de uva,
    área total administrada por gerente y los viñedos con sus correspondientes gerentes.
    """

    def __init__(self, managers, grapes, vineyards, vineyards_info):
        """
        Inicializa la clase GestionDeVinedos con los datos de los gerentes, uvas, viñedos y su información correspondiente.

        :param managers: Lista de diccionarios donde cada uno representa un gerente.
        :param grapes: Lista de diccionarios dode cda uno representa una variedad de uva diferente.
        :param vineyards: Lista de diccionarios donde cada uno representa una parcela de viñedo diferente.
        :param vineyards_info: Lista de diccionarios con informaciín adicional de los viñedos.
        """

        self.managers = managers
        self.grapes = grapes
        self.vineyards = vineyards
        self.vineyards_info = vineyards_info

    def lista_ids_managers(self):
        """
        Devuelve una lista de los identificadores de todos los agentes.

        :return: Lista de enteros que representan los identificadores de los gerentes.
        """
        return [manager['id'] for manager in self.managers]

    def managers_ordenados_nombres(self):
        """
        Devuelve una lista de los números fiscales de los gerentes, ordenados alfabeticamente por su nombre.

        :return: Lista de strings con los números fiscales de los gerentes, ordenados alfabeticamente por nombre.
        """
        sorted_managers = sorted(self.managers, key=lambda x: x["name"])
        tax_numbers = [manager["tax_number"] for manager in sorted_managers]
        return tax_numbers
    def area_total_variedad_uvas(self):
        """
        Genera un diccionario donde las claves son los nombres de las uvas y los valores son la suma total del area plantada para cada variedad de uva.

        :return: Diccionario donde cada clave es el nombre de una variedad de uva y el valor es el area total cultivada.
        """
        grape_names = {grape['id']: grape['name'] for grape in self.grapes}
        grape_areas = {grape['name']: 0 for grape in self.grapes}
        for vineyard in self.vineyards:
            grape_name = grape_names[vineyard['grape_id']]
            grape_areas[grape_name] += vineyard['area']

        return grape_areas

    def area_total_adm_manager(self):
        """
        Crea un diccionario donde cad clave es el nombre de un gerente y el valor es la suma total del area qe administra.

        :return: Diccionario con el nombre de cada gerente como clave y el área total que administra como valor.
        """
        manager_names = {manager['id']: manager['name'] for manager in self.managers}
        manager_areas = {manager['name']: 0 for manager in self.managers}

        for vineyard in self.vineyards:
            manager_name = manager_names[vineyard['manager_id']]
            manager_areas[manager_name] += vineyard['area']

        return manager_areas
    def vinedos_y_gerentes(self):
        """
        Retorna un diccionario dode las claves son los nombres de los viñedos y los valores son listas de nombres de sus gerentes, ordenados alfabeticamente.

        :return: Diccionario donde cada clave es el nombre de un viñedo y el valor es una lista de nombres de gerentes que lo administran, ordenados alfabéticamente.
        """
        vineyard_names = {info['id']: info['name'] for info in self.vineyards_info}
        manager_names = {manager['id']: manager['name'] for manager in self.managers}
        vineyard_managers = {info['name']: set() for info in self.vineyards_info}

        for vineyard in self.vineyards:
            vineyard_name = vineyard_names[vineyard['vineyard_id']]
            manager_name = manager_names[vineyard['manager_id']]
            vineyard_managers[vineyard_name].add(manager_name)

        for vineyard_name in vineyard_managers:
            vineyard_managers[vineyard_name] = sorted(vineyard_managers[vineyard_name])

        return vineyard_managers

if __name__ == "__main__":
    vm = GestionDeVinedos(
        managers=[
            {"id": 1, "tax_number": "132254524", "name": "Miguel Torres"},
            {"id": 2, "tax_number": "143618668", "name": "Ana Martín"},
            {"id": 3, "tax_number": "78903228", "name": "Carlos Ruiz"},
        ],
        grapes=[
            {"id": 1, "name": "Tempranillo"},
            {"id": 2, "name": "Albariño"},
            {"id": 3, "name": "Garnacha"},
        ],
        vineyards=[
            {"manager_id": 1, "vineyard_id": 1, "grape_id": 1, "year_planted": 2019, "area": 1500},
            {"manager_id": 2, "vineyard_id": 2, "grape_id": 2, "year_planted": 2021, "area": 9000},
            {"manager_id": 3, "vineyard_id": 1, "grape_id": 3, "year_planted": 2020, "area": 3000},
            {"manager_id": 1, "vineyard_id": 2, "grape_id": 1, "year_planted": 2020, "area": 2000},
            {"manager_id": 3, "vineyard_id": 2, "grape_id": 3, "year_planted": 2021, "area": 1000},
        ],
        vineyards_info=[
            {"id": 1, "name": "Viña Esmeralda"},
            {"id": 2, "name": "Bodegas Bilbaínas"},
        ]
    )

    print("Lista de Identificadores de Gerentes:")
    print(vm.lista_ids_managers())
    print("\nGerentes Ordenados por Nombre:")
    print(vm.managers_ordenados_nombres())
    print("\nÁrea Total por Variedad de Uva:")
    print(vm.area_total_variedad_uvas())
    print("\nÁrea Total Administrada por Gerente:")
    print(vm.area_total_adm_manager())
    print("\nViñedos y Sus Gerentes:")
    print(vm.vinedos_y_gerentes())

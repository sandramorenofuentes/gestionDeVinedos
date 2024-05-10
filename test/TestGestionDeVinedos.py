import unittest
from src.gestionDeVinedos import GestionDeVinedos


class TestGestionDeVinedos(unittest.TestCase):
    def setUp(self):
        # Datos para las pruebas
        self.gerentes = [
            {"id": 1, "tax_number": "132254524", "name": "Miguel Torres"},
            {"id": 2, "tax_number": "143618668", "name": "Ana Martín"},
            {"id": 3, "tax_number": "78903228", "name": "Carlos Ruiz"},
        ]
        self.uvas = [
            {"id": 1, "name": "Tempranillo"},
            {"id": 2, "name": "Albariño"},
            {"id": 3, "name": "Garnacha"},
        ]
        self.vinedos = [
            {"manager_id": 1, "vineyard_id": 1, "grape_id": 1, "year_planted": 2019, "area": 1500},
            {"manager_id": 2, "vineyard_id": 2, "grape_id": 2, "year_planted": 2021, "area": 9000},
            {"manager_id": 3, "vineyard_id": 1, "grape_id": 3, "year_planted": 2020, "area": 3000},
            {"manager_id": 1, "vineyard_id": 2, "grape_id": 1, "year_planted": 2020, "area": 2000},
            {"manager_id": 3, "vineyard_id": 2, "grape_id": 3, "year_planted": 2021, "area": 1000},
        ]
        self.info_vinedos = [
            {"id": 1, "name": "Viña Esmeralda"},
            {"id": 2, "name": "Bodegas Bilbaínas"},
        ]
        self.vm = GestionDeVinedos(self.gerentes, self.uvas, self.vinedos, self.info_vinedos)

    def test_lista_ids_gerentes(self):
        ids_esperados = [1, 2, 3]
        resultado = self.vm.lista_ids_managers()
        self.assertEqual(resultado, ids_esperados, "Debería devolver la lista de IDs de los gerentes")

    def test_gerentes_ordenados_nombres(self):
        numeros_fiscales_esperados = ["143618668", "78903228", "132254524"]
        resultado = self.vm.managers_ordenados_nombres()
        self.assertEqual(resultado, numeros_fiscales_esperados,
                         "Debería devolver los números fiscales ordenados por nombre")

    def test_area_total_variedad_uvas(self):
        areas_esperadas = {
            "Tempranillo": 3500,
            "Albariño": 9000,
            "Garnacha": 4000,
        }
        resultado = self.vm.area_total_variedad_uvas()
        self.assertEqual(resultado, areas_esperadas, "Debería devolver las áreas totales por variedad de uva")

    def test_area_total_adm_gerente(self):
        areas_esperadas = {
            "Miguel Torres": 3500,
            "Ana Martín": 9000,
            "Carlos Ruiz": 4000,
        }
        resultado = self.vm.area_total_adm_manager()
        self.assertEqual(resultado, areas_esperadas,
                         "Debería devolver las áreas totales administradas por cada gerente")

    def test_vinedos_y_gerentes(self):
        resultado_esperado = {
            "Viña Esmeralda": ["Carlos Ruiz", "Miguel Torres"],
            "Bodegas Bilbaínas": ["Ana Martín", "Carlos Ruiz", "Miguel Torres"],
        }
        resultado = self.vm.vinedos_y_gerentes()
        self.assertEqual(resultado, resultado_esperado, "Debería devolver los viñedos y sus gerentes ordenados")


if __name__ == '__main__':
    unittest.main()

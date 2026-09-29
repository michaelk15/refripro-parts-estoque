import unittest
from app import app, pecas


class TestEstoque(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.cliente = app.test_client()
        pecas.clear()

    def test_pagina_inicial(self):
        resposta = self.cliente.get("/")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"REFRIPR", resposta.data)

    def test_cadastrar_peca(self):
        resposta = self.cliente.post(
            "/cadastrar",
            data={"nome": "Compressor", "quantidade": "5"},
            follow_redirects=True
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(pecas), 1)
        self.assertEqual(pecas[0]["nome"], "Compressor")
        self.assertEqual(pecas[0]["quantidade"], 5)

    def test_excluir_peca(self):
        pecas.append({"nome": "Termostato", "quantidade": 2})

        resposta = self.cliente.get(
            "/excluir/0",
            follow_redirects=True
        )

        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(pecas), 0)


if __name__ == "__main__":
    unittest.main()

import unittest
from varasto import Varasto
#Joudut huomioimaan ainakin tapaukset, joissa varastoon yritetään laittaa liikaa tavaraa ja varastosta yritetään ottaa enemmän kuin siellä on

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_negatiivinen_maara_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisaa_liikaa_tayttaa_koko_varaston(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_negatiivinen_maara_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ota_liikaa_palauttaa_koko_saldon(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(100), 5)

    def test_ota_liikaa_tyhjentaa_varaston(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(100)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivinen_tilavuus_nollataan(self):
        self.assertAlmostEqual(Varasto(-10).tilavuus, 0)

    def test_negatiivinen_alkusaldo_nollataan(self):
        self.assertAlmostEqual(Varasto(10, -10).saldo, 0)

    def test_tilavuus_alkusaldo(self):
        self.assertAlmostEqual(Varasto(10, 10).saldo, 10)

    def test_tulostus(self):
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")

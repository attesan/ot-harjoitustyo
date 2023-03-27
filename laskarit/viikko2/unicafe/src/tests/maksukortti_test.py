import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_luotu_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_saldon_lataus_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_rahan_ottaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")

    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertNotEqual(str(self.maksukortti), "Kortilla on rahaa -1.00 euroa")

    def test_ota_rahaa_palauttaa_oikean_arvon_onnistumisesta(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_ota_rahaa_palauttaa_oikean_arvon_epaonnistumisesta(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)

    def test_negatiivinen_rahan_lisays_ei_muuta_saldoa(self):
        self.maksukortti.lataa_rahaa(-100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
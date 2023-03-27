import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(500)
        self.vajaaKortti = Maksukortti(100)

    #Luotu oikein testit
    def test_kassan_rahat_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_maukkaat_lukumaara_luotu_oikein(self):
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_edulliset_lukumaara_luotu_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)
    
    #Käteisosto testit
    def test_kateisosto_kasvattaa_kassaa_edullisella(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_kateisosto_kasvattaa_kassaa_maukkaalla(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_kateisosto_edullisten_maara_kasvaa_onnistuessa(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateisosto_maukkaiden_maara_kasvaa_onnistuessa(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_vaihtoraha_oikein_edullisella(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(300), 60)
    
    def test_kateisosto_vaihtoraha_oikein_maukkaalla(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)

    def test_kateisosto_vaihtoraha_kasvattaa_kassaa_oikein_edullisella(self):
        self.kassa.syo_edullisesti_kateisella(340)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_kateisosto_vaihtoraha_kasvattaa_kassaa_oikein_maukkaalla(self):
        self.kassa.syo_maukkaasti_kateisella(440)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_kateisosto_maksu_ei_riita_edullisella_toimii_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100), 100)

    def test_kateisosto_maksu_ei_riita_maukkalla_toimii_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(100), 100)

    def test_kateisosto_edullisten_maara_ei_kasva_epaonnistumisesta(self):
        self.kassa.syo_edullisesti_kateisella(0)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisosto_maukkaiden_maara_ei_kasva_epaonnistumisesta(self):
        self.kassa.syo_maukkaasti_kateisella(0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_kassa_ei_kasva_epaonnistumisessa_edullisella(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kateisosto_kassa_ei_kasva_epaonnistuessa_maukkaalla(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    #Korttiosto testit    
    def test_korttiosto_kasvattaa_kassaa_edullisella(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_korttiosto_kasvattaa_kassaa_maukkaalla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_korttiosto_kortin_rahamaara_oikein_edullisella(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.60 euroa")

    def test_korttiosto_kortin_rahamaara_oikein_maukkaalla(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 1.00 euroa")

    def test_korttiosto_edullisten_maara_kasvaa_onnistuessa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_korttiosto_maukkaiden_maara_kasvaa_onnistuessa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_korttiosto_onnistuu_edullisella_toimii_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

    def test_korttiosto_onnistuu_maukkalla_toimii_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

    def test_korttiosto_maksu_ei_riita_edullisella_toimii_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.vajaaKortti), False)

    def test_korttiosto_maksu_ei_riita_maukkalla_toimii_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.vajaaKortti), False)

    def test_korttiosto_edullisten_maara_ei_kasva_epaonnistumisesta(self):
        self.kassa.syo_edullisesti_kortilla(self.vajaaKortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_korttiosto_maukkaiden_maara_ei_kasva_epaonnistumisesta(self):
        self.kassa.syo_maukkaasti_kortilla(self.vajaaKortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_korttiosto_kassa_ei_kasva_epaonnistumisessa_edullisella(self):
        self.kassa.syo_edullisesti_kortilla(self.vajaaKortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_kassa_ei_kasva_epaonnistuessa_maukkaalla(self):
        self.kassa.syo_maukkaasti_kortilla(self.vajaaKortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_kortin_rahamaara_oikein_epaonnistuessa_edullisella(self):
        self.kassa.syo_edullisesti_kortilla(self.vajaaKortti)
        self.assertEqual(str(self.vajaaKortti), "Kortilla on rahaa 1.00 euroa")

    def test_korttiosto_kortin_rahamaara_oikein_epaonnistuessa_maukkaalla(self):
        self.kassa.syo_maukkaasti_kortilla(self.vajaaKortti)
        self.assertEqual(str(self.vajaaKortti), "Kortilla on rahaa 1.00 euroa")

    #Kortti testit

    def test_kortille_rahaa_saldo_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")
    
    def test_kortille_rahaa_kassa_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100100)

    def test_kortille_rahaa_epaonnistuu(self):
        self.assertEqual(self.kassa.lataa_rahaa_kortille(self.kortti, -100), None)

    def test_kortille_rahaa_epaonnistuu_kassa_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
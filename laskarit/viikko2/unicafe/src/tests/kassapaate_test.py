import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassapaate = Kassapaate()
		self.maksukortti = Maksukortti(1000)

	def test_edulliseen_on_rahaa(self):
		self.kassapaate.syo_edullisesti_kateisella(240)

		self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
		self.assertEqual(self.kassapaate.edulliset,1)
	
	def test_edulliseen_ei_rahaa(self):
		self.kassapaate.syo_edullisesti_kateisella(0)

		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(self.kassapaate.edulliset,0)


	def test_maukkaaseen_on_rahaa(self):
		self.kassapaate.syo_maukkaasti_kateisella(400)

		self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
		self.assertEqual(self.kassapaate.maukkaat,1)

	def test_maukkaaseen_ei_rahaa(self):
		self.kassapaate.syo_maukkaasti_kateisella(0)

		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(self.kassapaate.maukkaat,0)


	def test_edulliseen_on_saldoa(self):
		arvooo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(self.kassapaate.edulliset,1)
		self.assertEqual(arvooo, True)
	
	def test_edulliseen_ei_saldoa(self):
		maksukortti2 = Maksukortti(1)
		self.kassapaate.syo_edullisesti_kortilla(maksukortti2)
		arvoo = False
		arvoo2 = "False"

		self.assertEqual(str(maksukortti2), "Kortilla on rahaa 0.01 euroa")
		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(self.kassapaate.edulliset,0)
		self.assertFalse( arvoo, arvoo2)

	def test_maukkaaseen_on_saldoa(self):
		arvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(self.kassapaate.maukkaat,1)
		self.assertEqual(arvo, True)
	
	def test_maukkaaseen_ei_saldoa(self):
		maksukortti3 = Maksukortti(1)
		self.kassapaate.syo_maukkaasti_kortilla(maksukortti3)
		arvoo = False
		arvoo2 = "False"

		self.assertEqual(str(maksukortti3), "Kortilla on rahaa 0.01 euroa")
		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(self.kassapaate.edulliset,0)
		self.assertFalse(arvoo, arvoo2)

	def test_rahan_lataus_kortille(self):
		self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)


		self.assertEqual(self.kassapaate.kassassa_rahaa,100200)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")


	def test_rahan_lataus_ei_onnistu(self):
		self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -7)

		self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
		self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
		



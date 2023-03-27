import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_lataa(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")
    
    def test_vaheneeko(self):
        self.maksukortti.ota_rahaa(200)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")

    def test_ottaa(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 8.00 euroa")
        

    def test_ei_ota_rahaa(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa") 

    def test_rahat_riitti(self):
        totuusarvo = self.maksukortti.ota_rahaa(200)

        self.assertEqual(str(totuusarvo), "True")
        

    def test_rahat_ei_riittany(self):
        totuusarvo = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(str(totuusarvo), "False")

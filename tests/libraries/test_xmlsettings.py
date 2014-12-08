'''
Created on 7/12/2014

@author: Jafeth Garcia
'''
import unittest
from libraries import XMLSettings


class TestXMLSettings(unittest.TestCase):

    def setUp(self):
        self.path = "../../config/config.xml"
        unittest.TestCase.setUp(self)

    def test_data_can_be_stored(self):
        xml = XMLSettings(self.path)

        xml.put('window/size/width', 800)
        xml.put('window/size/height', 600)
        xml.save()

        self.assertEqual(xml.get("window/size/width", 1024), 800)

    def test_data_can_read(self):
        xml = XMLSettings(self.path)

        self.assertEqual("localhost", xml.get("mysql/host"))


if __name__ == "__main__":
    unittest.main()

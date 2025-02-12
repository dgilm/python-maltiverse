#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import json
from maltiverse import Maltiverse
import time

class TestMaltiverse(unittest.TestCase):
   """Test for Maltiverse class"""
   def __init__(self, *args, **kwargs):
       super(TestMaltiverse, self).__init__(*args, **kwargs)
       self.email = "foo@bar.com"
       self.password = "fakepassword"


   def test_ip_get(self):
        """ Test that performs an ip lookup"""
        m = Maltiverse()
        item = m.ip_get('1.1.1.1')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('ip_addr' in item)

   def test_ip_put_delete(self):
        """ Test that performs a IP put and a delete """
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        ip_dict = {
          "blacklist": [
            {
              "description": "test",
              "source": "test"
            }
          ],
          "classification": "whitelisted",
          "ip_addr": "60.60.60.60",
          "type": "ip"
        }
        item = m.ip_put(ip_dict)
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'IP created' or item['message'] == 'IP updated' )

        item = m.ip_delete(ip_dict['ip_addr'])
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'IP deleted')


   def test_hostname_get(self):
        """ Test that performs an hostname lookup"""
        m = Maltiverse()
        item = m.hostname_get('samuest.ru')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('hostname' in item)


   def test_hostname_put_delete(self):
        """ Test that performs a hostname put and a delete """
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        hostname_dict = {
          "blacklist": [
            {
              "description": "test",
              "source": "test"
            }
          ],
          "classification": "malicious",
          "domain": "test.com",
          "hostname": "www.test.com",
          "tld": "com",
          "type": "hostname",
        }
        item = m.hostname_put(hostname_dict)
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'Hostname created' or item['message'] == 'Hostname updated' )

        #Wait for two seconds to permit DB transaction happen
        time.sleep(2)

        item = m.hostname_delete(hostname_dict['hostname'])
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'Hostname deleted')


   def test_url_get(self):
        """ Test that performs an url lookup"""
        m = Maltiverse()
        item = m.url_get('https://www.welsfagmary-online.com/')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('url' in item)

   def test_url_put_delete(self):
        """ Test that performs a url put and a delete """
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        url_dict = {
          "blacklist": [
            {
              "description": "test",
              "source": "test"
            }
          ],
          "domain": "test.com",
          "hostname": "www.test.com",
          "type": "url",
          "url": "http://www.test.com/test.php"
        }
        item = m.url_put(url_dict)
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'Url created' or item['message'] == 'Url updated')

        #Wait for two seconds to permit DB transaction happen
        time.sleep(2)

        item = m.url_delete(url_dict['url'])
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'Url deleted')

   def test_sample_get(self):
        """ Test that performs an sample lookup"""
        m = Maltiverse()
        item = m.sample_get('3b9d4f379e59cfc5ed8217424c833fbd16e7bff322c2ea696870061bbd2c5273')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('sha256' in item)

   def test_sample_put_delete(self):
        """ Test that performs a sample put and a delete """
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        sample_dict = {
          "blacklist": [
            {
              "description": "test",
              "source": "test"
            }
          ],
          "classification": "whitelisted",
          "filename": [
            "test"
          ],
          "md5": "00000000000000000000000000000000",
          "sha1": "0000000000000000000000000000000000000000",
          "sha256": "0000000000000000000000000000000000000000000000000000000000000000",
          "sha512": "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "type": "sample"
        }
        item = m.sample_put(sample_dict)
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'Sample created' or item['message'] == 'Sample updated' )

        #Wait for two seconds to permit DB transaction happen
        time.sleep(2)

        item = m.sample_delete(sample_dict['sha256'])
        print item
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('status' in item)
        self.assertTrue(item['status'] == 'success')
        self.assertTrue(item['message'] == 'Sample deleted')

   '''
   def test_sample_get_by_md5(self):
        m = Maltiverse()
        item = m.sample_get_by_md5('47d48310504661dceb6283ca02469a96')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('md5' in item)
   '''

   def test_ip_get_with_authentication(self):
        """ Test that performs an ip lookup with authenticantion"""
        m = Maltiverse()

        m.login(email=self.email, password=self.password)

        item = m.ip_get('1.1.1.1')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('ip_addr' in item)

   def test_hostname_get_with_authentication(self):
        """ Test that performs an hostname lookup with authenticantion"""
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        item = m.hostname_get('samuest.ru')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('hostname' in item)

   def test_url_get_with_authentication(self):
        """ Test that performs an url lookup with authenticantion"""
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        item = m.url_get('https://www.welsfagmary-online.com/')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('url' in item)

   def test_sample_get_with_authentication(self):
        """ Test that performs an sample lookup with authenticantion"""
        m = Maltiverse()
        m.login(email=self.email, password=self.password)
        item = m.sample_get('3b9d4f379e59cfc5ed8217424c833fbd16e7bff322c2ea696870061bbd2c5273')
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        self.assertTrue('sha256' in item)

   def test_search(self):
        """ Test that performs search into the platform"""
        m = Maltiverse()
        print m.login(email=self.email, password=self.password)
        item = m.search('country_code:"CN"', fr=0, size=2)
        self.assertTrue(isinstance(str(item), str))
        self.assertTrue(isinstance(item, dict))
        print len(item['hits']['hits'])

if __name__ == '__main__':
    unittest.main()

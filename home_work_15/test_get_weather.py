import sys
sys.path.append('/home/oleg/PycharmProjects/pythonProject')
import json
import unittest
from unittest.mock import patch, MagicMock
from zadneprovskyi_oleg_hm_15 import get_weather




class GetWeatherTest(unittest.TestCase):

    @patch('zadneprovskyi_oleg_hm_15.requests')
    def test_success(self, requests_mock):

        with open('/home/oleg/PycharmProjects/pythonProject/response_succ_file.json') as f:
            prepared_data = json.load(f)

        req_resp_mock = MagicMock()
        req_resp_mock.json.return_value = prepared_data

        requests_mock.get.return_value = req_resp_mock
        self.assertEqual(get_weather('London'), 'temperature is 20.95C, pressure is 1022, weather is scattered clouds')

    @patch('zadneprovskyi_oleg_hm_15.requests')
    def test_unsuccess(self, requests_mock):
        req_resp_mock = MagicMock()
        req_resp_mock.json.return_value = {'message': 'city not found'}

        requests_mock.get.return_value = req_resp_mock
        self.assertEqual(get_weather('L'), 'city not found')


#if __name__ == '__main__':
#    unittest.main()
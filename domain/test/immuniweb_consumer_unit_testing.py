import unittest
import mock
from domain.main.file_processor import execute_consumer


# fyi https://stackoverflow.com/questions/27571429/python-how-can-i-override-a-complicated-function-during-unittest


class TestMyModule(unittest.TestCase):
    ClientListResult = '<cursor object at 0x7f7e85d07b50; closed: 0>'
    getIncidentParam = {'client_id': '9', 'client_name': 'Easy Solutions', 'url': 'http:www.DTPDiscoverycoMainTest.com', 'discovery_id': 4631253, 'discovery_tab_type': 'incidents', 'discovery_authorization': 'Basic OTgzNTM5MzIzOjZZTVhNR1BLRkI4MU1YNkpIWDRXQ09RN0kyQVBIRTcy', 'discovery_cookie': 't=Cgs7Hl7qkpal9gPCjCKAAg==; tr_firstpage=https%3A%2F%2Fportal.immuniweb.com%2Fclient%2F; s_token=BZ75QVPCSXHMNFKF26MCMNO1I36Y13F8', 'last_id_accepted': 1986833}






    @mock.patch('data_connect.main.ReadParamsPg.getClientList')
    def test_1(self, mocked):
        print('test 1')
        mocked.return_value = self.ClientListResult,'',False
        val1  = execute_consumer()
        self.assertEqual(True,val1)

    @mock.patch('consumer.inmuni_web_consumer.getIncidents')
    def test_2(self, mocked):
        print('test 2')
        mocked.return_value = '',False
        val1  = execute_consumer()
        self.assertEqual(True,val1)

    @mock.patch('data_connect.main.CreateResultPg.saveResultDb')
    def test_3(self, mocked):
        print('test 3')
        mocked.return_value = '',False
        val1  = execute_consumer()
        self.assertEqual(True,val1)

    @mock.patch('domain.main.ticketing_handler.start_ticket_life_cicle')
    def test_4(self, mocked):
        print('test 4')
        mocked.return_value = '',False
        val1  = execute_consumer()
        self.assertEqual(True,val1)

    @mock.patch('data_connect.main.ReadParamsPg.get_cursor')
    def test_5(self, mocked):
        print('test 5')
        mocked.return_value = '',False
        val1  = execute_consumer()
        self.assertEqual(False,val1)




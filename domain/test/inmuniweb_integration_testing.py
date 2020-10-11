import unittest

from utils.db_connection import get_cursor
from domain.main.file_processor import execute_consumer

def check_results_table_size():
    sql_query = "SELECT  count(id) from results_inmuniweb;"

    cursor = get_cursor('db_inmuniWeb')
    cursor.execute(sql_query)

    return cursor.fetchone()


def erase_fields_in_results():
    sql_query = "delete from results_inmuniweb;"

    cursor = get_cursor('db_inmuniWeb')
    cursor.execute(sql_query)
    cursor.execute("commit;")
    return cursor

def erase_fields_in_clients():
    sql_query = "delete from clients_inmuniweb;"

    cursor = get_cursor('db_inmuniWeb')
    cursor.execute(sql_query)
    cursor.execute("commit;")
    return cursor

def insert_one_client():
    sql_query = "insert into clients_inmuniweb " \
                "(client_id," \
                " client_name," \
                "url," \
                " discovery_id," \
                " discovery_tab_type," \
                " discovery_authorization," \
                " discovery_cookie," \
                "enabled," \
                "source) values " \
                "('549432'," \
                "'growfinancial'," \
                "'http:www.growfinancial.org'," \
                "'4631253'," \
                "'incidents'," \
                "'Basic OTgzNTM5MzIzOjZZTVhNR1BLRkI4MU1YNkpIWDRXQ09RN0kyQVBIRTcy','t=Cgs7Hl7qkpal9gPCjCKAAg==; tr_firstpage=https%3A%2F%2Fportal.immuniweb.com%2Fclient%2F; s_token=BZ75QVPCSXHMNFKF26MCMNO1I36Y13F8'," \
                "true," \
                "'ticketing');"

    cursor = get_cursor('db_inmuniWeb')
    cursor.execute(sql_query)
    cursor.execute("commit;")
    return cursor

class IntegrationRunTest(unittest.TestCase):

    def test_resutls_with_no_params(self):
        erase_fields_in_results()
        erase_fields_in_clients()
        execute_consumer()
        self.assertEqual(check_results_table_size()[0],0)

    def test_results_with_insertion_in_params(self):
        erase_fields_in_clients()
        erase_fields_in_results()
        insert_one_client()
        self.assertEqual(check_results_table_size()[0],0)

    def test_results_after_executing_with_existent_params(self):
        erase_fields_in_clients()
        erase_fields_in_results()
        insert_one_client()
        execute_consumer()
        self.assertEqual(check_results_table_size()[0],1)


if __name__ == '__main__':
        unittest.main()
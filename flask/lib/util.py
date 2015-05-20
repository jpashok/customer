import re
import os
import logger

from pyelasticsearch import ElasticSearch
from config import Config

class SingletonESClient:
    '''
    This class acts as a singleton on a per process basis.
    ES is inherently thread safe so we don't need for each thread we can return the same instance
    '''
    es_client_instances = {}

    @staticmethod
    def get_elastic_search_client(host,port,connection_type_str,connection_reset=False):
        pid = os.getpid()
        if connection_type_str == 'http':
            connection_string = '{0}://{1}:{2}'.format(connection_type_str,host,port)
        else:
            #For now only http is supported.
            raise Exception('Only HTTP connection to Elastic Search is supported as of now')
        if connection_reset or not pid in SingletonESClient.es_client_instances:
            if connection_reset:
                logger.index_logger().debug('Connection is resetting for process_id %s'%pid)
            SingletonESClient.es_client_instances[pid] = ElasticSearch(connection_string)
        if not connection_reset:
            return SingletonESClient.es_client_instances[pid]


def sanitize_string(keyword_string):
    '''
    Does a basic cleanup of the string .
    The string which is parsed out from html can be a bit messy .
    '''
    ignore_strings = [':', '\.', '/', ';', '>', '\(s\)', '\(', '\)', '#', '\"', '\'', '&', ',', '-', '_',
                      '&quot;', '<br>', '%', '\d']
    keyword_string = re.sub((('|').join(ignore_strings)), ' ', keyword_string).strip()
    return keyword_string

def find_price_from_string(price_string):
    #Find all continous numbers for now . Keeping it simple
    prince_list = re.findall(r'\d+',price_string)
    #Assume 0 if the price is not available
    return int(prince_list[0]) if prince_list is not None else 0

def get_master_connection_configuration():
    master_host = Config.get()['es_master']['host']
    master_port = Config.get()['es_master']['port']
    connection_type_str = Config.get()['es_master']['connection_type_str']
    return {'host':master_host,'port':master_port,'connection_type_str':connection_type_str}





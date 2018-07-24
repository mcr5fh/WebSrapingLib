from abc import ABCMeta, abstractmethod

'''
Base 'interface' class for scraping modules. Child classes
should decide where to store the data that is queried

Module abc (abstract base class) is used to create an abstract class
and ensure that all abtract methods are implemented
'''


class BaseWebScraper():
    # Set the metaclass as ABCMeta to ensure an instance of
    # the interface is not instansiated
    __metaclass__ = ABCMeta

    def __init__(self, data_source_name):
        self.data_source_name = data_source_name

    @abstractmethod
    def scrape_todays_data(self):
        raise NotImplementedError("This method must to be implemented")

    @abstractmethod
    def scrape_data(self, start_date, end_date):
        raise NotImplementedError("This method must to be implemented")

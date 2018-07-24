'''
To run this go to command line and run:
python example_scraper.py

It will print out some text
'''

'''
Imports work in the following way:
from <file name in the same folder> import <class>
'''
from base_web_scraper import BaseWebScraper
from datetime import datetime


class ExampleWebScraper(BaseWebScraper):
    '''the __init__() method is the constructor for all classes.
        All class methods must take `self` as the first parameter.
        You don't have to know why, or care at all, just know that it has to be there'''

    def __init__(self, data_source_name, some_other_field):
        ''' Since were extending the BaseWebScraper, we have to call that
         constructor too. We can access all of the fields in the parent class
         In this case, that's data_source_name '''
        BaseWebScraper.__init__(self, data_source_name)
        ''' But this class can also have what ever else we want, like
         some_other_field'''
        self.some_other_field = some_other_field

    def scrape_todays_data(self):
        return "This is from today! " + str(datetime.now())

    def scrape_data(self, start_date, end_date):
        return "Start: " + str(start_date) + " End: " + str(end_date)

#############################
#############################
#############################


example_scraper = ExampleWebScraper("Data Source", "some_other_field")

# You can access the fields directly
print(example_scraper.data_source_name)
print(example_scraper.some_other_field)
print(example_scraper.scrape_todays_data())
print(example_scraper.scrape_data(1, 2))

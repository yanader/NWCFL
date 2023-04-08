# This is a file used mostly to run larger scale tests.
import date_formatting as df
from fixtures_parser import FixturesParser

custom_date = df.custom_date(2)
print(custom_date)

fp = FixturesParser(custom_date)



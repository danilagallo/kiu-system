import json

from fake_data import packages
from models.client import Client
from models.package import Package


class Company:
    packages = []

    def __init__(self, name=None):
        self.name = name

    def add_to_aircraft(self, package):
        self.packages.append(package)

    def add_bulk_to_aircraft(self):
        packages_ = json.loads(json.dumps(packages))
        for p in packages_:
            client = Client(**p['owner'])
            package = Package(**p)
            package.client = client
            self.packages.append(package)

    def report_by_date(self, date=None):
        if date is not None:
            packages_by_date = list(filter(lambda p: p.date == date,
                                           self.packages))
            number_of_packages = len(packages_by_date)
            total_raised = number_of_packages * 10
            return 'By the date {date} the total raised is ${total_raised} ' \
                'and the number of packages is {number}' \
                .format(date=date, total_raised=total_raised,
                        number=number_of_packages)
        return 'You must specify a date for the report.'

    # Detailed report to be viewed via console.
    def report_by_date_detailed(self, date=None):
        self.add_bulk_to_aircraft()
        if date is not None:
            packages_by_date = list(filter(lambda p: p.date ==
                                           date, self.packages))
            number_of_packages = len(packages_by_date)
            total_raised = number_of_packages * 10
            for package in packages_by_date:
                print("\nCode: ", package.code)
                print("Date: ", package.date)
                print("Client Name: ", package.client.full_name)
                print("Client Passport Number: ",
                      package.client.passport_number)
                print("Origin: ", package.origin)
                print("Destination: ", package.destination)
                print("Description: ", package.description)
                print("----------------------")
            print("\nNUMBER OF PACKAGES: ", number_of_packages)
            print("\nTOTAL RAISED: ", total_raised)
        else:
            print('You must specify a date for the report.')

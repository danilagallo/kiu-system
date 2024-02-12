import datetime

from models.company import Company
from utils import create_client, create_package


def test_get_report_by_date():
    company = Company('JetSMART')
    # Creation of data for the report
    cliente_1 = create_client('David Houton')
    cliente_2 = create_client('Laura OConnor', 'AA876')
    cliente_3 = create_client('Frank Louis')
    package_1 = create_package(
        date=datetime.datetime(2024, 2, 12).date(), owner=cliente_1)
    package_2 = create_package(
        date=datetime.datetime(2024, 2, 12).date(), owner=cliente_2)
    package_3 = create_package(
        date=datetime.datetime(2024, 1, 23).date(), owner=cliente_1)
    package_4 = create_package(
        date=datetime.datetime(2024, 1, 14).date(), owner=cliente_1)
    package_5 = create_package(
        date=datetime.datetime(2024, 1, 14).date(), owner=cliente_3)
    package_6 = create_package(
        date=datetime.datetime(2024, 2, 12).date(), owner=cliente_1)
    # Add package per package to the aircraft
    company.add_to_aircraft(package_1)
    company.add_to_aircraft(package_2)
    company.add_to_aircraft(package_3)
    company.add_to_aircraft(package_4)
    company.add_to_aircraft(package_5)
    company.add_to_aircraft(package_6)

    assert company.report_by_date(datetime.datetime(2024, 2, 12).date()) \
        == 'By the date {date} the total raised is ' \
        '${total_raised} and the number of packages is {number}' \
        .format(date=datetime.datetime(2024, 2, 12).date(),
                total_raised=30, number=3)


def test_get_report_by_no_date():
    company = Company('JetSMART')

    assert company.report_by_date() == \
        'You must specify a date for the report.'

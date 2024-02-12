from models.company import Company


def report_by_date(date):
    company = Company('Flybondy')
    company.report_by_date_detailed(date)


if __name__ == '__main__':
    import sys
    function = getattr(sys.modules[__name__], sys.argv[1])
    date = sys.argv[2] if len(sys.argv) > 2 else None
    report_by_date(date)

def time():
    import datetime
    dt1 = datetime.datetime.now()
    print(dt1.strftime("%I"), ':', dt1.strftime("%M"), dt1.strftime("%p"))


def date():
    import datetime
    dt1 = datetime.datetime.now()
    print(dt1.strftime("%d"))


def month():
    import datetime
    dt1 = datetime.datetime.now()
    print(dt1.strftime("%B"), '[', dt1.strftime("%m"), ']')


def year():
    import datetime
    dt1 = datetime.datetime.now()
    print(dt1.strftime("%Y"), '[', dt1.strftime("%y"), ']')


def tdmy():
    import datetime
    dt1 = datetime.datetime.now()
    print(dt1.strftime("%c"))


def week():
    import datetime
    dt1 = datetime.datetime.now()
    print(dt1.strftime("%A"), '[', dt1.strftime("%w"), ']')


def you():
    import datetime
    dt1 = datetime.datetime.now()
    a = str(dt1.strftime("%d")) + '/' + str(dt1.strftime("%m")) + '/' + str(dt1.strftime("%Y")) + ' ' + str(
        dt1.strftime("%I")) + ':' + str(dt1.strftime("%M")) + ' ' + str(dt1.strftime("%p"))
    print(a)

import argparse
import sys
parser = argparse.ArgumentParser(description='Home task 2')


def task1():
    keys = ['key1', 'key2', 'key3', 'key4']
    values = ['value1', 'value2', 'value3']
    result = {}
    print "task1 ========================"
    print "keys: ", keys
    print "values: ", values
    for idx, val in enumerate(keys):
        if idx < len(values):
            result.update({val: values[idx]})
        else:
            result.update({val: None})
    print "result: ", result
    return


def task2(inputstring='abcba'):
    print "task2 ========================"
    print inputstring, inputstring == inputstring[::-1]
    return


def task3():
    print "task3 ========================"
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = list(set(a + b))
    print "first list: ", a
    print "second list: ", b
    print "result: ", c
    return


def task4():
    print "task4 ========================"
    log = '''192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
    127.0.0.1 - - [28/Jul/2006:10:22:04 -0300] "GET / HTTP/1.0" 200 2216
    192.168.2.21 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
    127.0.0.1 - - [28/Jul/2006:10:22:04 -0300] "GET / HTTP/1.0" 200 2216
    192.168.2.22 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
    127.0.0.1 - - [28/Jul/2006:10:22:04 -0300] "GET / HTTP/1.0" 200 2216
    192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
    120.0.0.1 - - [28/Jul/2006:10:22:04 -0300] "GET / HTTP/1.0" 200 2216'''
    from collections import OrderedDict
    ips = {}
    for idx, val in enumerate(log.splitlines()):
        ips[val.split()[0]] = ips.get(val.split()[0], 0) + 1
    d_ascending = OrderedDict(sorted(ips.items(), key=lambda kv: kv[1], reverse=True)[:10])
    print d_ascending.items()
    return


parser.add_argument('-all', action="store_true", default=False)
parser.add_argument('-t1', action="store_true",  default=False)
parser.add_argument('-t2', action="store_true",  default=False)
parser.add_argument('-t3', action="store_true",  default=False)
parser.add_argument('-t4', action="store_true",  default=False)
args = parser.parse_args(sys.argv[1:])


def main():
    if (args.t1 is True) | (args.all is True):
        task1()
    if (args.t2 is True) | (args.all is True):
        task2()
    if (args.t3 is True) | (args.all is True):
        task3()
    if (args.t4 is True) | (args.all is True):
        task4()

if __name__ == "__main__":
    main()

#!/usr/bin/python
def average(list):
    return sum(list) / len/(list)

class FilterModule(object):

    def filters(self):
        return {
            'average': average
        }

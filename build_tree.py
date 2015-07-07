#!/usr/bin/python
# -*- coding: ascii -*-
''' Parses a CSV into a tree structure for use in jsTree. '''
__author__ = "Adrianus Kleemans"

import csv

def main():
    filename = 'data.csv'
    data = []
    nodes = []
    json = ['"data" : [']

    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in reader:
            data.append(row)

    for i in range(len(row)):
        for j in range(len(data)):
            row = data[j]
            parent = '#'
            if i > 0: parent = row[i-1].lower().replace(' ', '')
            id = row[i].lower().replace(' ', '')

            # if leaf element, concatenate id with parent
            if i == len(row) - 1: id = row[i-1].lower().replace(' ', '') + id

            if id not in nodes or i == len(row) - 1:
                if i == len(row)-1: icon = ', "icon": false'
                else: icon = ''

                nodes.append(id)
                json.append('{ "id" : "' + id + '", "parent" : "' + parent + '", "text" : "' + row[i] + '" ' + icon + '},')
    json.append(']')
    print '\n'.join(json)

if __name__ == "__main__":
    main()

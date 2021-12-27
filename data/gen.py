#!/usr/bin/env python3

import csv
import math

with open('data.csv', mode='r') as data_file:
    csv_reader = csv.DictReader(data_file)
    month = ['']
    attendee = ['명']
    score = [0, 0, 0, 0, 0]
    from_dict = {'':'권'}
    for row in csv_reader:
        month.append(row['Month'])
        attendee.append(row['Attendee'])
        score[math.floor(float(row['Score2']))] += 1
        if row['From'] in from_dict :
            from_dict[row['From']] += 1
        else :
            from_dict[row['From']] = 1

    with open('data_attendee.csv', 'w') as data_attendee:
        csv_writer = csv.writer(data_attendee)
        csv_writer.writerows([month, attendee])

    with open('data_score.csv', 'w') as data_score:
        csv_writer = csv.writer(data_score)
        csv_writer.writerows([['토비', '레스트레이드', '왓슨', '셜록', '모리어티'], score])

    with open('data_from.csv', 'w') as data_from:
        csv_writer = csv.writer(data_from)
        csv_writer.writerows([from_dict.keys(), from_dict.values()])


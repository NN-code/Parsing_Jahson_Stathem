import json
import xlsxwriter

with open('photos.json') as json_file:
    title = json.load(json_file)

workbook = xlsxwriter.Workbook('titles_data.xlsx')
worksheet = workbook.add_worksheet()

for row_num, data in enumerate(title):
    worksheet.write(row_num, 1, data['title'])

workbook.close()
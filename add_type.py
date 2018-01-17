import csv
filepath = '/Users/sunxuanzhi/Downloads/winequality-both.csv'
filewriter = csv.writer(open('winequality-both_beta.csv','w',newline=''))
with open(filepath,'r',newline='') as file_csv:
	filereader = csv.reader(file_csv)
	header = next(filereader)
	header = header[0]
	header = header.split(';')
	header_temp = []
	for value in header:
		value = value.strip('"').strip()
		header_temp.append(value)
	header_temp.insert(0,'type')
	filewriter.writerow(header_temp)

	line_count = 0
	for row in filereader:
		line_count += 1
		row =row[0]
		row = row.split(';')
		if line_count <= 1599:
			row.insert(0,'red')
		else:
			row.insert(0,'white')
		filewriter.writerow(row)




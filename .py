from BeautifulSoup import BeautifulSoup

html = open('page.html', 'r').read()

soup = BeautifulSoup(html)
results_table = soup.find('table')

output = []

for tr in results_table.findAll('tr'):

	output_row = []


	for td in tr.findAll('td'):
		data = td.text.replace('&nbsp;', '').replace('View', '')
		
		output_row.append(data)

	if data == 'Columbia, City Of':
		output.append(output_row)

		print output

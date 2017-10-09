import pandas as pd
from bs4 import BeautifulSoup

def pd_read_broken_html(htmlstr):
	"""
	Return a list of DataFrames given an HTML string document, 
	where each DataFrame represents an HTML Table.
	"""

	# where to store each DataFrame
	df_list = list()

	# html5lib corrects broken/misssing elements to produce valid HTML
	soup = BeautifulSoup(htmlstr, 'html5lib')

	# iterate through the soup's tables, rows, and columns
	for table in soup.findAll('table'):
		# create a new DataFrame for each table
		df = pd.DataFrame()
		
		# build the DataFrame cell by cell
		for row, tr in enumerate(table.findAll('tr')):
			for col, td in enumerate(tr.findAll('td')):
				# remove excess whitespace and non-printing characters
				df.at[row, col] = " ".join(td.text.split())
		
		# set empty & non-text tags to NaN
		df = df.replace('', float('NaN'))
		
		# add newly built DataFrame to the list
		df_list.append(df)

	return df_list
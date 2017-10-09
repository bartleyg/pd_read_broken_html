import pytest
from pd_read_broken_html import pd_read_broken_html
import pandas as pd

def test_tables_single_entry():
	tables_single_entry = '''<html>
	<head>
	<title>test</title>
	</head>
	<body>
		<table>
			<tr>
				<td>a</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>b</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>c</td>
			</tr>
		</table>
	</body>
	</html>'''
	expected = [ pd.DataFrame(['a']), pd.DataFrame(['b']), pd.DataFrame(['c']) ]
	results = pd_read_broken_html(tables_single_entry)
	
	# test pd_read_broken_html version
	assert len(results) == len(expected)
	for i, df in enumerate(results):
		assert results[i].equals(expected[i])
	
	# test pandas version
	pandas_results = pd.read_html(tables_single_entry)
	assert len(pandas_results) == len(expected)
	for i, df in enumerate(pandas_results):
		assert pandas_results[i].equals(expected[i])

def test_tables_with_missing_tr():
	tables_with_missing_tr = '''<html>
	<head>
	<title>test</title>
	</head>
	<body>
		<table>
			<tr>
				<td>a</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>b</td>
			</tr>
		</table>
		<table>
				<td>c</td>
			</tr>
		</table>
	</body>
	</html>'''
	expected = [ pd.DataFrame(['a']), pd.DataFrame(['b']), pd.DataFrame(['c']) ]
	results = pd_read_broken_html(tables_with_missing_tr)
	
	# test pd_read_broken_html version
	assert len(results) == len(expected)
	for i, df in enumerate(results):
		assert results[i].equals(expected[i])
	
	# test pandas version
	pandas_results = pd.read_html(tables_with_missing_tr)
	assert len(pandas_results) == len(expected)
	for i, df in enumerate(pandas_results):
		assert pandas_results[i].equals(expected[i])

def test_duplicate_tables_with_duplicate_missing_tr():
	duplicate_tables_with_duplicate_missing_tr = '''<html>
	<head>
	<title>test</title>
	</head>
	<body>
		<table>
				<td>a</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>a</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>b</td>
			</tr>
		</table>
	</body>
	</html>'''
	expected = [ pd.DataFrame(['a']), pd.DataFrame(['a']), pd.DataFrame(['b']) ]
	results = pd_read_broken_html(duplicate_tables_with_duplicate_missing_tr)
	
	# test pd_read_broken_html version
	assert len(results) == len(expected)
	for i, df in enumerate(results):
		assert results[i].equals(expected[i])
	
	# test pandas version
	pandas_results = pd.read_html(duplicate_tables_with_duplicate_missing_tr)
	assert len(pandas_results) == len(expected)
	for i, df in enumerate(pandas_results):
		assert pandas_results[i].equals(expected[i])

def test_duplicate_tables_with_unique_missing_tr():
	duplicate_tables_with_unique_missing_tr = '''<html>
	<head>
	<title>test</title>
	</head>
	<body>
		<table>
			<tr>
				<td>a</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>a</td>
			</tr>
		</table>
		<table>
				<td>b</td>
			</tr>
		</table>
	</body>
	</html>'''
	expected = [ pd.DataFrame(['a']), pd.DataFrame(['a']), pd.DataFrame(['b']) ]
	results = pd_read_broken_html(duplicate_tables_with_unique_missing_tr)
	
	# test pd_read_broken_html version
	assert len(results) == len(expected)
	for i, df in enumerate(results):
		assert results[i].equals(expected[i])
	
	# test pandas version (fails)
	pandas_results = pd.read_html(duplicate_tables_with_unique_missing_tr)
	assert len(pandas_results) == len(expected)
	for i, df in enumerate(pandas_results):
		assert pandas_results[i].equals(expected[i])

def test_duplicate_tables_with_both_duplicates_missing_tr():
	duplicate_tables_with_both_duplicates_missing_tr = '''<html>
	<head>
	<title>test</title>
	</head>
	<body>
		<table>
				<td>a</td>
			</tr>
		</table>
		<table>
				<td>a</td>
			</tr>
		</table>
		<table>
			<tr>
				<td>b</td>
			</tr>
		</table>
	</body>
	</html>'''
	expected = [ pd.DataFrame(['a']), pd.DataFrame(['a']), pd.DataFrame(['b']) ]
	results = pd_read_broken_html(duplicate_tables_with_both_duplicates_missing_tr)
	
	# test pd_read_broken_html version
	assert len(results) == len(expected)
	for i, df in enumerate(results):
		assert results[i].equals(expected[i])
	
	# test pandas version (fails)
	pandas_results = pd.read_html(duplicate_tables_with_both_duplicates_missing_tr)
	assert len(pandas_results) == len(expected)
	for i, df in enumerate(pandas_results):
		assert pandas_results[i].equals(expected[i])

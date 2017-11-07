# pd_read_broken_html
```pd_read_broken_html()``` returns a list of DataFrames given an HTML string document, where each DataFrame represents an HTML table.

This is a replacement for the Pandas ```read_html()``` function where a bug drops duplicate tables in broken/missing HTML.
## Usage:
```python
df_list = pd_read_broken_html(html_string)
```
## Replaces in Pandas:
```python
df_list = pandas.read_html(html_string)
```
## Extra:
Run test_read_html.py to see examples where Pandas ```read_html()``` fails and this function succeeds.

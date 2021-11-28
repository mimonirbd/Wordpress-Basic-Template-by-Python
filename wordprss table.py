# this script is for wordpress table
def wpTable(th1, th2, td1, td2):
    tableStarting = '<!-- wp:table {"className":"is-style-stripes"} --><figure class="wp-block-table is-style-stripes"><table><thead><tr><th>'
    return tableStarting + th1 + '</th><th>' + th2 + '</th></tr></thead><tbody><tr><td>' + td1 + '</td><td>' + td2 + '</td></tr><tr><td>'


tableH1, tableH2 = 'Key', 'Value' + '\n'
cell1, cell2, = '1', '2'
print(wpTable(tableH1, tableH2, cell1, cell2))

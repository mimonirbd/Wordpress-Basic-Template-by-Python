# function for wordpress paragraph
def wpP(text):
    return '<!-- wp:paragraph --><p>' + text + '</p><!-- /wp:paragraph -->'


# this function for wordpress heading 2 (h2)
def h2(heading2):
    return '<!-- wp:heading --><h2>' + heading2 + '</h2><!-- /wp:heading -->'


# this function is for wordpress heading 3 (h3)
def h3(heading3):
    return '<!-- wp:heading --><h3>' + heading3 + '</h2><!-- /wp:heading -->'


# function for wordpress quotes
def wpQ(quotes, author):
    return '<!-- wp:quote {"className":"is-style-default"} --><blockquote class="wp-block-quote is-style-default"><p>' + quotes + '</p><cite>' + author + '</cite></blockquote><!-- /wp:quote -->'


# wordpress image posting template
def wpImg(url, anchor):
    return '<!-- wp:image {"sizeSlug":"large"} --><figure class="wp-block-image size-large"><img src="' + url + '\" alt=\"' + anchor + '"/></figure><!-- /wp:image --> '


# this script is for wordpress list item
def wpList(li1, li2, li3, li4):
    return '<!-- wp:list --><ul><li>' + li1 + '</li><li>' + li2 + '</li><li>' + li3 + '</li><li>' + li4 + '</li></ul><!-- /wp:list -->'


# this script is for wordpress table
def wpTable(th1, th2, td1, td2):
    tableStarting = '<!-- wp:table {"className":"is-style-stripes"} --><figure class="wp-block-table is-style-stripes"> <table><thead><tr><th>'
    return tableStarting + th1 + '</th><th>' + th2 + '</th></tr></thead><tbody><tr><td>' + td1 + '</td><td>' + td2 + '</td></tr><tr><td>'


# direct use as string
print(h2('This is heading 2'))
# using variable
head2 = 'This is h2'
print(h2(head2))
# h3
head3 = 'This title for heading 3'
print(h3(head3))

# quotes
quo = 'Time and tide wait for none.'
auth = 'Unknown'
print(wpQ(quo, auth))

# image
imgLink = 'https://example.com/img.png'
imgAnchor = 'flower'
print(wpImg(imgLink, imgAnchor))

# list item
one = 'Bangladesh'
two = 'India'
three = 'US'
four = 'United Kingdom'
print(wpList(one, two, three, four))

# table
tableH1, tableH2 = 'Key', 'Value' + '\n'
cell1, cell2, = '1', '2'
print(wpTable(tableH1, tableH2, cell1, cell2))
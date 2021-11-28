# this script is for wordpress list item

def wpList(li1, li2, li3, li4):
    return '<!-- wp:list --><ul><li>' + li1 + '</li><li>' + li2 + '</li><li>' + li3 + '</li><li>' + li4 + '</li></ul><!-- /wp:list -->'


one = 'Bangladesh'
two = 'India'
three = 'US'
four = 'United Kingdom'

print(wpList(one, two, three, four))
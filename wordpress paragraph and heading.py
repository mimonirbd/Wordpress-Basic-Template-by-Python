# function for wordpress paragraph

def wpP(text):
    return '<!-- wp:paragraph --><p>' + text + '</p><!-- /wp:paragraph -->'


firstP = 'This is paragraph.'
print(wpP(firstP))

secondP = 'Hello friends, how are you all?'
print(wpP(secondP))


# this function for wordpress heading 2 (h2)
def h2(heading2):
    return '<!-- wp:heading --><h2>' + heading2 + '</h2><!-- /wp:heading -->'


# this function is for wordpress heading 3 (h3)
def h3(heading3):
    return '<!-- wp:heading --><h3>' + heading3 + '</h2><!-- /wp:heading -->'


# direct use as string
print(h2('This is heading 2'))
# using variable
head2 = 'This is h2'
print(h2(head2))

head3 = 'This title for heading 3'
print(h3(head3))

# function for wordpress quotes

def wpQ(quotes, author):
    return '<!-- wp:quote {"className":"is-style-default"} --><blockquote class="wp-block-quote is-style-default"><p>' \
           + quotes + '</p><cite>' + author + '</cite></blockquote><!-- /wp:quote -->'


quo = 'Time and tide wait for none.'
auth = 'Unknown'
print(wpQ(quo, auth))

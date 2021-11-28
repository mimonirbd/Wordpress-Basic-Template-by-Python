# wordpress image posting template
def wpImg(url, anchor):
    return '<!-- wp:image {"sizeSlug":"large"} --><figure class="wp-block-image size-large"><img src="' + url + '\" alt=\"' + anchor + '"/></figure><!-- /wp:image --> '


imgLink = 'https://example.com/img.png'
imgAnchor = 'flower'

print(wpImg(imgLink, imgAnchor))

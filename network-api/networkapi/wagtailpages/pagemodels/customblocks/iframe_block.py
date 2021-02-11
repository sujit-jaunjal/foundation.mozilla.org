from wagtail.core import blocks


class iFrameBlock(blocks.StructBlock):
    url = blocks.CharBlock(
        help_text='Please note that only URLs from white-listed domains will work.'
    )
    height = blocks.IntegerBlock(
        required=False,
        help_text='Optional integer value of the iFrame height (in pixels)'
    )
    caption = blocks.CharBlock(
        required=False
    )
    captionURL = blocks.CharBlock(
        required=False,
        help_text='Optional URL that this caption should link out to.'
    )

    class Meta:
        template = 'wagtailpages/blocks/iframe_block.html'

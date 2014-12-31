# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


WHITELIST = ('test', 'image',)


TEST_STRING = """
<div>
    <test />
    <div>
        <test class="foobar"></test>
    </div>
</div>
"""

TEST_STRING_RESULT = """
<div>
    <b>Test transformed.</b>
    <div>
        <b>Test transformed.</b>
    </div>
</div>
"""
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


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

TEST_OC_STRING = """
<div>
    <openclose class="foobar">I am content!</test>
</div>
"""

TEST_OC_STRING_RESULT = """
<div>
    <div>I am content!</div>
</div>
"""

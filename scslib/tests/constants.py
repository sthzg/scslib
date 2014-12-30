# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


WHITELIST = ('test', 'image',)


TEST_STRING = """
<div>
<h1>Hello world</h1>
<image embed-id="foobar" class="img-responsive" />
<test />
<bs-row fluid="true">
    <bs-col sm="12" md="8">
        <h2>Head</h2>
        <p>Lorem ipsum.</p>
        <test class="hello-world">Foobar</test>
    </bs-col>
    <bs-col sm="12" md="4">
        <image embed-id="foobar" class="img-responsive" lazy="true" />
        <h2>Head 2</h2>
        <p>Dolor sit.</p>
    </bs-col>
</bs-row>
<bs-slideshow autoplay="false">
    <image embed-id="bam" />
    <image embed-id="baz" />
    <image embed-id="bar" />
</bs-slideshow>
<crazy-box template="darkblue">
    <p>Lorem ipsum.</p>
    <image embed-id="fjord" />
</crazy-box>
</div>
"""

TEST_STRING_EMPTY = ""

# -*- coding: utf-8 -*-
<%inherit file="base.mak"/>
<div class="well well-large">
<div class="pull-right">
<img src="${request.static_url("panstora:static/img/cart.png")}" alt="Cart Icon. By: klepas"></img>
</div>
% if dev_id is not None:
	<p>dev_id is ${request.session['dev_id']}</p>
% endif

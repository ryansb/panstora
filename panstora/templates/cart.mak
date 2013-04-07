# -*- coding: utf-8 -*-
<%inherit file="base.mak"/>
<div class="well well-large">
<div class="pull-right">
<img src="${request.static_url("panstora:static/img/cart.png")}" alt="Cart Icon. By: klepas"></img>
</div>
% if request.session['user'] is not None:
	<% user = request.session['user'] %>
	<p>dev_id is ${request.session['dev_id']}</p>
	<h1>${user.name}'s shopping cart</h1>
	<ul>
		% for item in user_cart_items:
			<li>${item.name}</li>
		% endfor
	</ul>
% endif

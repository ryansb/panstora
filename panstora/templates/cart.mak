# -*- coding: utf-8 -*-
<%inherit file="base.mak"/>
<div class="well well-large">
<div class="pull-right">
<img src="${request.static_url("panstora:static/img/cart.png")}" alt="Cart Icon. By: klepas"></img>
</div>
% if request.session['user'] is not None:
	<% user = request.session['user'] %>
	<strong>${user.name}'s shopping cart</strong>
	<ul>
		% for item in user_cart_items:
			<li>${item.name}</li>
		% endfor
	</ul>
	<a class="button" href="/">Checkout</a>
% else:
<p>Unknown user. Scan an item to identify yourself.</p>
% endif

# -*- coding: utf-8 -*-
<%inherit file="base.mak"/>
<div class="well well-large">
<h1>${item.name}</h1>
<span>Item code ${item.code}</span>
<div class="pull-right">
<img src="${request.static_url("panstora:static/img/cart.png")}" alt="Cart Icon. By: klepas"></img>
</div>
<ul>
	<li><strong>Description:</strong>${item.description}</li>
	<li><strong>Tags:</strong></li>
		<ul>
			% for tag in item.tags:
			<li>${tag.name}</li>
			% endfor
		</ul>
	<li><strong>Price:</strong>${item.price}</li>
	<li><strong>Rack:</strong>${item.rack}</li>
	<li><strong>Department:</strong>${item.dept}</li>
</ul>
</div>

% if dev_id is not None:
	<a class="btn btn-primary" href="/cart/add">Add to Cart</a>
% endif

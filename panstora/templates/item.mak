# -*- coding: utf-8 -*-
<%inherit file="base.mak"/>
<h1>${item.name}</h1>
<span>Item code ${item.code}</span>
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

# -*- coding: utf-8 -*-
<!-- This file is used as the base for all other pages. -->
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<link href="${request.static_url(
		"panstora:static/css/panstora.css")}"
		rel="stylesheet" type="text/css" media="all">
	<title>Panstora</title>
</head>
<body>
<div class="title-block">
	<span class="title">Panstora</span>
	<span class="subtitle">
		Panstora is the place from which all good things come.
	</span>
</div>
<ul class="nav-list">
	<li><a href="/">Home</a></li>
	<li>NavB</li>
	<li>NavC</li>
</ul>

${self.body()}

</body>
</html>

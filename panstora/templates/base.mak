# -*- coding: utf-8 -*-
<!-- This file is used as the base for all other pages. -->
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="${request.static_url(
		"panstora:static/css/bootstrap.min.css")}"
		rel="stylesheet" type="text/css" media="all">
	<title>Panstora</title>
</head>
<body>
<script src="http://code.jquery.com/jquery.js"></script>
<script src="${request.static_url("panstora:static/js/bootstrap.min.js")}"></script>
<div class="title-block">
	<h1 class="text-center">Panstora <br/>
	<small>
		Panstora is the place from which all good things come.
	</small>
	</h1>
</div>
<!--
<ul class="nav-list">
	<li><a class="button" href="/">Home</a></li>
</ul>
-->
<hr/>
${self.body()}

</body>
</html>

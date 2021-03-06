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
	<link href="${request.static_url(
		"panstora:static/css/panstora.css")}"
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
<ul class="nav-list">
	<center>
		<li><a class="btn btn-primary text-center" href="/">Home</a></li>
		<li><a class="btn btn-primary text-center" href="/cart">Cart</a></li>
	</center>
</ul>
<hr/>
<div class="container-fluid">
	<div class="row-fluid">
		<div class="span2"></div>
		<div class="span8">
		${self.body()}
		</div>
		<div class="span2"></div>
	</div>
</div>
</body>
</html>

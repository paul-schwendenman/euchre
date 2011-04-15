
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<title>Euchre</title>
<link rel="shortcut icon" href="favicon.ico" />
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<link rel="stylesheet" type="text/css" href="static/base.css" />
<script type="text/javascript" src="static/jquery.js"></script>
<script type="text/javascript" src="static/render.js"></script>
<script type="text/javascript">
$(document).ready(function(){
	hideall();
  	$("button").click(function(){
		$.ajax({url:"/game", success:callback});		
		mode = 0;
		callback();
 	});
});
</script>

</head>
<body>
<div class='top'>
<div id='played_cards'>
	<p>Played Cards. Fill me in</p>
</div>
<!-- <h1 id="show_msg">{{str(msg)}}</h1>
% if "result" in locals():
<p>{{result}}</p>
% end
-->
<p id='trump'>Trump: None</p>
</div>
<div class='bottom'>
<div id='cards'>
	<p>Cards. Fill me in</p>
</div>

<div id='suits'>
	<p>Suits. Fill me in</p>
</div>
<div id='yesno'>
	<p>Yesno. Fill me in</p>
</div>
<div id='next'>
	<p>Next. Fill me in</p>
</div>

<form id="frm" action="/" method="post">
    <p>
	<input id="result" type="hidden" name="result" value="" />
	<input id="msg" type="hidden" name="msg" value='{{msg}}' />
    </p>
</form>
</div>
</body>
</html>

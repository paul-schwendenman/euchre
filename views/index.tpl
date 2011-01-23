

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
<table id='played_cards'>
<tr><th>Played Cards</th></tr>
<tr>
<td></td>
<td></td>
<td>Partner:</td><td><img alt='{{played_cards[0]}}' src='{{"static/" + played_cards[0].image()}}' /></td>
<td></td>
</tr>
<tr>
<td>Opponent 1:</td><td><img alt='{{played_cards[1]}}' src='{{"static/" + played_cards[1].image()}}' /></td>
<td></td>
<td></td>
<td>Opponent 3:</td><td><img alt='{{played_cards[2]}}' src='{{"static/" + played_cards[2].image()}}' /></td>
</tr>
<tr>
<td></td>
<td></td>
<td>You:</td><td><img alt='{{played_cards[3]}}' src='{{"static/" + played_cards[3].image()}}' /></td>
<td></td>
</tr>
</table>
<h1 id="show_msg">{{str(msg)}}</h1>
% if "result" in locals():
<p>{{result}}</p>
% end
% if "trump" in locals():
<p class='trump'>Trump: {{trump}}</p>
% end
</div>
<div class='bottom'>
<table id='cards'>
  <tr><th>Your Cards:</th></tr>
  <tr>
  % for card in cards:
  <td><img alt='{{card}}' src="{{'static/' + card.image()}}" /></td>
	% end
	</tr>
	<tr>
	% for index, card in enumerate(cards):
  <td class='card_buttons'><button>{{str(card)}}</button></td>
	% end
  </tr>
</table>

<div id='suits'>
  <table>
    <tr><th>Suits</th></tr>
    <tr>
    <td><button>Spades</button></td>
    <td><button>Hearts</button></td>
    <td><button>Clubs</button></td>
    <td><button>Diamonds</button></td>
    <td><button>Pass</button></td>
    </tr>
  </table>
</div>
        <div id='yesno'>
        <table>
                <tr><th>Yes No</th></tr>
                <tr>
                        <td><button>Yes</button></td>
                        <td><button>No</button></td>
                </tr>
        </table>
	</div>
<div id='next'>
  <table>
    <tr><th>Next</th></tr>
    <tr>
	    <td><button>Next</button></td>
    </tr>
  </table>
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

<html>
<head>
<title>Test</title>
<script type="text/javascript">
function callback(str)
{
document.getElementById("result").value=str;
document.getElementById("frm").submit();
//alert(str);
}

</script>

</head>
<body>
% if played_cards:
<table>
<tr><th>Played Cards</th></tr>
<tr>
<td></td>
<td>P:<img src="pics/C9.gif" /></td>
<td></td>
</tr>
<tr>
<td>1:<img src="pics/DJ.gif" /></td>
<td></td>
<td>3:<img src="pics/CQ.gif" /></td>
</tr>
<tr>
<td></td>
<td>U:<img src="pics/HA.gif" /></td>
<td></td>
</tr>
</table>
% end
% if cards:
<table>
<tr><th>Your Cards</th></tr>
<tr>
% for index, card in enumurate(cards):
<td><img src="{{p.imagedict[card]}}" /></td>
</tr>
<tr>
<td><input type="button" value={{str(_card.suit) + str(_card.rank)}} onclick={{"callback(%s)" % str(index)}}  /></td>
</tr>
</table>
% end
% end
% if suits:
<form>
<table>
<tr><th>Suits</th></tr>
<tr>
<td><input type="button" value="Spades" onclick="callback('S')" /></td>
<td><input type="button" value="Hearts" onclick="callback('H')" /></td>
<td><input type="button" value="Clubs" onclick="callback('C')" /></td>
<td><input type="button" value="Diamonds" onclick="callback('D')" /></td>
<td><input type="button" value="Pass" onclick="callback('P')" /></td>
</tr>
</table>
</form>
% end
% if yesno:
<form>
<table>
<tr><th>Yes No</th></tr>
<tr>
<td><input type="button" value="Yes" onclick="callback('Y')" /></td>
<td><input type="button" value="No" onclick="callback('P')" /></td>
</tr>
</table>
</form>
% end
% if next:
<form>
<table>
<tr><th>Next</th></tr>
<tr>
<td><input type="button" value="Next" onclick="callback(' ')" /></td>
</tr>
</table>
</form>
% end

<form id="frm" method="POST">
<input id="result" type="hidden" name="result" value="" />
<input type="hidden" name="msg" value="{{msg}}" />
</form>

</body>
</html>

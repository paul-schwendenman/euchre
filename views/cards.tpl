<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<table>
<tr><th>Your Cards:</th></tr>
<tr>
	% for card in cards:
	<td><img alt='{{card}}' src="{{'static/' + card.image()}}" /></td>
	% end
</tr>
<tr>
	% for card in cards:
	<td class='card_buttons'><button>{{str(card)}}</button></td>
	% end
</table>
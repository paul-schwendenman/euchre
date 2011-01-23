function callback(mode)
{
	switch(mode)
	{
	case 0:
	{bid_1();break;}
	case 1:
	{bid_2();break;}
	case 2:
	{pickitup();break;}
	case 3:
	{play();break;}
	case 4:
	{results();break;}
	case 88:
	{hideall();break;}
	case 99:
	{showall();break;}
	default:
	{alert(mode);
	showall();}
	}	
	if (msg != "")
	{
		$("#msg").html(msg);
	}
};
function showall()
{
	$("#cards").show();
	$("#trump").show();
	$("#played_cards").show();
	$(".card_buttons").show();
	$("#yesno").show();
	$("#topcard").show();
	$("#next").show();
	$("#suits").show();
};
function hideall()
{
	$("#cards").hide();
	$("#trump").hide();
	$("#played_cards").hide();
	$(".card_buttons").hide();
	$("#yesno").hide();
	$("#topcard").hide();
	$("#next").hide();
	$("#suits").hide();
};
function results()
{
	$("#cards").hide();
	$("#trump").hide();
	$("#played_cards").show();
	$(".card_buttons").hide();
	$("#yesno").hide();
	$("#topcard").hide();
	$("#next").show();
	$("#suits").hide();
};
function play()
{
	$("#cards").show();
	$("#trump").show();
	$("#played_cards").show();
	$(".card_buttons").show();
	$("#yesno").hide();
	$("#topcard").hide();
	$("#next").hide();
	$("#suits").hide();
};
function bid_1()
{
	$("#cards").show();
	$("#trump").show();
	$("#played_cards").hide();
	$(".card_buttons").hide();
	$("#yesno").show();
	$("#topcard").show();
	$("#next").hide();
	$("#suits").hide();
};
function bid_2()
{
	$("#cards").show();
	$("#trump").hide();
	$("#played_cards").hide();
	$(".card_buttons").hide();
	$("#yesno").hide();
	$("#topcard").hide();
	$("#next").hide();
	$("#suits").show();
};
function pickitup()
{
	$("#cards").show();
	$("#trump").show();
	$("#played_cards").hide();
	$(".card_buttons").show();
	$("#yesno").hide();
	$("#topcard").hide();
	$("#next").hide();
	$("#suits").hide();
};
function butt(str)
{
document.getElementById("msg").value=msg;
document.getElementById("result").value=str;
document.getElementById("frm").submit();
//alert(str);
};



console.log("Started Script ...")
var gt = document.getElementById("GeneralText")
gt.style.background = "green"
gt.style.opacity = 1
gt.style.padding = "10px 5px 5px 50px"
gt.style.border = "dotted"



function cardHighlight(event)
{
	event.target.style.background = "grey"	
}

function cardNormal(event)
{
	event.target.style.background = "white"	
}


var cd = document.getElementsByClassName("card");
console.log(cd);

for(var i=0 ; i<cd.length; i++)
{
	cd[i].addEventListener("mouseover", cardNormal);
	cd[i].addEventListener("mouseout", cardNormal);
	cd[i].addEventListener("mousedown", cardHighlight);
}


console.log("Script Ended ...")
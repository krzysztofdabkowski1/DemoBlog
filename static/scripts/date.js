function x() {
	var d = document.getElementsByClassName("main_post_date");
	var i=0;
	var temp;
	var days = ["nie","pon","wto","śro","czw","pią","sob"];
	var today=new Date();
	for (i;i<d.length;i++){
		temp=new Date(d[i].innerHTML);
		if(temp==new Date()){
			d[i].innerHTML="dzisiaj";
		}
		else{
			temp=days[temp.getDay()]+", "+temp.getDate()+"."+temp.getMonth()+"."+temp.getFullYear();
			d[i].innerHTML=temp;
		}
		
		
	}

}
x();



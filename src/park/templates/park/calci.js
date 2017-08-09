



window.onload=function(){
    console.log("harsh")
	var s=$('#info')
	var info=s.html()
  //  var slots=$('.slots')
    console.log("harsh")
    

    id=["A1","A2","A3","A4"]

    for(var i=0;i<info.length;i++){
         
         var t='#'+id[i]
         var slot=$(t)
         if(info[i]==0){
         	slot.color="blue"


         }
         else{slot.style.color="red"}






    }




}
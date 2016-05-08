	       	 
	       	 $(document).ready(function(){
	       	 		$(".goto").fadeIn("fast");
	       	 		$(".attention").fadeOut();
	       	 		$(".fans").fadeOut();
	       	 		$(".push").fadeOut();
	       	 	});
	       	
	       	 
	       	 $(document).ready(function(){
	       	 	$('.1').click(function(){
	       	 		$(".fans").fadeIn("fast");
	       	 		$(".attention").fadeOut();
	       	 		$(".goto").fadeOut();
	       	 		$(".push").fadeOut();
	       	 	});
	       	 });
	     
	       	 $(document).ready(function(){
	       	 	$('.2').click(function(){
	       	 		$(".fans").fadeOut();
	       	 		$(".attention").fadeIn("fast");
	       	 		$(".goto").fadeOut();
	       	 		$(".push").fadeOut();
	       	 	});
	       	 });
	       
	       	 $(document).ready(function(){
	       	 	$('.3').click(function(){
	       	 		$(".fans").fadeOut();
	       	 		$(".attention").fadeOut();
	       	 		$(".goto").fadeIn("fast");
	       	 		$(".push").fadeOut();
	       	 	});
	       	 });
	       	
	       	 $(document).ready(function(){
	       	 	$('.4').click(function(){
	       	 		$(".fans").fadeOut();
	       	 		$(".attention").fadeOut();
	       	 		$(".goto").fadeOut();
	       	 		$(".push").fadeIn("fast");
	       	 	});
	       	 });

	        var As=document.getElementById("nav").getElementsByTagName("a");
	        As[0].style.borderBottom="5px solid black";
	    	function bian(n){	    	 
		    	for(var j=0;j<As.length;j++){
		    		As[n].style.borderBottom="5px solid black";
		    		
		    		if(j!=n){
		    			As[j].style.border="0px";
		    			
		    		}
		    	}	    		
	    	}
	       
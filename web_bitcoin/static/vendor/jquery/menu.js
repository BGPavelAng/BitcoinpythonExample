$(document).ready(function(){
	$('#btn-menu').click(function(){
		if($('.btn-menu span').attr('class') == 'fa fa-bars'){
			$('.btn-menu span').removeClass('fa-bars').addClass('fa fa-close');
			$('.menu-link').css({'left':'0'});
		}else{
			$('.btn-menu span').removeClass('fa-close').addClass('fa fa-bars');
			$('.menu-link').css({'left':'-100%'});
		}
	})
})
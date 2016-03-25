$(function() {
	$('#jugar').click(function(event){
		event.preventDefault();
		jugador = $("#jugada").val();
		$.getJSON('/resultado', { 
			jugador : jugador 
			}, function(data) {
				$('#DatosJugador').text(data.jugador);
				$('#DatosPC').text(data.pc);
				$('#Resultado').text(data.resultado);
			});
	});
});
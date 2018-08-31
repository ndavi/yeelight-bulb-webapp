

function toggleDimmer() {
$.post( "f", function( data ) {
  $( ".result" ).html( data );
});
}

function changecolor(jscolor) {
colors = hexToRgb(jscolor)
$.post( "color", colors)
  .done(function( data ) {
  });
}

function changeIntensity(intensity) {
    $.post( "changeIntensity", {'intensity' : intensity})
        .done(function( data ) {

        });
}


function hexToRgb(hex) {
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}
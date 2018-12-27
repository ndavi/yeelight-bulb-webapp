var lamps;

$( document ).ready(function() {
    lamps = $('#data').data("value");

});

function toggleDimmer(lampID) {
    $.post("f/" + lampID)
        .done(function( data ) {
            Snackbar.show({text: data});
        })
}

function changecolor(jscolor, lampID) {
colors = hexToRgb(jscolor)
$.post( "color/" + lampID, colors)
  .done(function( data ) {
      Snackbar.show({text: data});
  })
}

function changeIntensity(intensity, lampID) {
    $.post( "changeIntensity/" + lampID, {'intensity' : intensity})
        .done(function( data ) {
            Snackbar.show({text: data});
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
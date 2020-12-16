/*
# riverflow_test.js
#
# about the code:
# to display the animation of riverflow on the map.
 This javascript needs the CSS from the riverflow.html for better visualization of the legend.
 This javascript load the data that I load from the 
 Created on: 11 Nov 2020
 by: symfikri@gmail.com




*/

var map = L.map('map', {
  center:[3.023833, 101.376665],
  // setView: true,
  panTo: true,
  zoom: 13,
  maxzoom: 18,
  minzoom: 1,
  zoomControl: false,  
  editable: true, 
});   
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

//read the JSON data from php file

var geoJsonData = $.getJSON("{% url 'riverData' %}", function(geoJsonData){

features = geoJsonData.features,
layers = [];

console.log(geoJsonData)
// Assume we have only point features in the GeoJSON.
for (var i = 0; i < features.length; i += 1) {
if (i) {
  // Create a polyline between the previous point and the current one.
  layers.push(L.polyline.antPath([
    swapLngLat(features[i - 1].geometry.coordinates),
    swapLngLat(features[i].geometry.coordinates)
  ], 

// getStyle(features[i].properties.ID_POINT) 
lineStyle(features[i])



));
  

} 
var legend = L.control({position: 'topleft'});
// var legend = L.control({position: 'bottomright'});
legend.onAdd=function(map){
    var div=L.DomUtil.create('div','info legend');
    var labels=["Plastic less than 300","Plastic less than 600",
                "Plastic more than 600"];
    var grades = [299,599,600];
    div.innerHTML='<div><b>Legend</b></div';
    for(var i=0; i <grades.length; i++){
        div.innerHTML+='<i style=background:'+lineColor(grades[i])+'>&nbsp;</i>&nbsp;&nbsp;'+labels[i]+'<br/>' ;
    }
    return div;
      };
      
      

}
legend.addTo(map);
L.layerGroup(layers).addTo(map);
});

function swapLngLat(lngLatArray) {
return [
  lngLatArray[1],
  lngLatArray[0]
];
}


function lineStyle(features){

return {
    "color":lineColor(features.properties.id),
    "paused": false,   　　
    "reverse": false,　　
    "delay": 2000,　　　　
    "dashArray": [2, 30],　
    "weight": 5,　　　　
    "opacity": 0.3,　
    "pulseColor": "#FFFFFF"　
}
};

function lineColor(colour_line){
if(colour_line<300){ 
  return "#FF0000";
}else if(colour_line < 600){  
  return 'blue';
}else{
    return 'green';
}
};
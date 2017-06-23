// var canvas = document.createElement('canvas');
// var worldmap = echarts.init(canvas, null, {
//     width: 4096, height: 2048
// });
// var worldmap = echarts.init(document.getElementById('main'));
 // worldmap.setOption(option = {
 //        bmap: {
 //            center: [120.13066322374, 30.240018034923],
 //            zoom: 14,
 //            roam: true,
 //            mapStyle: {
 //                styleJson: [{
 //                    'featureType': 'water',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#d1d1d1'
 //                    }
 //                }, {
 //                    'featureType': 'land',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#f3f3f3'
 //                    }
 //                }, {
 //                    'featureType': 'railway',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'visibility': 'off'
 //                    }
 //                }, {
 //                    'featureType': 'highway',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#fdfdfd'
 //                    }
 //                }, {
 //                    'featureType': 'highway',
 //                    'elementType': 'labels',
 //                    'stylers': {
 //                        'visibility': 'off'
 //                    }
 //                }, {
 //                    'featureType': 'arterial',
 //                    'elementType': 'geometry',
 //                    'stylers': {
 //                        'color': '#fefefe'
 //                    }
 //                }, {
 //                    'featureType': 'arterial',
 //                    'elementType': 'geometry.fill',
 //                    'stylers': {
 //                        'color': '#fefefe'
 //                    }
 //                }, {
 //                    'featureType': 'poi',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'visibility': 'off'
 //                    }
 //                }, {
 //                    'featureType': 'green',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'visibility': 'off'
 //                    }
 //                }, {
 //                    'featureType': 'subway',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'visibility': 'off'
 //                    }
 //                }, {
 //                    'featureType': 'manmade',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#d1d1d1'
 //                    }
 //                }, {
 //                    'featureType': 'local',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#d1d1d1'
 //                    }
 //                }, {
 //                    'featureType': 'arterial',
 //                    'elementType': 'labels',
 //                    'stylers': {
 //                        'visibility': 'off'
 //                    }
 //                }, {
 //                    'featureType': 'boundary',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#fefefe'
 //                    }
 //                }, {
 //                    'featureType': 'building',
 //                    'elementType': 'all',
 //                    'stylers': {
 //                        'color': '#d1d1d1'
 //                    }
 //                }, {
 //                    'featureType': 'label',
 //                    'elementType': 'labels.text.fill',
 //                    'stylers': {
 //                        'color': '#999999'
 //                    }
 //                }]
 //            }
 //        },
 //        series: [{
 //            type: 'lines',
 //            coordinateSystem: 'map',
 //            data: [],
 //            polyline: true,
 //            lineStyle: {
 //                normal: {
 //                    color: 'purple',
 //                    opacity: 0.6,
 //                    width: 1
 //                }
 //            }
 //        }]
 //    });



var myChart = echarts.init(document.getElementById('main'));
option = {
    backgroundColor: '#000',
    globe: {
        // baseTexture: worldmap,
        // heightTexture: worldmap,
        displacementScale: 0.04,
        shading: 'realistic',
        environment: 'img/data-1491837999815-H1_44Qtal.jpg',
        realisticMaterial: {
            roughness: 0.9
        },
        postEffect: {
            enable: true
        },
        globeRadius:70,
        globeOuterRadius:90,
        light: {
            main: {
                intensity: 5,
                shadow: true
            },
            ambientCubemap: {
                texture: 'img/data-1491838644249-ry33I7YTe.hdr',
                diffuseIntensity: 0.2
            }
        }
    },
    mapbox: {
        style: 'mapbox://styles/mapbox/dark-v9'
    }
};
// var bmap = worldmap.getModel().getComponent('bmap').getBMap();
// bmap.addControl(new BMap.MapTypeControl());
myChart.setOption(option);

mapboxgl.accessToken = 'pk.eyJ1IjoiZmFuYWlhaSIsImEiOiJjajQ1YXlrZWkxbnRyMzNydXRqMDZiYXEzIn0.ztl8K4ErFftucvDAaqDcpw';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v9'
});

require([
    "esri/views/2d/draw/Draw",
    "esri/Map",
    "esri/views/MapView",
    "esri/layers/GroupLayer",
    "esri/layers/MapImageLayer",
    "esri/widgets/LayerList",
    "esri/widgets/BasemapGallery",
    "esri/widgets/Expand",
    "esri/widgets/Legend",
    "esri/Graphic",
    "esri/geometry/Polygon",
    "esri/geometry/geometryEngine",
    "esri/widgets/Search",
    "dojo/domReady!"
], function(
    Draw, Map, MapView, GroupLayer, MapImageLayer, LayerList, BasemapGallery, Expand, Legend, Graphic, Polygon, geometryEngine,Search
) {

    // Create layer showing sample data of the United States.



    // Create GroupLayer with the two MapImageLayers created above
    // as children layers.

    var layerGroup1 = new MapImageLayer({
        url: "http://cartography.hawaii.edu/arcgis/rest/services/HawaiiSoil/HawaiiSoil/MapServer",
        title:"Soil Conditions",
        sublayers: [
            {id: 0, visible: true, title: "Water Permeability", source: {mapLayerId: 7}},
            {id: 1, visible: false,title: "Soil Type ",source: {mapLayerId: 8}},
            {id: 2, visible: false,title: "Shrink Swell State",source: {mapLayerId: 9}},
            {id: 3, visible: false,title: "PH",source: {mapLayerId: 10}},
            {id: 4, visible: false,title: "Organic Matter",source: {mapLayerId: 11}},
            {id: 5, visible: false,title: "Fertility Class",source: {mapLayerId: 12}},
            {id: 6, visible: false,title: "Cation exchange capacity (CEC) ",source: {mapLayerId: 13}}
        ]
    });

    var layerGroup2 = new MapImageLayer({
        url: "http://cartography.hawaii.edu/arcgis/rest/services/HawaiiSoil/HawaiiSoil/MapServer",
        title:"Topography",
        sublayers: [
            {id: 0, visible: false, title: "Slope (degree)", source: {mapLayerId: 9}},
            {id: 1, visible: false,title: "Land use and land cover",source: {mapLayerId: 10}},
            {id: 2, visible: false,title: "Elevation",source: {mapLayerId: 11}}
        ]
    });

    var layerGroup3 = new MapImageLayer({
        url: "http://cartography.hawaii.edu/arcgis/rest/services/HawaiiSoil/HawaiiSoil/MapServer",
        title:"Climate Data",
        sublayers: [
            {id: 0, visible: false, title: "Surface temperature", source: {mapLayerId: 1}},
            {id: 1, visible: false,title: "Annual precipitation (mm)",source: {mapLayerId: 4}},
            {id: 2, visible: false,title: "Solar Radiation",source: {mapLayerId: 5}},
            {id: 3, visible: false,title: "Air temperature",source: {mapLayerId: 3}},
            {id: 4, visible: false,title: "Evaportransportation",source: {mapLayerId: 2}}
        ]
    });

    var var_title = "Hawaii Soil Health"
    var demographicGroupLayer = new GroupLayer({
        title: var_title,
        visible: true,
        visibilityMode: "exclusive",
        layers: [layerGroup3,layerGroup2,layerGroup1],
        opacity: 0.75
    });

    // Create a map and add the group layer to it


    var map = new Map({
        container: "viewDiv",
        basemap: "satellite",
        layers: [demographicGroupLayer]
    });

    // Add the map to a MapView

    mapExtent = { // autocasts as new Extent()
        xmin: -154.7100,
        ymin: 17.881,
        xmax: -160.2505,
        ymax: 23.4364,
        spatialReference: 4326
    }

    var view = new MapView({
        zoom: 3,
        container: "viewDiv",
        map: map,
        extent: mapExtent
    });

    var legend = new Legend({
        view: view,
        layerInfos: [{
            layer: demographicGroupLayer,
            title: "Legend"
        }]
    });

    var searchWidget = new Search({
        view: view
    });

    // Creates actions in the LayerList.

    function defineActions(event) {

        // The event object contains an item property.
        // is is a ListItem referencing the associated layer
        // and other properties. You can control the visibility of the
        // item, its title, and actions using this object.

        var item = event.item;

        if (item.title === var_title) {

            // An array of objects defining actions to place in the LayerList.
            // By making this array two-dimensional, you can separate similar
            // actions into separate groups with a breaking line.

            item.actionsSections = [
                [{
                    title: "Go to full extent",
                    className: "esri-icon-zoom-out-fixed",
                    id: "full-extent"
                }, {
                    title: "Layer information",
                    className: "esri-icon-description",
                    id: "information"
                }],
                [{
                    title: "Increase opacity",
                    className: "esri-icon-up",
                    id: "increase-opacity"
                }, {
                    title: "Decrease opacity",
                    className: "esri-icon-down",
                    id: "decrease-opacity"
                }]
            ];
        }
    }

    view.when(function() {

        // Create the LayerList widget with the associated actions
        // and add it to the top-right corner of the view.

        var layerList = new LayerList({
            view: view,
            // executes for each ListItem in the LayerList
            listItemCreatedFunction: defineActions
        });

        // Event listener that fires each time an action is triggered

        layerList.on("trigger-action", function(event) {

            // The layer visible in the view at the time of the trigger.
            var visibleLayer = layer.visible ?
                layer : layer;

            // Capture the action id.
            var id = event.action.id;

            if (id === "full-extent") {

                // if the full-extent action is triggered then navigate
                // to the full extent of the visible layer
                view.goTo(visibleLayer.fullExtent);

            } else if (id === "information") {

                // if the information action is triggered, then
                // open the item details page of the service layer
                window.open(visibleLayer.url);

            } else if (id === "increase-opacity") {

                // if the increase-opacity action is triggered, then
                // increase the opacity of the GroupLayer by 0.25

                if (layer.opacity < 1) {
                    layer.opacity += 0.25;
                }
            } else if (id === "decrease-opacity") {

                // if the decrease-opacity action is triggered, then
                // decrease the opacity of the GroupLayer by 0.25

                if (layer.opacity > 0) {
                    layer.opacity -= 0.25;
                }
            }
        });


        //add the search widget
        view.ui.add(searchWidget, {
            position: "top-right"
        });

        // Add widget to the top right corner of the view
        view.ui.add(layerList, "top-right");
    });

    // Create a BasemapGallery widget instance and set
    // its container to a div element

    var basemapGallery = new BasemapGallery({
        view: view,
        container: document.createElement("div")
    });

    // Create an Expand instance and set the content
    // property to the DOM node of the basemap gallery widget
    // Use an Esri icon font to represent the content inside
    // of the Expand widget

    var bgExpand = new Expand({
        view: view,
        content: basemapGallery.container,
        expandIconClass: "esri-icon-basemap"
    });


    // Add the expand instance to the ui
    view.ui.add(bgExpand, "top-left");

    // Add legend onto the map
    //view.ui.add(legend, "bottom-left");




    // add the button for the draw tool
    view.ui.add("draw-polygon", "top-left");

    view.when(function(evt) {
        var draw = new Draw({
            view: view
        });

        // *******************
        // draw polygon button
        // *******************
        var drawPolygonButton = document.getElementById("draw-polygon");
        drawPolygonButton.addEventListener("click", function() {
            view.graphics.removeAll();
            enableCreatePolygon(draw, view);
        });
    });

    function enableCreatePolygon(draw, view) {
        // create() will return a reference to an instance of PolygonDrawAction
        var action = draw.create("polygon");

        // focus the view to activate keyboard shortcuts for drawing polygons
        view.focus();

        // listen to vertex-add event on the action
        action.on("vertex-add", drawPolygon);

        // listen to cursor-update event on the action
        action.on("cursor-update", drawPolygon);

        // listen to vertex-remove event on the action
        action.on("vertex-remove", drawPolygon);

        // *******************************************
        // listen to draw-complete event on the action
        // *******************************************
        action.on("draw-complete", drawPolygon);
    }

    // this function is called from the polygon draw action events
    // to provide a visual feedback to users as they are drawing a polygon
    function drawPolygon(evt) {
        var vertices = evt.vertices;

        //remove existing graphic
        view.graphics.removeAll();

        // create a new polygon
        var polygon = createPolygon(vertices);

        // create a new graphic representing the polygon, add it to the view
        var graphic = createGraphic(polygon);
        view.graphics.add(graphic);

        // calculate the area of the polygon
        var area = geometryEngine.geodesicArea(polygon, "acres");
        if (area < 0) {
            // simplify the polygon if needed and calculate the area again
            var simplifiedPolygon = geometryEngine.simplify(polygon);
            if (simplifiedPolygon) {
                area = geometryEngine.geodesicArea(simplifiedPolygon, "acres");
            }
        }
        // start displaying the area of the polygon
        labelAreas(polygon, area);
    }

    // create a polygon using the provided vertices
    function createPolygon(vertices) {
        return new Polygon({
            rings: vertices,
            spatialReference: view.spatialReference
        });
    }

    // create a new graphic representing the polygon that is being drawn on the view
    function createGraphic(polygon) {
        graphic = new Graphic({
            geometry: polygon,
            symbol: {
                type: "simple-fill", // autocasts as SimpleFillSymbol
                color: [178, 102, 234, 0.8],
                style: "solid",
                outline: { // autocasts as SimpleLineSymbol
                    color: [255, 255, 255],
                    width: 2
                }
            }
        });
        return graphic;
    }

    //Label polyon with its area
    function labelAreas(geom, area) {
        var graphic = new Graphic({
            geometry: geom.centroid,
            symbol: {
                type: "text",
                color: "white",
                haloColor: "black",
                haloSize: "1px",
                text: area.toFixed(2) + " acres",
                xoffset: 3,
                yoffset: 3,
                font: { // autocast as Font
                    size: 14,
                    family: "sans-serif"
                }
            }
        });
        view.graphics.add(graphic);
    }


});
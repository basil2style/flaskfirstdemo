var app = angular.module("app",[]);

app.controller("AppCtrl",function($http) {
    var app = this

    $http.get("/api/pin").success(function (data) {

        app.pins = data.objects;

    })
    app.addPin = function() {
        $http.post("api/pin",{"title":"New Title","image":12}).success(function (data) {
            app.pins.push(data);
        })
    }
})
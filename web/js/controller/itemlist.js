'use strict';

/* Controllers */
var module = angular.module('app.controllers');
module.controller("itemlist", function($http, $scope) {
    Array.prototype.removeByValue = function(val) {  
        for (var i = 0; i < this.length; i++) {    
            if (this[i] == val) {       this.splice(i, 1);      
                break;     }   }
    }
    $scope.itemlist = [];
    $scope.sources = [{ "name": "京东", "type": "1", "checked": false }, { "name": "淘宝", "type": "2", "checked": false }]
    $scope.keyword = "";

    $scope.post = {
        "source": [],
        "keyword": $scope.keyword
    }
    $scope.addSource = function(item) {
        if (item.checked) {
            $scope.post.source.removeByValue(item.type)
        }
        else{
        	$scope.post.source.push(item.type)	
        }
        item.checked = !item.checked
    }
    $scope.getList = function() {
    	$scope.postData={}
    	$scope.postData.keyword=$scope.keyword
    	$scope.postData.source=$scope.post.source.join(",")
        $.ajax({
                type: "post",
                data: $scope.postData,
                "url": "http://localhost:5000/api/getList/",
                "success": function(d) {
                	$scope.d=JSON.parse(d)
                    $scope.itemlist = $scope.d.data
                    $scope.$apply();
                }
            })
            // $http({
            //     "url": "http://localhost:5000/api/getList/",
            //     "method": "post",
            //     "headers": { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' },
            //     "data": { "keyword": "aa" },
            //     "transformRequest": transformUrlEncoded
            // }).success(function(r) {
            //     $scope.itemlist = JSON.parse(r)
            // })  //这什么玩意
    }
    $scope.getList();
    $("#search").keydown(function(e){
    	if(e.keyCode==13){
    		$scope.getList();
    	}
    })

    $scope.showMenu=function(){
    	if($(".menu").css("display")=="none"){
    	$(".menu").slideDown()}
    	else{
    	$(".menu").slideUp()	
    	}
    }
})

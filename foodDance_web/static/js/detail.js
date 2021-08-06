
const serve_url = 'http://127.0.0.1:8000'

function getCookie(name){
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");

    if(arr=document.cookie.match(reg))

        return unescape(arr[2]);
    else
        return null;
}

function login(){
    alert('You have to login fisrtly')

}


function likeIt(recipe_id, user_id){
    eventWithServer(recipe_id,user_id,'/like/','likeAmount','likeIcon','like','dislike','dislike')

}


function collectIt(recipe_id, user_id){
    eventWithServer(recipe_id,user_id,'/collect/','collectAmount','collectIcon','collect','discollect','discollect')
}


function eventWithServer(recipe_id, user_id,url, ele_id, icon_id ,selected_icon_name,unselected_icon_name,unselected_condition){

    let httpRequest =new XMLHttpRequest();

    httpRequest.open('POST', serve_url + url,true);
    httpRequest.setRequestHeader("X-CSRFToken",getCookie("csrftoken"));

    httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    body = "recipe=" + recipe_id + "&user=" + user_id;
    httpRequest.send(body);

    httpRequest.onreadystatechange =function () {
    if (httpRequest.readyState == 4 && httpRequest.status == 200) {
        var data = JSON.parse(httpRequest.responseText)

        var ele = document.getElementById(ele_id)
        var icon = document.getElementById(icon_id)

        if (data.result == unselected_condition){
            ele.innerText = parseInt(ele.innerText) - 1;
            icon.src = icon.src.split('images/')[0] + "images/" + unselected_icon_name + ".svg"
        }
        else {
            ele.innerText = parseInt(ele.innerText) + 1;
            icon.src = icon.src.split('images/')[0] + "images/" + selected_icon_name + ".svg"
        }

    }
    };
}

function share(id){
    let httpRequest =new XMLHttpRequest();

    httpRequest.open('POST', '/share/',true);
    httpRequest.setRequestHeader("X-CSRFToken",getCookie("csrftoken"));

    httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    body = "recipe=" + id
    httpRequest.send(body);

    httpRequest.onreadystatechange =function () {
    if (httpRequest.readyState == 4 && httpRequest.status == 200) {
        var data = JSON.parse(httpRequest.responseText)
        var ele = document.getElementById('shareAmount')

        if (data.result == 'success'){
            ele.innerText = parseInt(ele.innerText) + 1;
        }
    }
}
}

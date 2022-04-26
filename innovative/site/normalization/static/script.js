let content1 = document.getElementById('content1');
let content2 = document.getElementById('content2');
let content3 = document.getElementById('content3');
let content4 = document.getElementById('content4');
let content5 = document.getElementById('content5');
let content6 = document.getElementById('content6');
let content7 = document.getElementById('content7');

function onBtn1() {
    content1.style.display = "flex";
    content2.style.display = "none";
    content3.style.display = "none";
    content4.style.display = "none";
    content5.style.display = "none";
    content6.style.display = "none";
    content7.style.display = "none";
}

function onBtn2() {
    content1.style.display = "none";
    content2.style.display = "flex";
    content3.style.display = "none";
    content4.style.display = "none";
    content5.style.display = "none";
    content6.style.display = "none";
    content7.style.display = "none";
}

function onBtn3() {
    content1.style.display = "none";
    content2.style.display = "none";
    content3.style.display = "flex";
    content4.style.display = "none";
    content5.style.display = "none";
    content6.style.display = "none";
    content7.style.display = "none";
}

function onBtn4() {
    content1.style.display = "none";
    content2.style.display = "none";
    content3.style.display = "none";
    content4.style.display = "flex";
    content5.style.display = "none";
    content6.style.display = "none";
    content7.style.display = "none";
}

function onBtn5() {
    content1.style.display = "none";
    content2.style.display = "none";
    content3.style.display = "none";
    content4.style.display = "none";
    content5.style.display = "flex";
    content6.style.display = "none";
    content7.style.display = "none";
}

function onBtn6() {
    content1.style.display = "none";
    content2.style.display = "none";
    content3.style.display = "none";
    content4.style.display = "none";
    content5.style.display = "none";
    content6.style.display = "flex";
    content7.style.display = "none";
}

function onBtn7() {
    content1.style.display = "none";
    content2.style.display = "none";
    content3.style.display = "none";
    content4.style.display = "none";
    content5.style.display = "none";
    content6.style.display = "none";
    content7.style.display = "flex";
}



// Logic For Dynamic Functional Dependencies
var add_new_fd = document.querySelector("#add_new_fd")
var parent = document.querySelector("#fd_parent")

var i=2
add_new_fd.addEventListener('click', (e)=>{
    e.preventDefault()
    console.log("Success")
    var html = `<div class="d-flex justify-content-between my-2" id="` + i.toString() + `">
            <span><input type="text" name="key`+ i.toString() + `" class="form-control"></span>
            <span><i class="fas fa-arrow-right"> </i></span>
            <span><input type="text" name="value`+ i.toString() + `" class="form-control"></span>
            <button class="btn btn-danger delete" onclick="delete_section(`+ i.toString() +`)">Delete</button>
        </div>`

    var count = document.getElementById("count")
    count.value = i.toString()
    parent.innerHTML += html
    i+=1
});

function delete_section(id){
    Event.preventDefault
    var my_section = document.getElementById(id)
    parent.removeChild(my_section)

    i-=1
    var count = document.getElementById("count")
    count.value = (parseInt(count.value) - 1).toString()
}
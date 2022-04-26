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
    i+=1
    parent.innerHTML += html
});

function delete_section(id){
    Event.preventDefault
    var my_section = document.getElementById(id)
    parent.removeChild(my_section)
}
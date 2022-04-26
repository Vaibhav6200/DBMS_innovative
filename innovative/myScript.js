var add_new_fd = document.querySelector("#add_new_fd")
var parent = document.querySelector("#fd_parent")


let i=2
add_new_fd.addEventListener('click', (e)=>{
    e.preventDefault()
    console.log("Add Button Clicked")

    const child = document.createElement("div")
    child.classList.add("d-flex", "justify-content-between",  "my-2")

    const span1 = document.createElement("span")
    const first_input = document.createElement("input")
    first_input.classList.add("form-control")
    first_input.type = 'text'
    first_input.name = "key" + i.toString()
    span1.appendChild(first_input)

    const span2 = document.createElement("span")
    const icon = document.createElement("i")
    icon.classList.add('fas', 'fa-arrow-right')
    span2.appendChild(icon)



    const span3 = document.createElement("span")
    const second_input = document.createElement("input")
    second_input.classList.add("form-control")
    second_input.type = 'text'
    second_input.name = "value" + i.toString()
    span3.appendChild(second_input)


    // <button class="btn btn-danger">Delete</button>
    const button = document.createElement("button")
    button.classList.add('btn', 'btn-danger')
    button.innerHTML = 'Delete'

    i = i+1

    child.appendChild(span1)
    child.appendChild(span2)
    child.appendChild(span3)
    child.appendChild(button)
    parent.appendChild(child)
})
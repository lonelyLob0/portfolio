const projects = document.getElementsByClassName("project")
const projects_container = document.getElementsByClassName("projects-container")
const next_btn = document.getElementById("next-btn")
const previous_btn = document.getElementById("previous-btn")
let index = 0
let projects_count = projects.length - 1

function change_project(){
     if(index > projects_count) {
        index = 0
    }
    else if (index < 0) {
        index = projects_count
    }
    projects_container.item(0).style.transform = `translateX(${-index * 432}px)`
}

next_btn.addEventListener("click", () => {
    index++
    change_project()
})

previous_btn.addEventListener("click", () => {
    index--
    change_project()
})
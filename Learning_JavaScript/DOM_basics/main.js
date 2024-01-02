

console.log(document.body.children)
console.log(typeof document.body.children) // not an array
console.log(Array.from(document.body.children)) // This is how to convert to an array

let links = document.body.getElementsByTagName("a") // Live // Object containing all the a tag elements
let some_image = document.getElementById("some-image") // Live 
let divs = document.body.getElementsByTagName("div")

console.log(links)
console.log(some_image)
console.log(links[1].innerHTML)
console.log(links[1].innerText)
console.log(some_image.src)
console.log(document.querySelectorAll(".div1 p")) // Not Live // elements inside div1 class with p tag

divs[0].setAttribute("style","background-color:red;")

let test_button_click_action = function() {
    let links = document.body.getElementsByTagName("a") // Live 

    document.body.setAttribute("style","background-color:powderblue;")

    console.log(links)

    for(let i = links.length-1; i >= 0; i--) { // <--------- Important - getElementsByTagName is a live function so the loop starts from the end
        let link = links[i]
        console.log(link.innerText)
        let text_node = document.createTextNode('---')
        link.parentNode.replaceChild(text_node, link)
    }
}







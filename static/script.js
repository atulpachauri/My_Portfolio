function toggleGreeting() {
    let heading = document.getElementById("greeting");
    if (heading.innerText === "Hello World") {
        heading.innerText = "Goodbye World";
    } else {
        heading.innerText = "Hello World";
    }
}
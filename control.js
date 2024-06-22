document.addEventListener("DOMContentLoaded", function () {
    const button1 = document.getElementById("button1");
    const button2 = document.getElementById("button2");
    const button3 = document.getElementById("button3");
    const content = document.getElementById("content");

    const slides = content.children;

    button1.addEventListener("click", () => {
        Array.from(slides).forEach(slide => slide.style.display = 'none');
        content.querySelector(".slide-1").style.display = 'block';
    });

    button2.addEventListener("click", () => {
        Array.from(slides).forEach(slide => slide.style.display = 'none');
        content.querySelector(".slide-2").style.display = 'block';
    });

    button3.addEventListener("click", () => {
        Array.from(slides).forEach(slide => slide.style.display = 'none');
        content.querySelector(".slide-3").style.display = 'block';
    });
});
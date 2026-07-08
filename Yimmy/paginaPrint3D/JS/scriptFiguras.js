let currentIndex = 0

function moveSlide(button, direction) {
    const slider = button.parentElement;
    const slides = slider.querySelector('.slides');
    const totalSlides = slides.children.length;

    let currentIndex = Number(slider.dataset.index || 0);

    currentIndex = (currentIndex + direction + totalSlides) % totalSlides;
    slides.style.transform = `translateX(-${currentIndex * 100}%)`;
    slider.dataset.index = currentIndex;
}
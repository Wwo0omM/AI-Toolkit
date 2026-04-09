// Parallax effect on mouse move
document.addEventListener('DOMContentLoaded', function() {
    const starfield = document.getElementById('starfield');

    if (!starfield) return;

    let mouseX = 0;
    let mouseY = 0;
    let currentX = 0;
    let currentY = 0;

    // Track mouse position
    document.addEventListener('mousemove', function(e) {
        mouseX = (e.clientX / window.innerWidth - 0.5) * 2;
        mouseY = (e.clientY / window.innerHeight - 0.5) * 2;
    });

    // Smooth parallax animation
    function animate() {
        // Smooth interpolation
        currentX += (mouseX - currentX) * 0.05;
        currentY += (mouseY - currentY) * 0.05;

        // Apply subtle parallax transform
        const translateX = currentX * 20;
        const translateY = currentY * 20;

        starfield.style.transform = `translate(${translateX}px, ${translateY}px)`;

        requestAnimationFrame(animate);
    }

    animate();
});

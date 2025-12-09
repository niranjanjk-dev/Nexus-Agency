document.addEventListener('DOMContentLoaded', () => {
    const marker = document.querySelector('#nav-marker');
    const links = document.querySelectorAll('.nav-links a');

    // Function to move the dot
    function moveMarker(element) {
        // Calculate center position
        const leftPosition = element.offsetLeft + (element.offsetWidth / 2) - 3; // -3 is half of dot width
        
        marker.style.left = `${leftPosition}px`;
        marker.classList.add('visible');
    }

    // Initialize position based on the currently 'active' link
    const activeLink = document.querySelector('.nav-links a.active');
    if (activeLink) {
        moveMarker(activeLink);
    }

    // Handle clicks
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            // e.preventDefault(); // Uncomment if you don't want the page to reload

            // Remove active class from others
            links.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked
            this.classList.add('active');

            // Move the dot
            moveMarker(this);
        });
    });

    // Handle Window Resize (so dot stays centered if screen changes)
    window.addEventListener('resize', () => {
        const currentActive = document.querySelector('.nav-links a.active');
        if (currentActive) moveMarker(currentActive);
    });
});

/* --- HERO SCROLL FADE EFFECT --- */
document.addEventListener('scroll', function() {
    const scrollY = window.scrollY;
    
    // Select elements
    const heroImage = document.querySelector('.hero-faded-image-container');
    const heroText = document.querySelector('.hero-text-content');

    // 1. Fade out the Image
    // It will be fully invisible after scrolling 600px
    if (heroImage) {
        let imageOpacity = 1 - (scrollY / 600);
        // Ensure opacity never goes below 0
        heroImage.style.opacity = Math.max(0, imageOpacity);
    }

    // 2. Fade out the Text (Slightly faster for depth effect)
    if (heroText) {
        let textOpacity = 1 - (scrollY / 400);
        heroText.style.opacity = Math.max(0, textOpacity);
        
        // Optional: Move text up slightly as it fades
        heroText.style.transform = `translateY(-${scrollY * 0.2}px)`;
    }

    /* --- SCROLL REVEAL ANIMATIONS --- */
    const observerOptions = {
        threshold: 0.2, // Trigger when 20% of element is visible
        rootMargin: "0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add 'reveal-effect' to the shutter mask
                const mask = entry.target.querySelector('.shutter-mask');
                if (mask) mask.classList.add('reveal-effect');
                
                // Add generic 'in-view' class to section for other items
                entry.target.classList.add('in-view');
                
                // Stop observing once animated
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Target the About Section
    const aboutSection = document.querySelector('.about-section');
    if (aboutSection) {
        observer.observe(aboutSection);
    }

    /* --- MOVABLE PHOTO SECTION (PARALLAX) --- */
    const scene = document.getElementById('parallax-scene');
    
    if (scene) {
        scene.addEventListener('mousemove', (e) => {
            const layers = scene.querySelectorAll('.visual-layer');
            
            // Get mouse position relative to the container center
            const x = (e.clientX - scene.getBoundingClientRect().left) / scene.offsetWidth - 0.5;
            const y = (e.clientY - scene.getBoundingClientRect().top) / scene.offsetHeight - 0.5;
            
            layers.forEach(layer => {
                // Get the speed from the HTML data-attribute
                const speed = layer.getAttribute('data-speed');
                
                // Calculate movement (Reverse direction for depth)
                const xMove = x * speed;
                const yMove = y * speed;
                
                // Apply subtle rotation for extra "luxury" feel
                const rotateX = y * 5; 
                const rotateY = x * -5;
                
                layer.style.transform = `translate(${xMove}px, ${yMove}px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
            });
        });

        // Reset to center when mouse leaves
        scene.addEventListener('mouseleave', () => {
            const layers = scene.querySelectorAll('.visual-layer');
            layers.forEach(layer => {
                layer.style.transform = `translate(0, 0) rotate(0)`;
                // Add a transition in CSS so it floats back smoothly
            });
        });
    }

    
});
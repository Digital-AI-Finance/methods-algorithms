/* Wiki Layout - Methods & Algorithms */

document.addEventListener('DOMContentLoaded', function() {
    initScrollSpy();
    initMobileMenu();
    initSmoothScroll();
});

/**
 * Scroll Spy - Highlights active section in TOC
 */
function initScrollSpy() {
    const sections = document.querySelectorAll('.section');
    const tocLinks = document.querySelectorAll('.toc-link');
    const navItems = document.querySelectorAll('.nav-item');

    if (sections.length === 0) return;

    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -60% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');

                // Update TOC links
                tocLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + id) {
                        link.classList.add('active');
                    }
                });

                // Update nav items
                navItems.forEach(item => {
                    item.classList.remove('active');
                    if (item.getAttribute('href') === '#' + id) {
                        item.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
}

/**
 * Mobile Menu Toggle
 */
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');

    if (!toggle || !sidebar) return;

    toggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
        if (overlay) overlay.classList.toggle('show');
    });

    if (overlay) {
        overlay.addEventListener('click', () => {
            sidebar.classList.remove('open');
            overlay.classList.remove('show');
        });
    }

    // Close sidebar when clicking a nav item on mobile
    const navItems = sidebar.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                sidebar.classList.remove('open');
                if (overlay) overlay.classList.remove('show');
            }
        });
    });
}

/**
 * Smooth Scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const target = document.querySelector(targetId);

            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Update URL without jumping
                history.pushState(null, null, targetId);
            }
        });
    });
}

/**
 * Build TOC dynamically from h3 elements within current section
 */
function buildDynamicToc(sectionId) {
    const section = document.getElementById(sectionId);
    const tocList = document.querySelector('.toc-list');

    if (!section || !tocList) return;

    // Clear existing sub-items
    tocList.querySelectorAll('.toc-item.sub').forEach(item => item.remove());

    // Find all h3 in section and add to TOC
    const headings = section.querySelectorAll('h3[id]');
    const sectionTocItem = tocList.querySelector(`a[href="#${sectionId}"]`)?.parentElement;

    if (sectionTocItem && headings.length > 0) {
        headings.forEach(h3 => {
            const li = document.createElement('li');
            li.className = 'toc-item sub';
            li.innerHTML = `<a href="#${h3.id}" class="toc-link sub">${h3.textContent}</a>`;
            sectionTocItem.after(li);
        });
    }
}

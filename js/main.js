/* Methods and Algorithms - Course Hub JavaScript */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize collapsible lecture sections
    initCollapsibles();

    // Open first lecture by default
    const firstLecture = document.querySelector('.lecture-card');
    if (firstLecture) {
        firstLecture.classList.add('open');
    }
});

/**
 * Initialize collapsible lecture sections
 */
function initCollapsibles() {
    const lectureHeaders = document.querySelectorAll('.lecture-header');

    lectureHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const card = this.closest('.lecture-card');

            // Toggle current card
            card.classList.toggle('open');
        });

        // Keyboard accessibility
        header.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });
}

/**
 * Expand all lecture sections
 */
function expandAll() {
    document.querySelectorAll('.lecture-card').forEach(card => {
        card.classList.add('open');
    });
}

/**
 * Collapse all lecture sections
 */
function collapseAll() {
    document.querySelectorAll('.lecture-card').forEach(card => {
        card.classList.remove('open');
    });
}

/**
 * Track download clicks (for analytics if needed)
 */
function trackDownload(category, name) {
    console.log(`Download: ${category} - ${name}`);
    // Can be extended for analytics integration
}

document.addEventListener("DOMContentLoaded", function () {
    function updateLang(tabName) {
        const lang = tabName.toLowerCase().includes("tiếng") || tabName.toLowerCase().includes("việt") ? "vi" : "en";
        document.body.setAttribute("data-lang", lang);
        console.log("Language set to:", lang, "from tab:", tabName); // Debug log

        // Directly filter ToC items
        filterToc(lang);
    }

    function filterToc(lang) {
        // Get all ToC links
        const tocLinks = document.querySelectorAll('.md-nav--secondary .md-nav__link');

        tocLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (!href) return;

            // Get the parent list item
            const listItem = link.closest('.md-nav__item');
            if (!listItem) return;

            // Check if this is a language-specific link
            if (href.includes('#en-') || href.includes('#vi-')) {
                if (lang === 'en' && href.includes('#vi-')) {
                    listItem.style.display = 'none';
                } else if (lang === 'vi' && href.includes('#en-')) {
                    listItem.style.display = 'none';
                } else {
                    listItem.style.display = '';
                }
            }
        });
    }

    // Initial check - default to English
    setTimeout(() => {
        const activeTab = document.querySelector(".tabbed-labels input:checked + label");
        if (activeTab) {
            console.log("Found active tab:", activeTab.innerText); // Debug log
            updateLang(activeTab.innerText);
        } else {
            console.log("No active tab found, defaulting to English"); // Debug log
            updateLang("English");
        }
    }, 100); // Small delay to ensure DOM is fully loaded

    // Watch for tab changes using event delegation
    document.addEventListener("click", function (e) {
        // Check if a tab label was clicked
        const label = e.target.closest(".tabbed-labels label");
        if (label) {
            setTimeout(() => {
                console.log("Tab clicked:", label.innerText); // Debug log
                updateLang(label.innerText);
            }, 50); // Small delay to ensure the tab is activated
        }
    });

    // Also watch for change events on radio inputs
    document.addEventListener("change", function (e) {
        if (e.target.matches(".tabbed-labels input")) {
            const label = e.target.nextElementSibling;
            if (label) {
                console.log("Tab changed via input:", label.innerText); // Debug log
                updateLang(label.innerText);
            }
        }
    });

    // Support for navigation between pages with content.tabs.link
    const observer = new MutationObserver(() => {
        const activeTab = document.querySelector(".tabbed-labels input:checked + label");
        if (activeTab) {
            updateLang(activeTab.innerText);
        }
    });

    const tabsContainer = document.querySelector(".md-content");
    if (tabsContainer) {
        observer.observe(tabsContainer, { childList: true, subtree: true });
    }

    // Also observe ToC changes (in case it's dynamically updated)
    const tocObserver = new MutationObserver(() => {
        const activeTab = document.querySelector(".tabbed-labels input:checked + label");
        if (activeTab) {
            const lang = activeTab.innerText.toLowerCase().includes("tiếng") || activeTab.innerText.toLowerCase().includes("việt") ? "vi" : "en";
            filterToc(lang);
        } else {
            // Default to English
            filterToc("en");
        }
    });

    const tocContainer = document.querySelector('.md-nav--secondary');
    if (tocContainer) {
        tocObserver.observe(tocContainer, { childList: true, subtree: true });
    }
});

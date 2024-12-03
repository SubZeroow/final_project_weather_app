// Switch tabs between Sign Up and Login
document.addEventListener("DOMContentLoaded", function() {
    // Get all tab links
    const tabLinks = document.querySelectorAll(".tablinks");
    
    // Get all tab content
    const tabContents = document.querySelectorAll(".tabcontent");
    
    // Function to handle tab switching
    function switchTab(event) {
        // Remove the 'active' class from all tab links and content
        tabLinks.forEach(tab => tab.classList.remove("active"));
        tabContents.forEach(content => content.classList.remove("active"));
        
        // Add 'active' class to the clicked tab and its corresponding content
        event.target.classList.add("active");
        const activeTabContent = document.querySelector(`#${event.target.dataset.target}`);
        activeTabContent.classList.add("active");
    }
    
    // Add event listeners to each tab
    tabLinks.forEach(tab => {
        tab.addEventListener("click", switchTab);
    });

    // Initially activate the first tab
    tabLinks[0].classList.add("active");
    tabContents[0].classList.add("active");
});
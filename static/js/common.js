document.addEventListener("DOMContentLoaded", function () {

    console.log("Common JS Loaded");

    // -----------------------------------
    // Floating Chat
    // -----------------------------------

    const chatButton = document.getElementById(
        "chatButton"
    );

    const chatPanel = document.getElementById(
        "chatPanel"
    );

    const closeChat = document.getElementById(
        "closeChat"
    );

    if (

        chatButton &&

        chatPanel &&

        closeChat

    ) {

        chatButton.addEventListener(

            "click",

            function () {

                chatPanel.classList.add(

                    "active"

                );

            }

        );

        closeChat.addEventListener(

            "click",

            function () {

                chatPanel.classList.remove(

                    "active"

                );

            }

        );

    }

    // -----------------------------------
    // Load Search Sources
    // -----------------------------------

    loadSearchSources();

});


// -----------------------------------
// Logout (Works on Every Page)
// -----------------------------------

document.addEventListener(

    "click",

    function (event) {

        const logoutBtn = event.target.closest(

            "#logoutBtn"

        );

        if (!logoutBtn) {

            return;

        }

        event.preventDefault();

        logout();

    }

);

function logout() {

    console.log("Logging Out...");

    localStorage.removeItem(

        "token"

    );

    localStorage.removeItem(

        "user"

    );

    window.location.replace(

        "/auth"

    );

}


// -----------------------------------
// Global Search Scope Loader
// -----------------------------------

async function loadSearchSources() {

    try {

        const select = document.getElementById(

            "searchScope"

        );

        if (!select) {

            return;

        }

        const response = await fetch(

            "/sources/list"

        );

        const sources = await response.json();

        select.innerHTML = "";

        select.innerHTML += `

            <option value="global">

                🌍 Global Search

            </option>

        `;

        sources.forEach(source => {

            const icon =

                source.startsWith("http")

                ? "🌐"

                : "📄";

            select.innerHTML += `

                <option value="${source}">

                    ${icon} ${source}

                </option>

            `;

        });

    }

    catch (error) {

        console.error(

            "loadSearchSources()",

            error

        );

    }

}


// -----------------------------------
// Refresh Entire Knowledge Base
// -----------------------------------

async function refreshKnowledgeBase() {

    try {

        if (

            typeof loadDocuments === "function"

        ) {

            await loadDocuments();

        }

        if (

            typeof loadWebsites === "function"

        ) {

            await loadWebsites();

        }

        if (

            typeof loadSearchSources === "function"

        ) {

            await loadSearchSources();

        }

        if (

            typeof loadAnalytics === "function"

        ) {

            await loadAnalytics();

        }

    }

    catch (error) {

        console.error(

            "refreshKnowledgeBase()",

            error

        );

    }

}




console.log("Website JS Loaded");

// --------------------------------------
// Elements
// --------------------------------------

const websiteInput =
document.getElementById(
    "websiteUrl"
);

const indexButton =
document.getElementById(
    "indexWebsite"
);

const websiteStatus =
document.getElementById(
    "websiteStatus"
);

const websiteScope =
document.getElementById(
    "websiteSearchScope"
);

const askWebsite =
document.getElementById(
    "askWebsite"
);

// --------------------------------------
// Event Listeners
// --------------------------------------

indexButton.addEventListener(

    "click",

    function(){

        indexWebsite();

    }

);

websiteInput.addEventListener(

    "keypress",

    function(e){

        if(e.key==="Enter"){

            indexWebsite();

        }

    }

);

// Save selected website scope

if(websiteScope){

    websiteScope.addEventListener(

        "change",

        function(){

            localStorage.setItem(

                "websiteScope",

                websiteScope.value

            );

        }

    );

}

// Open Chat

if(askWebsite){

    askWebsite.addEventListener(

        "click",

        function(){

            document.getElementById(

                "chatButton"

            ).click();

        }

    );

}

// --------------------------------------
// Index Website
// --------------------------------------

async function indexWebsite(){

    const url = websiteInput.value.trim();

    if(url===""){

        alert(

            "Please enter a website URL."

        );

        return;

    }

    websiteStatus.innerHTML =

    `
    <div class="alert alert-info">

        Crawling Website...

    </div>
    `;

    try{

        const response = await fetch(

            "/website/index",

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify({

                    url:url

                })

            }

        );

        const data = await response.json();

        if(!data.success){

            throw new Error(

                data.message

            );

        }

        websiteStatus.innerHTML =

        `
        <div class="alert alert-success">

            <strong>

                Website Indexed Successfully ✅

            </strong>

            <br>

            Chunks Created :

            ${data.chunks}

        </div>
        `;

        websiteInput.value="";

        await loadWebsites();

        await loadWebsiteSources();

        if(typeof loadAnalytics==="function"){

            loadAnalytics();

        }

    }

    catch(error){

        console.error(error);

        websiteStatus.innerHTML =

        `
        <div class="alert alert-danger">

            ${error.message}

        </div>
        `;

    }

}

// --------------------------------------
// Load Websites
// --------------------------------------

async function loadWebsites(){

    try{

        const response = await fetch(

            "/website/list"

        );

        const websites = await response.json();

        const table = document.getElementById(

            "websiteTable"

        );

        table.innerHTML="";

        websites.forEach(site=>{

            table.innerHTML +=

            `
            <tr>

                <td>

                    ${site}

                </td>

                <td>

                    <span class="badge bg-success">

                        Indexed

                    </span>

                </td>

                <td>

                    <button

                        class="btn btn-danger btn-sm"

                        onclick="deleteWebsite('${site}')">

                        Delete

                    </button>

                </td>

            </tr>
            `;

        });

        document.getElementById(

            "websiteCount"

        ).innerText = websites.length;

    }

    catch(error){

        console.error(

            "loadWebsites()",

            error

        );

    }

}

// --------------------------------------
// Delete Website
// --------------------------------------

async function deleteWebsite(url){

    if(!confirm(

        `Delete ${url}?`

    )){

        return;

    }

    try{

        await fetch(

            "/website/delete",

            {

                method:"DELETE",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify({

                    url:url

                })

            }

        );

        await loadWebsites();

        await loadWebsiteSources();

        if(typeof loadAnalytics==="function"){

            loadAnalytics();

        }

    }

    catch(error){

        console.error(error);

    }

}

// --------------------------------------
// Website Search Scope
// --------------------------------------

async function loadWebsiteSources(){

    try{

        const response = await fetch(

            "/sources/websites"

        );

        const websites = await response.json();

        if(!websiteScope){

            return;

        }

        websiteScope.innerHTML =

        `
        <option value="global">

            🌍 Global Websites

        </option>
        `;

        websites.forEach(site=>{

            websiteScope.innerHTML +=

            `
            <option value="${site}">

                🌐 ${site}

            </option>
            `;

        });

        const savedScope =

        localStorage.getItem(

            "websiteScope"

        );

        if(

            savedScope &&

            websites.includes(savedScope)

        ){

            websiteScope.value = savedScope;

        }

    }

    catch(error){

        console.error(

            "loadWebsiteSources()",

            error

        );

    }

}

// --------------------------------------
// Initial Load
// --------------------------------------

window.onload = async function(){

    await loadWebsites();

    await loadWebsiteSources();

};
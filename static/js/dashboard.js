console.log("Dashboard Loaded");

async function loadDashboard(){

    try{

        const response = await fetch(

            "/dashboard/stats"

        );

        const data = await response.json();

        document.getElementById(

            "documents"

        ).innerText = data.documents;

        document.getElementById(

            "websites"

        ).innerText = data.websites;

        document.getElementById(

            "chunks"

        ).innerText = data.chunks;

        document.getElementById(

            "sources"

        ).innerText = data.sources;

        document.getElementById(

            "storage"

        ).innerText =

            data.storage + " MB";

        document.getElementById(

            "llm"

        ).innerText =

            data.llm;

        document.getElementById(

            "embedding"

        ).innerText =

            data.embedding;

        document.getElementById(

            "vectordb"

        ).innerText =

            data.vector_db;

        document.getElementById(

            "status"

        ).innerText =

            data.status;

    }

    catch(error){

        console.error(error);

    }

}

document.addEventListener(

    "DOMContentLoaded",

    function(){

        loadDashboard();

        const assistant =

        document.getElementById(

            "openAssistant"

        );

        if(assistant){

            assistant.onclick = function(){

                document.getElementById(

                    "chatButton"

                ).click();

            };

        }

    }

);

window.onload = loadDashboard;
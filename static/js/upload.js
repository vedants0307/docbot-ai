console.log("UPLOAD JS LOADED");

// ------------------------------------
// Elements
// ------------------------------------

const browseBtn =
document.getElementById(
    "browseBtn"
);

const fileInput =
document.getElementById(
    "fileInput"
);

const uploadStatus =
document.getElementById(
    "uploadStatus"
);

const documentScope =
document.getElementById(
    "documentSearchScope"
);

// ------------------------------------
// Browse Files
// ------------------------------------

browseBtn.addEventListener(

    "click",

    function(){

        fileInput.click();

    }

);

// ------------------------------------
// File Selected
// ------------------------------------

fileInput.addEventListener(

    "change",

    function(){

        uploadFiles();

    }

);

// ------------------------------------
// Save Search Scope
// ------------------------------------

if(documentScope){

    documentScope.addEventListener(

        "change",

        function(){

            localStorage.setItem(

                "documentScope",

                documentScope.value

            );

        }

    );

}

// ------------------------------------
// Upload Files
// ------------------------------------

async function uploadFiles(){

    const files = fileInput.files;

    if(files.length===0){

        return;

    }

    const formData = new FormData();

    for(const file of files){

        formData.append(

            "files",

            file

        );

    }

    uploadStatus.innerHTML =

    `
    <div class="alert alert-info">

        Uploading Documents...

    </div>
    `;

    try{

        const response = await fetch(

            "/upload/upload_files",

            {

                method:"POST",

                body:formData

            }

        );

        const data = await response.json();

        uploadStatus.innerHTML = "";

        data.documents.forEach(doc=>{

            uploadStatus.innerHTML +=

            `
            <div class="alert alert-success">

                <strong>

                    ${doc.filename}

                </strong>

                <br>

                ${doc.updated

                    ? "Updated Successfully 🔄"

                    : "Indexed Successfully ✅"

                }

                <br>

                Chunks Created :

                <strong>

                    ${doc.chunks}

                </strong>

            </div>
            `;

        });

        await loadDocuments();

        await loadDocumentSources();

    }

    catch(error){

        console.error(error);

        uploadStatus.innerHTML =

        `
        <div class="alert alert-danger">

            Upload Failed

        </div>
        `;

    }

}

// ------------------------------------
// Load Documents
// ------------------------------------

async function loadDocuments(){

    try{

        const response = await fetch(

            "/upload/documents"

        );

        const docs = await response.json();

        const table = document.getElementById(

            "documentsTable"

        );

        table.innerHTML="";

        docs.forEach(doc=>{

            const extension =

            doc.split(".").pop().toUpperCase();

            table.innerHTML +=

            `
            <tr>

                <td>

                    ${doc}

                </td>

                <td>

                    ${extension}

                </td>

                <td>

                    <span class="badge bg-success">

                        Uploaded

                    </span>

                </td>

                <td>

                    <button

                        class="btn btn-danger btn-sm"

                        onclick="deleteDocument('${doc}')">

                        Delete

                    </button>

                </td>

            </tr>
            `;

        });

    }

    catch(error){

        console.error(

            "loadDocuments()",

            error

        );

    }

}

// ------------------------------------
// Delete Document
// ------------------------------------

async function deleteDocument(filename){

    if(!confirm(

        `Delete "${filename}"?`

    )){

        return;

    }

    try{

        await fetch(

            "/upload/delete/" + filename,

            {

                method:"DELETE"

            }

        );

        await loadDocuments();

        await loadDocumentSources();

    }

    catch(error){

        console.error(error);

    }

}

// ------------------------------------
// Load Search Scope
// ------------------------------------

async function loadDocumentSources(){

    try{

        const response = await fetch(

            "/sources/documents"

        );

        const docs = await response.json();

        if(!documentScope){

            return;

        }

        documentScope.innerHTML =

        `
        <option value="global">

            🌍 Global Documents

        </option>
        `;

        docs.forEach(doc=>{

            documentScope.innerHTML +=

            `
            <option value="${doc}">

                📄 ${doc}

            </option>
            `;

        });

        const savedScope =

        localStorage.getItem(

            "documentScope"

        );

        if(

            savedScope &&

            docs.includes(savedScope)

        ){

            documentScope.value = savedScope;

        }

    }

    catch(error){

        console.error(

            "loadDocumentSources()",

            error

        );

    }

}

// ------------------------------------
// Initial Load
// ------------------------------------

window.onload = async function(){

    await loadDocuments();

    await loadDocumentSources();

};
document.addEventListener("DOMContentLoaded", () => {

    console.log("Chat Loaded");

    const input =
        document.getElementById("chatInput");

    const button =
        document.getElementById("sendMessage");

    const body =
        document.getElementById("chatBody");

    const welcome =
        document.getElementById("welcomeScreen");

    if (!input || !button || !body) {

        console.error("Chat Elements Missing");

        return;

    }

    button.addEventListener(

        "click",

        sendMessage

    );

    input.addEventListener(

        "keypress",

        function (e) {

            if (e.key === "Enter") {

                e.preventDefault();

                sendMessage();

            }

        }

    );

    async function sendMessage() {

        const question = input.value.trim();

        if (question === "") {

            return;

        }

        if (welcome) {

            welcome.remove();

        }

        addUserMessage(question);

        input.value = "";

        addThinking();

        button.disabled = true;

        // ---------------------------------
        // Determine Search Scope
        // ---------------------------------

        let scope = "global";

        const documentScope =

            document.getElementById(
                "searchScope"
            );

        const websiteScope =

            document.getElementById(
                "websiteSearchScope"
            );

        if (

            documentScope

        ) {

            scope = documentScope.value;

        }

        else if (

            websiteScope

        ) {

            scope = websiteScope.value;

        }

        console.log(

            "Current Scope:",

            scope

        );

        try {

            const response = await fetch(

                "/chat/send_message",

                {

                    method: "POST",

                    headers: {

                        "Content-Type": "application/json"

                    },

                    body: JSON.stringify({

                        question: question,

                        scope: scope

                    })

                }

            );

            if (!response.ok) {

                throw new Error(

                    "Server Error"

                );

            }

            const data = await response.json();

            removeThinking();

            addBotMessage(

                data.answer,
                data.sources

            );

        }

        catch (err) {

            console.error(err);

            removeThinking();

            addBotMessage(

                "Something went wrong."

            );

        }

        finally {

            button.disabled = false;

            input.focus();

        }

    }

    function addUserMessage(message) {

        body.innerHTML += `

            <div class="message-row user-row">

                <div class="user-message">

                    ${message}

                </div>

            </div>

        `;

        scrollBottom();

    }

    function addBotMessage(

        message,

        sources = []

    ) {

        let sourcesHTML = "";

        if (sources.length > 0) {

            const uniqueSources = [];

            const seen = new Set();

            sources.forEach(source => {

                const key =

                    source.source +

                    "_" +

                    source.page;

                if (!seen.has(key)) {

                    seen.add(key);

                    uniqueSources.push(source);

                }

            });

            sourcesHTML += `

                <div class="chat-sources">

                    <strong>

                        📚 Sources

                    </strong>

                    <ul>

            `;

            uniqueSources.forEach(source => {

                if (

                    source.type === "website"

                ) {

                    sourcesHTML += `

                        <li>

                            🌐 ${source.source}

                        </li>

                    `;

                }

                else {

                    sourcesHTML += `

                        <li>

                            📄 ${source.source}

                            ${source.page !== undefined
                                ? `(Page ${source.page + 1})`
                                : ""
                            }

                        </li>

                    `;

                }

            });

            sourcesHTML += `

                    </ul>

                </div>

            `;

        }
        const html = marked.parse(message);
        
        body.innerHTML += `

            <div class="message-row">

                <div class="bot-message">

                    ${html}

                    ${sourcesHTML}

                </div>

            </div>

        `;

        scrollBottom();

    }

    function addThinking() {

        body.innerHTML += `

            <div
                id="thinking"
                class="message-row">

                <div class="bot-message typing">

                    <span></span>

                    <span></span>

                    <span></span>

                </div>

            </div>

        `;

        scrollBottom();

    }

    function removeThinking() {

        const thinking =

            document.getElementById(

                "thinking"

            );

        if (

            thinking

        ) {

            thinking.remove();

        }

    }

    function scrollBottom() {

        body.scrollTop =

            body.scrollHeight;

    }

});
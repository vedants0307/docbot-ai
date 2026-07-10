if (

    localStorage.getItem(

        "token"

    )

) {

    window.location.href =

        "/dashboard/";

}

document.addEventListener(

    "DOMContentLoaded",

    function () {

        console.log("Login Loaded");

        const email =

            document.getElementById(

                "email"

            );

        const password =

            document.getElementById(

                "password"

            );

        const loginBtn =

            document.getElementById(

                "loginBtn"

            );

        const alertBox =

            document.getElementById(

                "loginAlert"

            );

        loginBtn.addEventListener(

            "click",

            login

        );

        password.addEventListener(

            "keypress",

            function (e) {

                if (

                    e.key === "Enter"

                ) {

                    login();

                }

            }

        );

        async function login() {

            const emailValue =

                email.value.trim();

            const passwordValue =

                password.value.trim();

            if (

                emailValue === "" ||

                passwordValue === ""

            ) {

                showAlert(

                    "Please fill all fields.",

                    "danger"

                );

                return;

            }

            loginBtn.disabled = true;

            loginBtn.innerText =

                "Logging in...";

            try {

                const response = await fetch(

                    "/auth/login",

                    {

                        method: "POST",

                        headers: {

                            "Content-Type":

                                "application/json"

                        },

                        body: JSON.stringify(

                            {

                                email:

                                    emailValue,

                                password:

                                    passwordValue

                            }

                        )

                    }

                );

                const data =

                    await response.json();

                if (

                    !data.success

                ) {

                    throw new Error(

                        data.message

                    );

                }

                localStorage.setItem(

                    "token",

                    data.token

                );

                localStorage.setItem(

                    "user",

                    JSON.stringify(

                        data.user

                    )

                );

                window.location.href =

                    "/dashboard/";

            }

            catch (error) {

                showAlert(

                    error.message,

                    "danger"

                );

            }

            finally {

                loginBtn.disabled = false;

                loginBtn.innerText =

                    "Login";

            }

        }

        function showAlert(

            message,

            type

        ) {

            alertBox.innerHTML =

                `

                <div class="alert alert-${type}">

                    ${message}

                </div>

                `;

        }

    }

);
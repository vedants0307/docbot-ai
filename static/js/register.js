document.addEventListener(

    "DOMContentLoaded",

    function () {

        const name =

            document.getElementById("name");

        const email =

            document.getElementById("email");

        const password =

            document.getElementById("password");

        const confirmPassword =

            document.getElementById("confirmPassword");

        const registerBtn =

            document.getElementById("registerBtn");

        const alertBox =

            document.getElementById("registerAlert");

        registerBtn.addEventListener(

            "click",

            register

        );

        async function register() {

            if (

                name.value.trim() === "" ||

                email.value.trim() === "" ||

                password.value.trim() === "" ||

                confirmPassword.value.trim() === ""

            ) {

                return showAlert(

                    "Please fill all fields.",

                    "danger"

                );

            }

            if (

                password.value !==

                confirmPassword.value

            ) {

                return showAlert(

                    "Passwords do not match.",

                    "danger"

                );

            }

            registerBtn.disabled = true;

            registerBtn.innerText =

                "Creating Account...";

            try {

                const response = await fetch(

                    "/auth/register",

                    {

                        method: "POST",

                        headers: {

                            "Content-Type":

                                "application/json"

                        },

                        body: JSON.stringify(

                            {

                                name:

                                    name.value.trim(),

                                email:

                                    email.value.trim(),

                                password:

                                    password.value

                            }

                        )

                    }

                );

                const data =

                    await response.json();

                if (!data.success) {

                    throw new Error(

                        data.message

                    );

                }

                showAlert(

                    "Registration Successful! Redirecting...",

                    "success"

                );

                setTimeout(

                    function () {

                        window.location.href =

                            "/auth/login";

                    },

                    1500

                );

            }

            catch (error) {

                showAlert(

                    error.message,

                    "danger"

                );

            }

            finally {

                registerBtn.disabled = false;

                registerBtn.innerText =

                    "Register";

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
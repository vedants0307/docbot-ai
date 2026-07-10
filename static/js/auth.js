function getToken() {

    return localStorage.getItem(

        "token"

    );

}

function getUser() {

    const user = localStorage.getItem(

        "user"

    );

    if (!user) {

        return null;

    }

    return JSON.parse(

        user

    );

}

function logout() {

    localStorage.removeItem(

        "token"

    );

    localStorage.removeItem(

        "user"

    );

    window.location.href =

        "/auth/login";

}

function requireLogin() {

    if (!getToken()) {

        window.location.href =

            "/auth/login";

    }

}
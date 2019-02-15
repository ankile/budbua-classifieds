import axios from 'axios'

class Api {
    static headers() {
        let headers = {
            Accept: "application/json",
            "Content-Type": "application/json",
        };

        let token = localStorage.getItem("token");

        // JWT with bearer
        if (token) {
            let jwt= `JWT ${token}`;
            headers["Authorization"] = jwt;
        }

        return headers;
    }

    static config() {
        let config = {
            headers: Api.headers()
        }
    }
    static get(url) {
        const config = Api.config();
        return axios.get(url, config)
    }
}
import axios from 'axios'

export default class Api {
    static headers() {
        let headers = {
            Accept: "application/json",
            "Content-Type": "application/json",
        };

        //let token = localStorage.getItem("token");
        let token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6Iml2YXJubSIsImV4cCI6MTU4MTc3MjM0MCwiZW1haWwiOiJlZ2ZyYXVzQGdtYWlsLmNvbSJ9.cdxzgKZ_9yJNEsbmLmtegooyerfzxP2XywPt9FZEodc"
        // JWT with bearer
        if (token) {
            let jwt= `JWT ${token}`;
            headers["Authorization"] = jwt;
        }

        return headers;
    }

    static config() {
        return {
            headers: Api.headers()
        };
    }

    static addHostToPath(path) {
        const host = 'localhost:8000/'; //TODO make enviroment variable
        return host + path;
    }

    static get(url) {
        const fullPath = Api.addHostToPath(url);
        const config = Api.config();
        return axios.get(fullPath, config);
    }

    static post(url, data) {
        return axios.post(url, data, Api.config())
    }
}

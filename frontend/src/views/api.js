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
            headers["Authorization"] = `JWT ${token}`;
        }

        return headers;
    }

    static config() {
        return {
            headers: Api.headers(),
        };
    }

    static addHostToPath(path) {
        const host = String(process.env.VUE_APP_API_BASE_URL); //TODO make enviroment variable
        return host + path;
    }

    static get(url) {
        const fullPath = Api.addHostToPath(url);
        const config = Api.config();
        return axios.get(fullPath, config);
    }

    static post(url, data) {
        const fullPath = Api.addHostToPath(url);
        const config = Api.config();
        return axios.post(fullPath, data, config)
    }


}

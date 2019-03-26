import axios from 'axios'

export default class Api {
    static headers() {
        let headers = {
            Accept: "application/json",
            "Content-Type": "application/json",
        };

        let token = localStorage.getItem("token");
        if (token) {
            headers["Authorization"] = `JWT ${token}`;
        }

        return headers;
    }

    static config() {
        return {
            headers: Api.headers()
        };
    }

    static addHostToPath(path) {
        const host = 'http://localhost:8000'; //TODO make enviroment variable
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
        if (data) {
            return axios.post(fullPath, data, config);
        }
        else {
            return axios.post(fullPath, config);
        }
    }


    static delete(url) {
        const fullPath = Api.addHostToPath(url);
        const config = Api.config();
        return axios.delete(fullPath, config);
    }

}

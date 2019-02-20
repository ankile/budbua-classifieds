import axios from 'axios'


export {
    Api,
    User
}

class Api {
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
            headers: Api.headers(),
        };
    }

    static addHostToPath(path) {
        const host = String(process.env.VUE_APP_API_BASE_URL) || "localhost:8080"; //TODO make enviroment variable
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


class User extends Api{

    static login(email, password){
        this.post("/users/api-token-auth/", {email, password})
            .error(res=>{

            })
            .success(res=>{
                localStorage.setItem("token", JSON.stringify(res.token))
            })
    }

}

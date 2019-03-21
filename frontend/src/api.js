import axios from 'axios'
import jwt_decode from 'jwt-decode'


//TODO:: faktisk håndtere feilmeldinger :))


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
        const host = String(process.env.VUE_APP_API_BASE_URL);
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
    static put(url, data) {
        const fullPath = Api.addHostToPath(url);
        const config = Api.config();
        return axios.put(fullPath, data, config)
    }
    static delete(url) {
        const fullPath = Api.addHostToPath(url);
        const config = Api.config();
        return axios.delete(fullPath, config)
    }


}


class User extends Api {

    static isLoggedIn(){
        return new Promise((resolve, reject)=>{
            let token = localStorage.getItem('token');
            let a = jwt_decode(token);
            if (a) {
                resolve();
            }else{
                reject();
            }
        })
    }


    static login(email, password) {
        return new Promise((resolve, reject) => {
            this.post("/users/api-token-auth/", {email, password})

                .then(res => {
                    localStorage.setItem("token", res.data.token);
                    resolve();
                })

                .catch(err => {
                    alert("Brukernavn/Passord kombinasjon er feil. Prøv på nytt.")
                    reject();
                });
        });

    }



    static register(firstName, lastName, email, password, password2) {
        return new Promise((resolve, reject) => {
            this.post("/users/create/",
                {firstName, lastName, email, password, password2})
                .then(res => {
                    resolve();
                })

                .catch(err => {
                    reject();
                });
        });
    }

    static getCurrentUser(){
        return new Promise((resolve, reject) => {
            this.get("/users/")
                .then(res => {
                    resolve(res);
                })
                .catch(err => {
                    reject(err);
                });
        });
    }

    static updateUserInfo(email, firstName, lastName){
        return new Promise((resolve, reject) => {
            this.put("/users/", {email,firstName,lastName})
                .then(res => {
                    resolve(res);
                })
                .catch(err => {
                    reject(err);
                });
        });
    }

    static deleteUser(){
        return new Promise((resolve, reject) => {
            this.delete("/users/", {})
                .then(res => {
                    localStorage.removeItem("token");
                    resolve(res);
                })
                .catch(err => {
                    reject(err);
                });
        });
    }

}

import axios from 'axios'
import jwt_decode from 'jwt-decode'


//TODO:: faktisk håndtere feilmeldinger :))


export {
    Api,
    User,
    MessageApi}

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
            let token=localStorage.getItem('token');
            let a=jwt_decode(token);
            if(a){
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


class MessageApi extends Api{

    static createChat(userId){
        return new Promise((resolve, reject) => {
            this.post("/messages/", {with:userId})
                .then(res => {
                    resolve(res);
                })
                .catch(err => {
                    reject(err);
                });
        });
    }

    static openChat(userId){
        return new Promise((resolve, reject) => {

        });
    }

    static getChatWithUser(userId){
        return new Promise((resolve, reject) => {

        })
    }

    static getChat(chatId){
        return new Promise((resolve, reject) => {
            /*this.get("/messages/"+chatId, {})
                .then(res => {

                    resolve(res);
                })
                .catch(err => {
                    reject(err);
                });
                */
            let res={}
            switch(chatId){
                case "1":
                    res=[{from: 1, text: "vsfdsfds", time: 123}, {from: 2, text: "dsa g", time: 123}]
                    break;
                case "2":
                    res=[{from: 1, text: "f3efsdf", time: 123}, {from: 2, text: "22e44", time: 123}]
                    break;
                case "3":
                    res=[{from: 1, text: "gtggf", time: 123}, {from: 2, text: "wdwdwdw", time: 123}]
                    break;
            }
            resolve(res)
        });
    }

    static getAllChats(){
        return new Promise((resolve, reject)=>{
            let res=[
                {
                    chatId: "1",
                    displayName: 'Jo Nesbø',
                    latestMessage: {from: 1, text: "hallo", time: 123},
                    messages: [{from: 1, text: "hallgfgfo", time: 123}, {from: 2, text: "haldla", time: 123}]
                },
                {
                    chatId: "2",
                    displayName: 'Tor',
                    latestMessage: {from: 1, text: "hadllo", time: 133223},
                    messages: [{from: 1, text: "haldlo", time: 123}, {from: 2, text: "halla", time: 123}]
                },
                {
                    chatId: "3",
                    displayName: 'Gunnar',
                    latestMessage: {from: 1, text: "halwlo", time: 1423},
                    messages: [{from: 1, text: "hallasdo", time: 123}, {from: 2, text: "halla", time: 123}]
                }
            ]
            res.sort((a, b) => {
                return (a.latestMessage.time < b.latestMessage.time) ? 1 : -1
            });
            resolve(res)
        })
    }

    static fetchMessagesFromChat(ChatId, time){
        return new Promise((resolve, reject)=>{
            this.get("/messages/"+chatId+"?after="+time).then(res=>{
                resolve(res)
            })
        })
    }

    static sendMessage(chatId,text, time){
        return new Promise((resolve, reject) => {
            this.post("/messages/"+chatId, {text, time})
                .then(()=>{
                    resolve();
                })
                .catch(()=>{
                    reject();
                })
        })
    }

}

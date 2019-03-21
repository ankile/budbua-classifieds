
export default class {
    static getPrettyTime(datetime) {
        let hours = datetime.getHours().toString();
        let minutes = datetime.getMinutes().toString();
        const year = datetime.getFullYear().toString().substr(2);
        let month = (datetime.getMonth() + 1).toString();
        let day = datetime.getDay().toString();

        (day.length === 1) && (day = '0' + day); // eg. '4' => '04'
        (month.length === 1) && (month = '0' + month);
        (hours.length === 1) && (hours = '0' + hours);
        (minutes.length === 1) && (minutes = '0' + minutes);

        return hours + ':' + minutes + ' | ' + day + '.' + month + '.' + year;
    }
}


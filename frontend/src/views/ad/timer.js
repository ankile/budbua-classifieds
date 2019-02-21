// Methods for countdown timer on ads

export default class {
    static getTimeRemaining(endtime) {
        //todo: problem with UTC and timezones
        const now = new Date();
        const timediff = Date.parse(endtime) - Date.parse(now);
        const seconds = Math.floor((timediff / 1000) % 60);
        const minutes = Math.floor( (timediff/1000/60) % 60 );
        const hours = Math.floor( (timediff/(1000*60*60)) % 24 );
        const days = Math.floor( timediff/(1000*60*60*24) );
        return {
            'totalseconds': Math.floor(timediff/1000), //total timediff in seconds
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        };

    }

    static prettyGetTimeRemainng(endtime) {
        const timeObject = this.getTimeRemaining(endtime);
        //return timeObject.days + 'd ' + timeObject.hours + 't ' + timeObject.minutes + 'm ' + timeObject.seconds + 's';
        // formats (depending on how long until endtime)
        // 19s,   // 2m 34s    // 1t 19m    // 5d 13m

        if (timeObject.totalseconds <= 0) {
            return {
                timestring: null,
                shouldCount: false
            }
        }
        if (timeObject.totalseconds < 60) { // seconds left
            return {
                timestring: timeObject.seconds + 's',
                shouldCount: true
            }
        }
        if (timeObject.totalseconds < (60*60)) { // minutes left
            return {
                timestring: timeObject.minutes + 'm ' + timeObject.seconds + 's',
                shouldCount: true
            }
        }
        if (timeObject.totalseconds < (60*60*24)) { //hours left
            return {
                timestring: timeObject.hours + 't ' + timeObject.minutes + 'm',
                shouldCount: false
            }
        }
        else { //days left
            return {
                timestring: timeObject.days + 'd ' + timeObject.hours + 't',
                shouldCount: false
            }
        }

    }

}


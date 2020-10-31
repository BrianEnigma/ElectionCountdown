function debug(s)
{
    if (true)
        console.log(s);
}

class ApplicationInterface
{
    constructuor()
    {
        this.initialize();
    }

    initialize()
    {
        this.cache = {};
        this.loadingCallback = undefined;
        this.loading = false;
    }

    setLoadingCallback(theCallback)
    {
        this.loadingCallback = theCallback;
    }

    getCounter()
    {
        // Hack in TODAY:
        //this.cache['days'] = 0;
        //this.cache['weeks'] = 0;

        // Hack in THE PAST:
        //this.cache['days'] = -1;

        return this.cache;
    }

    isLoading()
    {
        return this.loading;
    }

    fetchCounter()
    {
        this.loading = true; // Encapsulate this in RAII?
        const url = 'https://api.electioncountdown.org/ElectionCountdown';

        debug('Loading counter from API.');
        if (this.loadingCallback != undefined)
        {
            debug('Starting loading animation.');
            this.loadingCallback(true);
        }
        let receivedData = undefined;
        let self = this;
        let jsonRequest = $.getJSON(url, {brief: 0})
            .done(function (data) {
                debug(data);
                receivedData = data;
            })
            .fail(function() {

            })
            .always(function() {

            });
        jsonRequest.always(function() {
            //debug(receivedData);
            if (receivedData['days'])
                self.cache = receivedData
            if (self.loadingCallback != undefined)
            {
                debug('Ending loading animation.');
                self.loadingCallback(false);
            }
            self.loading = false;
            debug('Loaded counter.');
        })
    }
};

let api = new ApplicationInterface();
api.initialize();
api.setLoadingCallback(setLoading);

function displayResult()
{
    const month_name = [
        '',
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    $('#counterDays').html('');
    $('#counterWeeks').html('');
    $('#counterMessage').html('');
    let counter = api.getCounter()
    debug(counter);
    if (counter['days'] !== undefined)
    {
        let label = counter['label']
        let days = Number(counter['days'])
        let weeks = Number(counter['weeks']).toFixed(1);
        let target = counter['target'];
        let target_year = Number(target.substring(0, 4));
        let target_month = Number(target.substring(5, 7));
        let target_day = Number(target.substring(8, 10));
        $('#intro').html('Countdown to the ' + label + ': ' + target_day + ' ' + month_name[target_month] + ', ' + target_year)
        if (days < 0) {
            $('#counterMessage').html('We are now past the ' + label + '.');
        } else if (days == 0)
        {
            $('#counterMessage').html('TODAY!');
        } else {
            $('#counterDays').html(days + ' day' + (days != 1 ? 's' : ''));
            $('#counterWeeks').html(weeks + ' week' + (weeks != 1 ? 's' : ''));
        }
    } else {
        $('#counterMessage').html('Error retrieving countdown.');
    }
}

function setLoading(isLoading)
{
    if (isLoading)
    {
        debug('Showing loading animation.');
        $('#loadingDiv').show();
    }
    else
    {
        debug('Hiding loading animation.');
        $('#loadingDiv').hide();
        displayResult();
    }
}

function initialize()
{
    // Nothing to do yet.
}

$(document).ready(function() {
    initialize();
    //setTimeout(initialize, 100);
    api.fetchCounter();
});

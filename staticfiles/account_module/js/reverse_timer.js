$(document).ready(function(){
    var minutes
    var seconds

    var appendSeconds = document.getElementById("seconds");
    var appendMinutes = document.getElementById("minutes");
    const saved_minutes= localStorage.getItem("minutes") || false
    const saved_seconds = localStorage.getItem("seconds") || false

    function update_counter() {
        seconds --;
        if (seconds < 0){
            minutes--;
            seconds = 59;

        }
        if (seconds > 9){
             appendSeconds.innerHTML = seconds;
        }
        if (seconds <= 9){
            appendSeconds.innerHTML = "0"+ seconds;
        }
        appendMinutes.innerHTML = minutes;
        check_timer()
    }

    function check_timer(){
        if (minutes == 0 && seconds == 0) {
            appendSeconds.innerHTML = "0" + seconds;
            appendMinutes.innerHTML = "0" + minutes;
            localStorage.setItem("minutes", "0")
            localStorage.setItem("seconds", "0")
            clearInterval(Interval)
        }
    }

    if(saved_minutes && saved_seconds){
        minutes = parseInt(saved_minutes, 10)
        seconds = parseInt(saved_seconds, 10)
    }else{
      minutes = 4;
      seconds = 1;
    }
    Interval = setInterval(update_counter, 1000);

    window.addEventListener('beforeunload', function (event){
        localStorage.setItem("minutes", minutes)
        localStorage.setItem("seconds", seconds)
    });
    window.onbeforeunload = function() {
      localStorage.removeItem('minutes');
      localStorage.removeItem('seconds');
    };
});


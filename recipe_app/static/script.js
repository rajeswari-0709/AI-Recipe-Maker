function startVoice() {

    if (!('webkitSpeechRecognition' in window)) {

        alert(
            "Speech Recognition not supported in this browser"
        );

        return;
    }

    const recognition =
        new webkitSpeechRecognition();

    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function(event) {

        const speechText =
            event.results[0][0].transcript;

        const textarea =
            document.querySelector("textarea");

        textarea.value = speechText;
    };
}
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent
var grammar = '#JSGF V1.0;';

var recognition = new SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();

speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.continuous = false;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

var input = document.querySelector('#command');
var form = document.querySelector('#voice');

function speak(){
    var button = document.getElementById('speak');
    input.value = '...'
    console.log('listening!!!');
    recognition.start();
}

recognition.onresult = function(event) {
    var text = event.results[0][0].transcript;
    console.log('text: ' + text);
    input.value = text;
    form.submit()
}

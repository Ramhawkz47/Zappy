# Zappy
Zappy is fun personal assistant and easy to deploy anywhere and do anything you ask. everything is needed to be pre-programmed. This is not an AI made from Machine Learning its just a Chatbot which does as it should be programmed.

Instructions:-

1. It requires following libraries:-
 
 a. Wheel package installer - pip install wheel
 
 b. SpeechRecognition - pip install SpeechRecognition
 
 c. python text-to-speech (pyttsx3) - pip install pyttsx3
 
 d. Pyaudio - https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio - my python is v3.8 so i used v38 - pip install PyAudio-0.2.11-cp38-cp38m-win_amd64.whl
 
 e. Microsoft Visual C++ v14 or higher - https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16 
 
 f. Cython (to precompile Python Libraries)(optional, if you need to speed it up) - pip install cython

2. Run micdecttest.py to test audio ports and note the ids (if you are using specific microphone). i'm using id 0 as it sets to the default microphone.
3. Run recotest.py for recognition of the speech to text recognition.
4. Run speechtest.py to test the text-to-speech recognition.
5. Run zappyproto.py to run both in Sync as for the recognition and sythesis of speech.
6. Finally run zappybumb.py to test the chatbot.

test.txt - consist of commands that are designated for chatbot.

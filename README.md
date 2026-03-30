**Automatic Text Generator**
##**Introduction**
**This little project shows you exactly that — in plain Python, sometimes no fancy libraries are needed. You paste in some text, it learns which words follow which, and then generates something new. Feed it a song, a story, or a Wikipedia paragraph and wathc it remix your words.
##**Features**
##Learns word patterns from any text you provide
Generates new text that tries to mimic the style of your input
##Great for understanding how AI text generation actually works
**Requirements**
Python 3.x 
**Installation**
Clone this repository and start working on it.
git clone cd text-generator
**Usage**
Paste your text, pick a starting word, and say how many words you want generated.
Paste some text here (the more the better!):
> Once upon a time there was a great wizard who lived in a great castle...

Which word should we start with? Once
How many words should I generate? 20

--- YOUR AI GENERATED TEXT ---
Once upon a time there was a great castle who lived in a wizard once upon...

**How It Works**
The program builds a simple dictionary that maps each word to a list of words that followed it in the input. When generating, it starts with your chosen word and keeps randomly picking the next one based on those learned pairs. This technique is called a “Markov Chain”.
**Limitations**
Short input text leads to repetitive or early-stopping output.
It only looks one word ahead, so the output can be a bit random at times.
There is no memory between runs ,thus every session starts fresh.
**Contributing**
Contributions are welcome and feel free to submit a pull request.
**License**
This project is free to use, modify, and share. 
**Acknowledgments**
Inspired by the simplicity of Markov Chain text generation and how much one can do with just a dictionary and a loop.
**Disclaimer**
The text this program generates is random and based purely on word patterns. It may occasionally produce sentences that don't make much sense.


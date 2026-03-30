import random

text = input("Paste some text here (the more the better!): ")

words = text.split()

brain = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    
    if current_word not in brain:
        brain[current_word] = []
    
    brain[current_word].append(next_word)

print("\nStep 2: Let's create something!")
start_word = input("Which word should we start with? ")
how_many_words = input("How many words should I generate? ")
how_many_words = int(how_many_words) 
current_word = start_word
sentence = [current_word]

for i in range(how_many_words - 1):
    if current_word in brain:
        possible_next_words = brain[current_word]
        next_word = random.choice(possible_next_words)
        
        sentence.append(next_word)
        
        current_word = next_word
    else:
        print(f"\n(Stopping early: I don't know what follows '{current_word}')")
        break

print("\n--- YOUR AI GENERATED TEXT ---")
print(" ".join(sentence))
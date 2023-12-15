import json
import random
import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
import nltk
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def augment_data(sentence):
    tokens = nltk.word_tokenize(sentence)
    augmented_sentences = [sentence]
    for token, tag in nltk.pos_tag(tokens):
        if tag.startswith('NN'):
            synsets = wordnet.synsets(token, pos=wordnet.NOUN)
            synonyms = set()
            for synset in synsets:
                for lemma in synset.lemmas():
                    synonyms.add(lemma.name())
            if synonyms:
                for synonym in synonyms:
                    new_sentence = ' '.join([synonym if word == token else word for word in tokens])
                    augmented_sentences.append(new_sentence)
    return augmented_sentences


class SpacyChatBot:
    def __init__(self, model):
        nlp = spacy.load(model)
        if not isinstance(nlp, spacy.language.Language):
            raise ValueError(f"Failed to load model: {model}")
        self.nlp = nlp
        self.model = "C:/Users/Mayra/Documents/AGI/CHATBOT/training_data/training_data.spacy"

    def respond(self, message, augmented_sentences):
        doc = self.nlp(message)
        entities = [ent.text for ent in doc.ents]
        if 'crime scene' in entities:
            return "Let's analyze the crime scene."
        elif 'hello' in entities:
            return "Hello! How can I assist you today?"
        else:
            return f"I recognized these entities in your message: {', '.join(entities)}"

def train_model(train_data, model=None, output_dir=None, n_iter=100):
    if model is not None:
        nlp = spacy.load(model)
    else:
        nlp = spacy.blank('en')

    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner, last=True)
    else:
        ner = nlp.get_pipe('ner')

    for _, annotations in train_data:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(train_data)
            batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                examples = []
                for text, annotations in batch:
                    doc = nlp.make_doc(text)
                    example = Example.from_dict(doc, annotations)
                    examples.append(example)
                nlp.update(examples, sgd=optimizer)

    if output_dir is not None:
        nlp.to_disk(output_dir)

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    train_data = []
    for paragraph in data['paragraphs']:
        for sentence in paragraph['sentences']:
            text = ' '.join([token['orth'] for token in sentence['tokens']])
            entities = []
            start_char = 0
            for token in sentence['tokens']:
                end_char = start_char + len(token['orth'])
                entities.append((start_char, end_char, token['tag']))
                start_char = end_char + 1  # +1 for the space
            annotations = {'entities': entities}
            augmented_sentences = augment_data(text)
            for augmented_sentence in augmented_sentences:
                train_data.append((augmented_sentence, annotations))
    return train_data

def main():
    train_data = load_data("C:/Users/Mayra/Documents/AGI/CHATBOT/training_data/training_data.json")
    train_model(train_data, 'en_core_web_sm', 'output', n_iter=20)
    bot = SpacyChatBot('output')
    while True:
        
        message = input("You: ")
        response = bot.respond(message, augmented_sentences=augment_data)
        print(f"Bat-Spacy: {response}")

if __name__ == "__main__":
    main()

import json
import spacy
import random
from spacy.training.example import Example

def load_training_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def train_spacy_nlu(training_data, output_model_dir, iterations=100):
    nlp = spacy.blank("en")  # Use the blank English model

    # nlp.add_pipe(your_custom_component)

    # Training loop
    for _ in range(iterations):
        random.shuffle(training_data)
        for example in training_data:
            text = example["text"]
            entities = example["entities"]

            # Ensure entities is a list of dictionaries
            if not isinstance(entities, list):
                continue

            # Convert entities to spaCy format
            annotations = {"entities": entities}

            # Create a spaCy Example
            spacy_example = Example.from_dict(nlp.make_doc(text), annotations)

            # Update the NER model
            nlp.update([spacy_example], drop=0.5)

    # Save the trained model
    nlp.to_disk(output_model_dir)

if __name__ == "__main__":
    training_data_path = "C:/Users/Mayra/Documents/AGI/CHATBOT/training_data/training_data.json"
    output_model_dir = "C:/Users/Mayra/Documents/AGI/CHATBOT/training_data/model-last"

    # Load training data
    training_data = load_training_data(training_data_path)

    # Train spaCy NLU
    train_spacy_nlu(training_data, output_model_dir)

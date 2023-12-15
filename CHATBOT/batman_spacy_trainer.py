import spacy
import random
from spacy.training.example import Example

# Load the spaCy model
nlp = spacy.blank("en")

# Your training data
train_data = [
    ({"text": "Analyze the cultural context of the crime, exploring any rituals, symbols, or traditions that may influence the investigation.", "role": "user"}, {"entities": []}),
    ({"text": "Explore alternative scenarios for the crime, considering multiple hypotheses and potential twists in the investigation.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze any potential connection between the crime and the surrounding community, considering local dynamics and relationships.", "role": "user"}, {"entities": []}),
    ({"text": "Evaluate the possibility of a copycat crime, comparing the current incident with similar cases to identify patterns or trends.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the victim's social circle, looking for potential motives or conflicts within their relationships.", "role": "user"}, {"entities": []}),
    ({"text": "Explore unconventional methods of investigation, such as using technology or techniques not commonly employed in traditional forensic procedures.", "role": "user"}, {"entities": []}),
    ({"text": "Examine the timeline of events leading up to the crime, identifying critical moments and potential triggers.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the victimology of the case, exploring patterns and characteristics of individuals targeted by the perpetrator.", "role": "user"}, {"entities": []}),
    ({"text": "Evaluate the potential impact of mental health issues on the crime, considering any connections to psychiatric conditions.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze any unusual or distinctive elements at the crime scene, focusing on details that may provide insights into the perpetrator's mindset.", "role": "user"}, {"entities": []}),
    ({"text": "Explore the use of advanced technology, such as AI-driven analytics or predictive modeling, to enhance the investigation.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the geographical aspects of the crime, exploring how the location may have influenced the dynamics of the incident.", "role": "user"}, {"entities": []}),
    ({"text": "Examine the potential involvement of external factors, such as political or social influences, in the commission of the crime.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze any potential involvement of organized crime or criminal syndicates, considering the impact on the investigation.", "role": "user"}, {"entities": []}),
    ({"text": "Explore the possibility of a motive-driven crime, analyzing the reasons behind the perpetrator's actions.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the use of any unconventional weapons or methods, exploring the uniqueness of the crime.", "role": "user"}, {"entities": []}),
    ({"text": "Evaluate the forensic implications of the crime, considering how specific evidence may contribute to solving the case.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the potential involvement of external entities, such as corporations or government agencies, in the commission of the crime.", "role": "user"}, {"entities": []}),
    ({"text": "Examine the potential influence of cultural or subcultural factors on the crime, considering unique motivations or rituals.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the impact of the media on the investigation, exploring how public perception and coverage may affect the case.", "role": "user"}, {"entities": []}),
    ({"text": "Examine the potential involvement of a serial offender, considering patterns, signatures, or similarities to other unsolved cases.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the role of technology in the commission of the crime, exploring digital evidence and potential cyber aspects.", "role": "user"}, {"entities": []}),
    ({"text": "Evaluate the potential involvement of hate crimes, exploring any indicators of prejudice or discrimination.", "role": "user"}, {"entities": []}),
    ({"text": "Analyze the potential involvement of extremist ideologies or groups in the crime, exploring radical motivations.", "role": "user"}, {"entities": []}),
]

# Update the training data format
train_data_modified = {}

# Training loop
for epoch in range(10):
    random.shuffle(train_data_modified)
    losses = []
    # Update the model with iterating over the training data
    for text, annotations in train_data_modified:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example], drop=0.5, losses=losses)
    print(losses)

# Save the trained model
nlp.to_disk("C:/Users/Mayra/Documents/AGI/CHATBOT")
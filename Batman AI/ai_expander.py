import agi
import cagi

def ai_expander(acronym):
    ai_dict = {
        "AI": "Artificial Intelligence",
        "ML": "Machine Learning",
        "DL": "Deep Learning",
        "NLP": "Natural Language Processing",
        "API": "Application Programming Interface",
        "CAGI": "Comprehensive Artificial General Intelligence"
    }

    expanded_form = ai_dict.get(acronym.upper(), f"Expansion not found for {acronym}")
    return expanded_form

class ai_Expander:
    def __init__(self, formula):
        self.formula = formula

    def expand_acronym(self, acronym):
        return self.formula(acronym)

def default_acronym_formula(acronym):
    return f"{acronym} Intelligent Assistant"

def custom_acronym_formula(acronym):
    # Define your custom formula here
    # For example, you might use a different concatenation pattern or add additional information.
    return f"Artificial {acronym} Assistant"

# Example Usage:
expander = ai_Expander(default_acronym_formula)

# Generate AI for a specific acronym
ai = expander.expand_acronym("AI")
print(ai)  # Output: "AI Intelligent Assistant"

# Example with a custom formula:
expander = ai_Expander(custom_acronym_formula)
ai = expander.expand_acronym("ML")
print('ai')  # Output: "Artificial ML Assistant"

if __name__ == "__main__":
    expander = ai_Expander(default_acronym_formula)
    ai = expander.expand_acronym("AI")
    print(ai)  # Output: "AI Intelligent Assistant"

    expander = ai_Expander(custom_acronym_formula)
    ai = expander.expand_acronym("ML")
    print(ai)
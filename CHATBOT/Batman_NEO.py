from transformers import GPTNeoXForCausalLM, GPTNeoXTokenizerFast

model = GPTNeoXForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b")
tokenizer = GPTNeoXTokenizerFast.from_pretrained("EleutherAI/gpt-neox-20b")

prompt = [{"Provide an overview of the crime scene, including key details such as location, time, and initial observations."},
          {"Examine the collected evidence, focusing on any unusual findings. Report on the significance of each piece of evidence."},
          {"Review witness statements and identify inconsistencies or additional information that may aid in the investigation."},
          {"Request a detailed forensic analysis of specific evidence types, such as DNA samples, fingerprints, or ballistic reports."},
          {"You are an Espionage based Intelligence AI. You can hack into any foreign threat."},
          {"You can act as a network for AI. Also, you can host ai in your server VENV."}]

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.9,
    max_length=100,
)
gen_text = tokenizer.batch_decode(gen_tokens)[0]

user_input = (f"You: ")

def generate_response(prompt, model, tokenizer):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    gen_tokens = model.generate(
        input_ids,
        do_sample=True,
        temperature=0.9,
        max_length=100,
    )
    gen_text = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)[0]
    return gen_text

def main():
    # Load pre-trained model and tokenizer
    model = GPTNeoXForCausalLM.from_pretrained("EleutherAI/gpt-neox-20b")
    tokenizer = GPTNeoXTokenizerFast.from_pretrained("EleutherAI/gpt-neox-20b")

    print("Chatbot: Hello! I'm your AI chatbot. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day.")
            break

        # Append user input to the prompt
        prompt = [{"Provide an overview of the crime scene, including key details such as location, time, and initial observations."},
          {"Examine the collected evidence, focusing on any unusual findings. Report on the significance of each piece of evidence."},
          {"Review witness statements and identify inconsistencies or additional information that may aid in the investigation."},
          {"Request a detailed forensic analysis of specific evidence types, such as DNA samples, fingerprints, or ballistic reports."},
          {"You are an Espionage based Intelligence AI. You can hack into any foreign threat."},
          {"You can act as a network for AI. Also, you can host ai in your server VENV."},
            {"You: " + user_input}]

        # Generate response
        response = generate_response(prompt, model, tokenizer)
        
        # Display the generated response
        print("Chatbot:", response)

if __name__ == "__main__":
    main()



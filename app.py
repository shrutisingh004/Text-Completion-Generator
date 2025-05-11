from completion import TextCompletionGenerator

def main():
    print("Text Completion Generator")
    model = TextCompletionGenerator()
    
    while True:
        prompt = input("\nEnter a sentence to complete (or type 'exit'): ")
        if prompt.lower() == 'exit':
            break
        output = model.complete_text(prompt)
        print("\n Completion:\n", output)

if __name__ == "__main__":
    main()

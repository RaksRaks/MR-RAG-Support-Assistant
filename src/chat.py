from rag import ask

def main():
    print("="*60)
    print("                           FNB Chat Assistant")
    print("="*60)
    while(True):
        question = input("You: ").strip()
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        if not question:
            continue
        answer, sources = ask(question)
        print(f"\nQ: {question}")
        print(f"A: {answer}")
        print(f"Sources: {sources}\n")


if __name__== "__main__":
    main()
import csv
from rag import ask

QUESTION_FILE = "corpus/test_questions.csv"
OUTPUT_FILE = "results_log.csv"

def run_tests():
    with open(QUESTION_FILE,encoding='utf-8')as f:
        with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as out:
            writer = csv.writer(out)
            writer.writerow(['question_id', "question", "answer", "sources_cited", "expected_source"])
            reader = csv.DictReader(f, delimiter = ';')
            for row in reader:
                question_id = row['question_id']
                question = row['question']
                expected = row['expected_source_doc']

                print(f"\n {question_id}: {question}")

                answer, sources = ask(question)
                print(f"Answer: {answer[:200]}")
                print(f"Sources cited: {sources}")
                print(f"Expected source: {expected}")

                writer.writerow([question_id, question, answer, sources, expected])


if __name__ == "__main__":
    run_tests()
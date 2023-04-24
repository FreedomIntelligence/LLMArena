from typing import Any, Dict, List
import json
from retrying import retry


class Competitor:
    name: str
    answers: List[Dict[str, Any]]

    def __init__(self, name: str) -> None:
        """
        Initializes a Competitor object with a name and an empty list of answers.
        """
        self.name = name
        self.answers = []

    @retry(wait_fixed=10000, stop_max_attempt_number=3)
    def answer_question(self, question: str) -> Any:
        """
        This method is used to answer a single question. It uses the @retry decorator to retry the function in case of any exceptions.
        This method needs to be implemented by a subclass.
        """
        raise NotImplementedError("answer_question() must be implemented by a subclass")

    def answer_questions(self, questions: List[str]) -> None:
        """
        Answers a list of questions and saves the answers to a JSONL file.
        """
        for question in questions:
            answer = self.answer_question(question)
            self.answers.append({'id': len(self.answers), 'question': question, 'answer': answer})
        self.save_results()

    def save_results(self) -> None:
        """
        Saves the competitor's answers to a JSONL file.
        """
        with open(f"{self.name}.jsonl", mode='w', encoding='utf-8') as writer:
            for item in self.answers:
                writer.write(json.dumps(item, ensure_ascii=False) + "\n")

import json
from typing import List, Dict, Any

from Competitor import Competitor
from Referee import Referee


class Arena:
    competitor1: Competitor
    competitor2: Competitor
    referee: Referee
    question_file: str
    questions: List[str]
    results: Dict[str, Any]

    def __init__(self, competitor1: Competitor, competitor2: Competitor, referee: Referee, question_file: str) -> None:
        """
        Initializes an Arena object with two competitors, a referee, and a question file.
        """
        self.competitor1 = competitor1
        self.competitor2 = competitor2
        self.referee = referee
        self.question_file = question_file
        self.questions = self.read_questions()
        self.results = {}

    def read_questions(self) -> List[str]:
        """
        Reads a list of questions from a JSONL file.
        """
        questions = []
        with open(self.question_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                item = json.loads(line)
            questions.append(item.get("instruction"))
        return questions

    def do_battle(self) -> None:
        """
        Conducts a competition between the two competitors and prints the final results.
        """
        self.competitor1.answer_questions(self.questions)
        self.competitor2.answer_questions(self.questions)
        self.referee.read_samples()
        self.referee.eval("all")
        self.referee.print_final_result()

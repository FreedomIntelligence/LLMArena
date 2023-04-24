import json
from statistics import mean
from typing import List, Dict, Any, Optional

from Competitor import Competitor


class Referee:
    final_result: Dict[str, Dict[str, List[Any]]]
    name: str
    competitor1: Competitor
    competitor2: Competitor

    def __init__(self, name: str = "", competitor1: Optional[Competitor] = None,
                 competitor2: Optional[Competitor] = None) -> None:
        """
        Initializes a Referee object with a name and two competitor objects.
        """
        self.name = name
        self.competitor1 = competitor1
        self.competitor2 = competitor2
        self.final_result = {
            "sample_list": {
                self.competitor1.name: [],
                self.competitor2.name: []
            },
            "score": {
                self.competitor1.name: [],
                self.competitor2.name: []
            },
            "better": {
                self.competitor1.name: [],
                self.competitor2.name: []
            }
        }

    def read_sample(self, competitor: Competitor) -> None:
        """
        Reads a competitor's sample data from a JSONL file and stores it in the final_result dictionary.
        """
        with open(f"{competitor.name}.jsonl", encoding='utf-8', mode='r') as reader:
            self.final_result["sample_list"][competitor.name] = json.load(reader)

    def read_samples(self) -> None:
        """
        Reads sample data for both competitors.
        """
        self.read_sample(self.competitor1)
        self.read_sample(self.competitor2)

    def eval(self, eval_class: str = "score") -> None:
        """
        Evaluates the competitors based on the evaluation class specified.
        """
        for result1, result2 in zip(self.final_result["sample_list"][self.competitor1.name],
                                    self.final_result["sample_list"][self.competitor2.name]):
            if eval_class == "score":
                self.eval_score(result1["answer"], result2["answer"], question=result1["question"])
            elif eval_class == "better":
                self.eval_better(result1["answer"], result2["answer"], question=result1["question"])
            else:
                self.eval_score(result1["answer"], result2["answer"], question=result1["question"])
                self.eval_better(result1["answer"], result2["answer"], question=result1["question"])

    def print_final_result(self, filename: str) -> None:
        """
        Prints the final result of the competition and saves it to a file.
        """
        with open(filename, 'w') as f:
            f.write(f"Results for {self.competitor1.name} vs. {self.competitor2.name}\n")
            f.write(
                f"Score: {mean(self.final_result['score'][self.competitor1.name])} vs. {mean(self.final_result['score'][self.competitor2.name])}\n")
            f.write(
                f"Winner: {mean(self.final_result['better'][self.competitor1.name])} vs. {mean(self.final_result['better'][self.competitor2.name])}\n")
            print(f"Results for {self.competitor1.name} vs. {self.competitor2.name}")
            print(
                f"Score: {mean(self.final_result['score'][self.competitor1.name])} vs. {mean(self.final_result['score'][self.competitor2.name])}")
            print(
                f"Winner: {mean(self.final_result['better'][self.competitor1.name])} vs. {mean(self.final_result['better'][self.competitor2.name])}")
        print("Results saved to file:", filename)

    def eval_score(self, answer1: Any, answer2: Any, question: Optional[str] = None) -> None:
        """
        Evaluates the competitors' scores based on their answers and stores the result in the final_result dictionary.
        This method needs to be implemented by a subclass.
        """
        raise NotImplementedError("eval_score() must be implemented by a subclass")

    def eval_better(self, answer1: Any, answer2: Any, question: Optional[str] = None) -> None:
        """
        Evaluates which competitor's answer is better based on the evaluation criteria and stores the result in the final_result dictionary.
        This method needs to be implemented by a subclass.
        """
        raise NotImplementedError("eval_better() must be implemented by a subclass")

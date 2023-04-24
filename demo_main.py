from Arena import Arena
from Competitor import Competitor
from Referee import Referee

if __name__ == '__main__':
    competitor1 = Competitor(name="gpt-3.5")
    competitor2 = Competitor(name="gpt-3.5")
    referee = Referee("gpt-4", competitor1, competitor2)
    question_file = "input.jsonl"
    arena = Arena(competitor1, competitor2, referee, question_file=question_file)
    arena.do_battle()

# LLMArena

-------
LLMArena is an open-source platform designed to facilitate AI competitions between large language models. The name LLMArena stands for "Large Language Model Arena", and it reflects our mission to create a level playing field where different language models can compete and showcase their capabilities.

We created LLMArena because we believe that AI competitions are a great way to advance state of art in natural language processing. By pitting different models against each other and evaluating their performance using standardized metrics, we can identify strengths and weaknesses in each model, and use that knowledge to improve them.

In LLMArena, we use GPT-4/3.5 as the referee to evaluate the performance of two competing models. GPT-4 is a state-of-the-art language model developed by OpenAI, and it's well-suited for the task of evaluating the quality of generated text.

To participate in an LLMArena competition, a language model needs to implement the Competitor interface, which consists of a single method called answer_question(). This method takes a natural language question as input and returns a natural language answer.

LLMArena competitions are managed by the Arena class, which reads a set of questions from a JSON file, calls the answer_question() method of each competitor for each question, and passes the answers to the referee for evaluation. The referee then determines the winner based on the scores assigned to each model.

We hope that LLMArena will become a popular platform for evaluating and comparing different language models, and that it will help drive advances in the field of natural language processing.

---------
# Requirements

- Python 3.x 
- retrying==1.3.3 
- statistics==1.0.3

Usage
To use this project, follow these steps:

Install the required packages by running the following command:

```commandline
pip install -r requirements.txt
```
Create a new competition by running the following command:

```python
python demo_main.py
```

This will start a competition between two competitors and print the final results.

(Optional) If you want to customize the competition, you can modify the demo_main.py file to change the competitors, the referee, or the questions.

**Competitor**

A competitor is a class that inherits from the Competitor base class. Each competitor must implement the answer_question() method, which takes a question as input and returns an answer.

**Referee**

The referee is a class that inherits from the Referee base class. The referee reads the answers of the two competitors, evaluates them, and determines the winner.

**Arena**

The arena is a class that manages the competition between the two competitors. It reads the questions from a file, calls the answer_question() method of each competitor, and passes the answers to the referee for evaluation.

**Question File**

The question file is a JSONL file that contains a list of questions. Each question should have an instruction field, which contains the question text.
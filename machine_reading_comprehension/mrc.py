import time
import tensorflow as tf
from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    TFAutoModelForQuestionAnswering
)


class Question_Aswering_model:
    def __init__(self) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(
            "ancs21/xlm-roberta-large-vi-qa"
            )
        self.model = TFAutoModelForQuestionAnswering.from_pretrained(
            "ancs21/xlm-roberta-large-vi-qa",
            from_pt=True
            )
        self.embebder = None

    def predict(self, context, question):
        start = time.time()
        inputs = self.tokenizer([context], [question], return_tensors="np", truncation=True)
        outputs = self.model(inputs)

        start_position = int(tf.argmax(outputs.start_logits, axis=1))
        end_position = int(tf.argmax(outputs.end_logits, axis=1))

        answer = inputs[
            "input_ids"][
            0, start_position: end_position + 1
            ]

        return start_position, end_position, self.tokenizer.decode(answer), time.time()-start

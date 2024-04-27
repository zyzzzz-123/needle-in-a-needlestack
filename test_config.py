from llm_client import GPT3_5, EVAL_ANTHROPIC_HAIKU, EVAL_GPT3_5, \
    EVAL_ANTHROPIC_SONNET, EVAL_MISTRAL_8X22B, MISTRAL_7B, MIXTRAL_8X7B, EVAL_GPT4, MISTRAL_8X22B


EVALUATOR_MODEL_LIST = [EVAL_ANTHROPIC_HAIKU, EVAL_GPT3_5, EVAL_GPT3_5, EVAL_MISTRAL_8X22B, EVAL_GPT4]
TEST_MODEL_LIST = [GPT3_5]


class TestConfig:
    def __init__(self, prompt_file_name, model_list, test_thread_count, evaluator_model_list, number_of_questions_per_cycle,
                 cycles, location_count, result_directory, write_prompt_text_to_file):
        self.prompt_file_name = prompt_file_name
        self.model_list = model_list
        self.test_thread_count = test_thread_count
        self.evaluator_model_list = evaluator_model_list
        self.number_of_questions_per_cycle = number_of_questions_per_cycle
        self.cycles = cycles
        self.location_count = location_count
        self.result_directory = result_directory
        self.write_prompt_text_to_file = write_prompt_text_to_file


DEFAULT_TEST_CONFIG = TestConfig("test_prompt", TEST_MODEL_LIST, 100, EVALUATOR_MODEL_LIST,
                                 10,10,
                                 10, "tests", True)
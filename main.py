from utils import *
user_satisify_prob=False

while user_satisify_prob:
    problem = chat_user_problem()
    get_chat_response()
    user_satisify_prob=True


user_satisify_rq=False

while user_satisify_rq:
    problem = chat_user_problem()
    get_chat_response()
    user_satisify_rq=True

lite=llmlit()


user_satisify_method=False

while user_satisify_rq:
    problem = propose_method()
    get_chat_response()
    user_satisify_method=True

user_satisify_exp=False

while user_satisify_exp:
    problem = design_exp()
    get_chat_response()
    user_satisify_method=True

result=anticipate_result()

writing_code()

summary()
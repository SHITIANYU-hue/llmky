
from openai import OpenAI



def get_chat_response(messages):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response

def chat_user_problem(input):
    ## 这里主要参考：https://mystylus.ai/onboarding
    ## 模仿 get_chat_reponse
    prompt=f'based on user {input}, summerize the research problem, and formulate the research questions'
    return None ## 确定研究问题

def llmlit(input):
    ## 输入可以是上传文档，也可以去谷歌进行爬虫搜索相近的参考文献
    ## 主要参考litllm这个repo
    prompt='based on the research problem xx search for related liteature'
    prompt='generate the literature review for this research problem'

    return None ## 输出literature review的结果，进行归纳总结

def propose_method(input):
    ## 这里涉及到多轮用户交流，先去询问用户意图，然后去看用户是否满意如果满意了，则为最终的research method
    prompt='based on the research problem and related literature, provide several potential method for this research'
    return None  


def design_exp(input):
    ## 这里可能先对之前生成的literature review，proposed method进行归纳总结
    prompt='based on the research problem and related literature and the potential method for this research, design experiment:'
    return None  

def anticipate_result(input):
    ## 这里可能先对之前生成的literature review，proposed method进行归纳总结
    prompt='based on the proposed experiment design, genrate the anticipated results and conclusion'
    return None  

def writing_code(input):
    ## 这里如果实际去写code比较困难，目前还是个难点，有一个比较好的可以参考这个https://arxiv.org/pdf/2401.07339（但是没有开源）
    return None

def summary(input):
    # 这里应该是整合前面的信息进行文章撰写

    return None
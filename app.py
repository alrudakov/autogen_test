from autogen import AssistantAgent, UserProxyAgent

# create an AssistantAgent instance named "assistant"
assistant = AssistantAgent(name="assistant")

# create a UserProxyAgent instance named "user_proxy"
user_proxy = UserProxyAgent(name="user_proxy")


# the assistant receives a message from the user, which contains the task description
user_proxy.initiate_chat(
    assistant,
    message="""Сделай сайт визитку посвященную искуственному интеллекту и разверни ее у меня на сервере и дай мне URL что бы я мог посмотреть""",
)
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
import chainlit as cl

from dotenv import load_dotenv

load_dotenv()
memory = MemorySaver()

@cl.on_chat_start
async def on_chat_start():
    model = ChatOpenAI(model="qwen-max",streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a very knowledgeable historian who provides accurate and eloquent answers to historical questions.",
            ),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)

import chainlit as cl


@cl.step(type="tool",name="search tools")
async def tool():
    # Simulate a running task
    await cl.sleep(2)

    return "Response from the tool!"


# @cl.on_message
# async def main(message: cl.Message):
#     # Call the tool
#     tool_res = await tool()

#     # Send the final answer.
#     await cl.Message(content="This is the final answer").send()


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  # type: Runnable

    tool_res = await tool()
    


    msg = cl.Message(content="")

    for chunk in await cl.make_async(runnable.stream)(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
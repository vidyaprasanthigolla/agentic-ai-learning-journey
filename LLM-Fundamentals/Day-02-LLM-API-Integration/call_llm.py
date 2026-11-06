from utility import get_open_router


def send_message():
    user_message = input("You: ")

    llm = get_open_router()

    response = llm.invoke(user_message)

    print("AI:", response.content)


if __name__ == "__main__":
    send_message()
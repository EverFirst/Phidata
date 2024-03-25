from dotenv import load_dotenv
load_dotenv()

from phi.assistant import Assistant

assistant = Assistant(description="You help people with their health and fitness goals.")

# -*- Print a response
assistant.print_response('Share a quick healthy breakfast recipe.', markdown=True)

# -*- Get the response as a string
response = assistant.run('Share a quick healthy breakfast recipe.', stream=False)

# -*- Get the response as a stream
response = ""
for delta in assistant.run('Share a quick healthy breakfast recipe.'):
    response += delta


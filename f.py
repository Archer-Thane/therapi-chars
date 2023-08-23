import asyncio
from PyCharacterAI import Client

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9.eyJpc3MiOiJodHRwczovL2NoYXJhY3Rlci1haS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDYxMjczNTQxNzAxNDA4MzA4MzQiLCJhdWQiOlsiaHR0cHM6Ly9hdXRoMC5jaGFyYWN0ZXIuYWkvIiwiaHR0cHM6Ly9jaGFyYWN0ZXItYWkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5MTMxODYwNiwiZXhwIjoxNjkzOTEwNjA2LCJhenAiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.fcqt-TGUKYGjMwxyxGcQ3PutM2PD3pBr6DCxXS3iryFizCIDqyuvLsx9cCXfdYFl64b5_6IGZD93i3xXTEw8UZvvxVWnVoO4p3VZ6oG-tGgH7kU3oQrVrpeLrpNA40BYlaR0LjFqelX9DvUrODht7UHugquwQ1sXY0N10cc-0RGpLoTqoLDS0ck8WKhe7nRUc3BzMccawcUZnH5HyLTDCoUP-nUHujenB0PSzB_Ikcb_McRwbW9jq31DulbquB0tuRYeuwFMG5wWw_aZyMnBSZMRt1Yh1x9c2fZpmv7pccpQwn00EIP_avQYSHVI6ibmVluMa1Efi6-bJW92U4txGA"


async def main():
    client = Client()
    await client.authenticate_with_token(token)

    username = (await client.fetch_user())['user']['username']
    print(f'Authenticated as {username}')

    character_id = "43tXvCZrGfShUCd2OlA4rxkyaqTPAncy0YMZwoZ0jPg"  # Lily (by @landon)
    chat = await client.create_or_continue_chat(character_id)

    while True:
        message = input(f'{username}: ')  # In: Hi!

        answer = await chat.send_message(message)
        print(f"Character: {answer.text}")  # Out: hello there! what kind of question you gonna ask me ? i'm here to assist you :)


asyncio.run(main())
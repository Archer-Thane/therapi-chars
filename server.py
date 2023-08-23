from flask import Flask, request, jsonify
import asyncio
from PyCharacterAI import Client

token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkVqYmxXUlVCWERJX0dDOTJCa2N1YyJ9.eyJpc3MiOiJodHRwczovL2NoYXJhY3Rlci1haS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDYxMjczNTQxNzAxNDA4MzA4MzQiLCJhdWQiOlsiaHR0cHM6Ly9hdXRoMC5jaGFyYWN0ZXIuYWkvIiwiaHR0cHM6Ly9jaGFyYWN0ZXItYWkudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY5MTMxODYwNiwiZXhwIjoxNjkzOTEwNjA2LCJhenAiOiJkeUQzZ0UyODFNcWdJU0c3RnVJWFloTDJXRWtucVp6diIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.fcqt-TGUKYGjMwxyxGcQ3PutM2PD3pBr6DCxXS3iryFizCIDqyuvLsx9cCXfdYFl64b5_6IGZD93i3xXTEw8UZvvxVWnVoO4p3VZ6oG-tGgH7kU3oQrVrpeLrpNA40BYlaR0LjFqelX9DvUrODht7UHugquwQ1sXY0N10cc-0RGpLoTqoLDS0ck8WKhe7nRUc3BzMccawcUZnH5HyLTDCoUP-nUHujenB0PSzB_Ikcb_McRwbW9jq31DulbquB0tuRYeuwFMG5wWw_aZyMnBSZMRt1Yh1x9c2fZpmv7pccpQwn00EIP_avQYSHVI6ibmVluMa1Efi6-bJW92U4txGA"

app = Flask(__name__)

client = Client()
loop = asyncio.get_event_loop()
loop.run_until_complete(client.authenticate_with_token(token))
username = loop.run_until_complete(client.fetch_user())['user']['username']

@app.route('/chat/<character_id>', methods=['POST'])
def chat_endpoint(character_id):
    chat = loop.run_until_complete(client.create_or_continue_chat(character_id))

    message = request.json.get('message')
    print(message)
    if not message:
        return jsonify({"error": "Message is required!"}), 400

    answer = loop.run_until_complete(chat.send_message(message))
    return jsonify({"response": answer.text})

if __name__ == "__main__":
    app.run(debug=True)

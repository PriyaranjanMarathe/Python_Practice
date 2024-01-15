import os
from claude_api import Client

cookie = os.environ.get('__cf_bm=6FfWmOPNhu.WVt0tfgquabtGL1mJI80NamwMRKS_PLw-1694363733-0-Aalw+nRVyZAJme+OBfSqt5wk97o/SIoyf+gu7B+/xJSddKm7NulWQwLIMqJXZzau0NedRtBuzoBoE2ViWU/QO44=; cf_clearance=EpfvSo13iAPifNc.IlEi7btd8xVXcAzv3sfWhjYdFSU-1694363734-0-1-7d883cc9.84f2ddd.2a896329-0.2.1694363734; sessionKey=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; intercom-device-id-lupk8zyo=46cbe675-d30b-4841-a016-66f53339f953; intercom-session-lupk8zyo=SytjdldFWGYxZlB3ZXpNcW1TZTFmWlIxT1BhbUNYWkVvd3NPSXAwK2hvOTdJdUc0OHhyNHVGMUVteTB3SXpZZS0tK3ozSzA4Yk1lb0t3OXNsL2VDcnVaQT09--d179fc919303f098862da28cc3d8bebae223ac88')
claude_api = Client(cookie)

conversations = claude_api.list_all_conversations()
for conversation in conversations:
    conversation_id = conversation['uuid']
    print(conversation_id)

prompt = "Hello, Claude!"
conversation_id = "<conversation_id>" or claude_api.create_new_chat()['uuid']
response = claude_api.send_message(prompt, conversation_id)
print(response)

# prompt = "Hey,Summarize me this document.!"
# conversation_id = "<conversation_id>" or claude_api.create_new_chat()['uuid']
# response = claude_api.send_message(prompt, conversation_id,attachment="path/to/file.pdf",timeout=600)
# print(response)

# conversation_id = "<conversation_id>"
# deleted = claude_api.delete_conversation(conversation_id)
# if deleted:
#     print("Conversation deleted successfully")
# else:
#     print("Failed to delete conversation")

# conversation_id = "<conversation_id>"
# history = claude_api.chat_conversation_history(conversation_id)
# print(history)

# new_chat = claude_api.create_new_chat()
# conversation_id = new_chat['uuid']
# print(conversation_id)

# reset = claude_api.reset_all()
# if reset:
#     print("All conversations reset successfully")
# else:
#     print("Failed to reset conversations")

# conversation_id = "<conversation_id>"
# title = "New Chat Title"
# renamed = claude_api.rename_chat(title, conversation_id)
# if renamed:
#     print("Chat conversation renamed successfully")
# else:
#     print("Failed to rename chat conversation")
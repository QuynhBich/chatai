import openai
import argparse
import os
import uvicorn
from fastapi import FastAPI, Path, Body
from fastapi.responses import JSONResponse
from starlette.responses import StreamingResponse

from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()
@app.post("/chat/{conversation_id}")
def chatbot(
    conversation_id: str = Path(..., title="Conversation ID"),
    question: str = Body(None, media_type="application/json", embed=True),
    expanded: bool = Body(False, media_type="application/json", embed=True),
):
    async def event_stream():
        yield "data: truong bich quynh"  # Your text data

    return StreamingResponse(event_stream(), media_type="text/event-stream")

def main():
    print("Starting GPT")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "prompt", nargs="+", type=str, help="Prompt for GPT-3 to complete"
    )
    args = parser.parse_args()
    prompt = " ".join(args.prompt)
    answer = ask_gpt(prompt)
    print(answer)

def ask_gpt(prompt: str):
    openai.api_key = openai_api_key
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "can u help me summarize content of this link: https://platform.openai.com/docs/guides/text-generation"}
    ]
    )

    content = response.choices[0].message.content
    return content

# port = int(os.environ.get("PORT", 8000))
if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=port)
    main()
from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/random-word")
async def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?length=3")
        words = response.json()
        return {"word": words[0].upper()}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

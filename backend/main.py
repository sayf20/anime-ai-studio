from fastapi import FastAPI, Form
from script_generator import generate_script

app = FastAPI()

@app.post("/generate_script/")
async def script_endpoint(prompt: str = Form(...)):
    script = generate_script(prompt)
    return {"script": script}

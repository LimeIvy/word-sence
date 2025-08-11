from fastapi import FastAPI, Request
from pydantic import BaseModel
from gensim.models import KeyedVectors

app = FastAPI()

# モデルはグローバルで一度だけロード
model = KeyedVectors.load_word2vec_format("./wiki_nouns_only.model", binary=True)

class AnalyzeRequest(BaseModel):
    positive: list[str] = []
    negative: list[str] = []

class SimilarityRequest(BaseModel):
    word1: str
    word2: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    try:
        result = model.most_similar(
            positive=req.positive, negative=req.negative, topn=1
        )
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.post("/similarity")
async def similarity(req: SimilarityRequest):
    try:
        result = model.similarity(req.word1, req.word2)
        return {"result": float(result)}
    except Exception as e:
        return {"error": str(e)}

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from machine_reading_comprehension import mrc
from document_retrieval.bm25 import BM25Gensim
from document_retrieval.loader import Document_Loader
import constant

origins = [
    "http://localhost:3000",
    "http://localhost:8001",
]

DOC_LIST = constant.DOCUMENT_LIST
PATH = [doc['Passage_path'] for doc in DOC_LIST]
OUT_PATH = "./document_retrieval/index"
K = 5

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = mrc.Question_Aswering_model()
document_loader = Document_Loader(PATH)
retriever = BM25Gensim()
retriever.load_model(OUT_PATH)


class Request_Item(BaseModel):
    context: str
    question: str


class Response_Item(BaseModel):
    start_position: int
    end_position: int
    text: str
    execution_time: float
    context: str
    question: str

@app.post("/api/v1/qa")
def answer_qa(Request: Request_Item):
    context = Request.context
    question = Request.question

    if context == "":
        retrieve_result = retriever.get_top_result(question, K)
        context = document_loader.get_context()[retrieve_result[0]]

    start_position, end_position, answer, execution_time = model.predict(
        context, question
    )

    return Response_Item(
        start_position=start_position,
        end_position=end_position,
        text=answer if answer != "<s>" else "",
        execution_time=round(execution_time, 4),
        context=context,
        question=question
    )


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=8002)

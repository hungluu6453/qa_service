import uvicorn
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from machine_reading_comprehension import mrc
from document_retrieval.bm25 import BM25Gensim
from document_retrieval.loader import Document_Loader
import constant

origins = [
    # "http://localhost:3000",
    "http://localhost:8001",
]


K = 3

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

document_loader_list = list()
retriever_list = list()

for index, docs in enumerate(constant.DOC_LIST):
    passage_path = [doc['Passage_path'] for doc in docs]
    index_offset = [doc['Index_offset'] for doc in docs]
    out_path = constant.OUT_PATH[index]
    
    document_loader_list.append(Document_Loader(passage_path, index_offset))
    retriever_list.append(BM25Gensim())
    retriever_list[index].load_model(out_path)

model = mrc.Question_Aswering_model()


class Request_Item(BaseModel):
    role: str # phd master udergraduate
    question: str


class Response_Item(BaseModel):
    start_position: int
    end_position: int
    text: str
    execution_time: float
    context: str
    question: str
    paragraph_id: int


@app.post("/api/v1/retrieve")
def retrieve(Request: Request_Item):
    print(Request)
    role = Request.role
    question = Request.question

    retriever = retriever_list[constant.ROLE_MAP[role]]
    document_loader = document_loader_list[constant.ROLE_MAP[role]]

    retrieve_result = retriever.get_top_result(question, K)
    context = document_loader.get_context()[retrieve_result[0][0]]
    paragraph_id = document_loader.get_id()[retrieve_result[0][0]]

    start_position, end_position, answer, execution_time = model.predict(
        context, question
    )

    answer = answer.replace('<s>', '')
    answer = answer.remove('</s>', '')

    logging.info('Question: %s, Role: %s', question, role)
    logging.info('Answer: %s, Execution time: %s', answer, execution_time)
    logging.info('Context: %s', context)

    return Response_Item(
        start_position=start_position,
        end_position=end_position,
        text=answer,
        execution_time=round(execution_time, 4),
        context=context,
        question=question,
        paragraph_id=paragraph_id
    )


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=8004)

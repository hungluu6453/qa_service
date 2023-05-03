import os
import constant
from document_retrieval.bm25 import BM25Gensim
from document_retrieval.loader import Document_Loader

def preprocess(text):
    text = text.replace('\n', ' ')
    return text

DOCUMENT_LIST_TIENSI = [
    constant.QUY_CHE_DAO_TAO_TIEN_SI,
    constant.QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    constant.QUY_DINH_VE_DAO_TAO_HOC_VU,
    constant.QUY_DINH_GIANG_DAY
]

DOCUMENT_LIST_THACSI = [
    constant.QUY_DINH_TO_CHUC_DAO_TAO_TRINH_DO_THAC_SI,
    constant.QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    constant.QUY_DINH_VE_DAO_TAO_HOC_VU,
    constant.QUY_DINH_GIANG_DAY
]

DOCUMENT_LIST_SINHVIEN = [
    constant.QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    constant.QUY_DINH_VE_DAO_TAO_HOC_VU,
    constant.QUY_DINH_GIANG_DAY
]
DOC_LIST = [DOCUMENT_LIST_TIENSI, DOCUMENT_LIST_THACSI, DOCUMENT_LIST_SINHVIEN]
OUT_PATH = ["./document_retrieval/index/phd", "./document_retrieval/index/master", "./document_retrieval/index/undergraduate"]

                    

passage_path = [doc['Passage_path'] for doc in DOCUMENT_LIST_TIENSI]
index_offset = [doc['Index_offset'] for doc in DOCUMENT_LIST_TIENSI]
out_path = OUT_PATH[0]

document_loader = Document_Loader(passage_path, index_offset)
data = document_loader.get_context()
data = list(map(preprocess, data))

retriever = BM25Gensim(data)
retriever.create_model(out_path)


passage_path = [doc['Passage_path'] for doc in DOCUMENT_LIST_THACSI]
index_offset = [doc['Index_offset'] for doc in DOCUMENT_LIST_THACSI]
out_path = OUT_PATH[1]

document_loader = Document_Loader(passage_path, index_offset)
data = document_loader.get_context()
data = list(map(preprocess, data))

retriever = BM25Gensim(data)
retriever.create_model(out_path)


passage_path = [doc['Passage_path'] for doc in DOCUMENT_LIST_SINHVIEN]
index_offset = [doc['Index_offset'] for doc in DOCUMENT_LIST_SINHVIEN]
out_path = OUT_PATH[2]

document_loader = Document_Loader(passage_path, index_offset)
data = document_loader.get_context()
data = list(map(preprocess, data))

retriever = BM25Gensim(data)
retriever.create_model(out_path)


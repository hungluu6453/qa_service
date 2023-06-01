
QUY_DINH_TO_CHUC_DAO_TAO_TRINH_DO_THAC_SI = {
    'Passage_path': 'document_retrieval/data/Quy dinh to chuc dao tao trinh do thac si/',  # nopep8
    'Index_offset': 101
}

QUY_CHE_DAO_TAO_TIEN_SI = {
    'Passage_path': 'document_retrieval/data/Quy che dao tao tien si/',
    'Index_offset': 1
}

QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO = {
    'Passage_path': 'document_retrieval/data/Quy dinh cau truc CTDT 2021/',
    'Index_offset': 53 
}

QUY_DINH_VE_DAO_TAO_HOC_VU = {
    'Passage_path': 'document_retrieval/data/Quy dinh ve dao tao hoc vu/',
    'Index_offset': 154
}

QUY_DINH_GIANG_DAY = {
    'Passage_path': 'document_retrieval/data/Quy dinh giang day/',
    'Index_offset': 71
}

DOCUMENT_LIST = [
    QUY_DINH_TO_CHUC_DAO_TAO_TRINH_DO_THAC_SI,
    QUY_CHE_DAO_TAO_TIEN_SI,
    QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    QUY_DINH_VE_DAO_TAO_HOC_VU,
    QUY_DINH_GIANG_DAY
]  

DOCUMENT_LIST_TIENSI = [
    QUY_CHE_DAO_TAO_TIEN_SI,
    QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    QUY_DINH_VE_DAO_TAO_HOC_VU,
    QUY_DINH_GIANG_DAY
]

DOCUMENT_LIST_THACSI = [
    QUY_DINH_TO_CHUC_DAO_TAO_TRINH_DO_THAC_SI,
    QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    QUY_DINH_VE_DAO_TAO_HOC_VU,
    QUY_DINH_GIANG_DAY
]

DOCUMENT_LIST_SINHVIEN = [
    QUY_DINH_VE_CAU_TRUC_CHUONG_TRINH_DAO_TAO,
    QUY_DINH_VE_DAO_TAO_HOC_VU,
    QUY_DINH_GIANG_DAY
]

DOC_LIST = [DOCUMENT_LIST_TIENSI, DOCUMENT_LIST_THACSI, DOCUMENT_LIST_SINHVIEN]
OUT_PATH = ["./document_retrieval/index/phd", "./document_retrieval/index/master", "./document_retrieval/index/undergraduate"]
OUT_PATH = ["./document_retrieval/index_v2/phd", "./document_retrieval/index_v2/master", "./document_retrieval/index_v2/undergraduate"]

ROLE_MAP ={
    'phd': 0,
    'master': 1,
    'undergraduate': 2,
}
import constant
from pprint import pprint

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
PATH = [doc['Passage_path'] for doc in DOCUMENT_LIST_TIENSI]
index_offset = [doc['Index_offset'] for doc in DOCUMENT_LIST_TIENSI]

questions = [
"Phạm vi điều chỉnh và đối tượng áp dụng ",
"Mục tiêu đào tạo",
"Nghiên cứu sinh và người hướng dẫn",
"Chế độ học tập và nghiên cứu của nghiên cứu sinh",
"Đăng ký học tập và nghiên cứu",
"Quản lý nghiên cứu sinh",
"Thu chi trong đào tạo tiến sĩ",
"Yêu cầu đối với việc xây dựng chương trình đào tạo",
"Loại chương trình đào tạo",
"Yêu cầu và cấu trúc của chương trình đào tạo",
"Quản lý chương trình đào tạo",
"Thời gian, hình thức, ngôn ngữ đào tạo",
"Tổ chức và quản lý hoạt động đào tạo",
"Những thay đổi trong quá trình đào tạo",
"Giảng viên giảng dạy chương trình đào tạo trình độ tiến sĩ",
"Người hướng dẫn nghiên cứu sinh",
"Nhiệm vụ và quyền của nghiên cứu sinh",
"Nhiệm vụ và quyền của Bộ môn đào tạo",
"Nhiệm vụ và quyền của Hội đồng ngành và Khoa",
"Nhiệm vụ và quyền của Phòng đào tạo Sau đại học",
"Yêu cầu đối với luận án tiến sĩ",
"Quy trình và phân công trong tổ chức đánh giá luận án",
"Đánh giá luận án cấp Khoa",
"Quy trình bảo vệ luận án cấp Khoa",
"Phản biện độc lập luận án",
"Điều kiện và hồ sơ đề nghị đánh giá luận án ở Hội đồng đánh giá luận án cấp Trường",
"Hội đồng đánh giá luận án cấp Trường",
"Đánh giá luận án ở cấp Trường",
"Quy trình bảo vệ luận án cấp Trường",
"Đánh giá lại luận án ở cấp Trường",
"Đánh giá luận án theo chế độ mật",
"Thẩm định quá trình đào tạo và chất lượng luận án",
"Hồ sơ thẩm định quá trình đào tạo và chất lượng luận án",
"Quy trình thẩm định quá trình đào tạo và chất lượng luận án",
"Hội đồng thẩm định luận án",
"Xử lý kết quả thẩm định",
"Cấp bằng tiến sĩ",
"Khiếu nại, tố cáo",
"Thanh tra, kiểm tra",
"Xử lý vi phạm",
"Xử lý học vụ",
"Quy định chuyển tiếp ",
"HÌNH THỨC VÀ CẤU TRÚC LUẬN ÁN TIẾN SĨ",
]

# questions = [
#     "Năm thành lập của trường Đại học Bách Khoa",
#     "Hôm này trời đẹp nhỉ"
# ]

document_loader = Document_Loader(PATH, index_offset)
data = [text['text'] for text in document_loader.get_passage()]
data = list(map(preprocess, data))

# retriever = BM25Gensim(data)
# retriever.create_model(TEST_OUT_PATH)

FULL_OUT_PATH = "./document_retrieval/index/phd"
K = 3

retriever = BM25Gensim()
retriever.load_model(FULL_OUT_PATH)

for question in questions:
    retrieve_results, scores = retriever.get_top_result(question, K)
    print(question, '\n\n')
    print(scores, '\n\n')
    for retrieve_result in retrieve_results:        
        context = document_loader.get_context()[retrieve_result]
        id = document_loader.get_id()[retrieve_result]
        print(context, '\n')
        # print(id, '\n\n\n\n')
    enter = input("Hit ENTER to see next result")









import fitz  # PyMuPDF
import os

def save_pdf_pages_as_pdfs(pdf_path, output_dir):
    # output_dir가 없으면 생성
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        new_doc = fitz.open()  # 빈 PDF 생성
        new_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
        output_path = os.path.join(output_dir, f"page_{page_num + 1}.pdf")
        new_doc.save(output_path)
        new_doc.close()
    doc.close()

# 사용 예시
if __name__ == "__main__":
    pdf_file = "/nearline/sa/yunho/docling_test/test/수학영역_문제지_홀수형.pdf"  # 처리할 PDF 파일 경로
    output_folder = "/nearline/sa/yunho/vlm_test_250219/data/tnsmdtngkr"  # 저장할 폴더명
    save_pdf_pages_as_pdfs(pdf_file, output_folder)

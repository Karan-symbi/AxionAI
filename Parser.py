from langchain_community.document_loaders import PyPDFLoader

class Parser():
    def __init__(self):
        pass
    def parse(self,file_path):
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        no_of_pages = pages[0].metadata["total_pages"]
        content = []
        for i in range(no_of_pages):
            content.append(pages[i].page_content)

        return {
            "content": content,
            "no_of_pages": no_of_pages
        }


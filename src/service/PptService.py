import os
import uuid

from pptx import Presentation
import  datetime
import pypandoc
class PptService:


    def __init__(self,words):
        self.words = words
        self.fileName=uuid.uuid4().hex
        folder,md_file=self.create_date_folder_and_save_md(base_dir=".",fileName=self.fileName,words=self.words)
        self.pathFile=md_file
        self.folder = folder
        self.md_file = md_file
        print(f"文件夹路径：{folder}\n文件路径：{md_file}")
        pass

    def create_date_folder_and_save_md(self,base_dir,fileName,words):
        # 获取日期信息
        # 构建文件夹路径
        folder_path = os.path.join(base_dir,"doc")

        # 创建文件夹
        os.makedirs(folder_path, exist_ok=True)

        # 生成Markdown文件
        md_filename = os.path.join(folder_path, fileName+".md")
        md_content =  words

        # 保存文件
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(md_content)
        return folder_path, md_filename


    def gernatePptFile(self):
        print(self.pathFile)
        ppts=os.path.join(self.folder,self.fileName+".pptx")
        outfile = pypandoc.convert_file(self.pathFile, 'pptx',
                                       outputfile=ppts)
        # 保存演示文稿
        return  self.fileName+".pptx"
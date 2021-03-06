import glob, os
import win32timezone
import pandas as pd

pd.set_option('display.max_columns', None)
import re


def get_content_from_txt(path):
    dl = []
    file_count = len(glob.glob(os.path.join(path, "*/*.txt")))
    # invalid_list = open()
    for f in glob.glob(os.path.join(path, "*/*.txt")):
        with open(f, mode='r', errors='replace') as fd:
            cell_content = []
            for line in fd.readlines():
                if line:
                    cell_content.append(line.strip(' '))

        all_clause = "".join(cell_content)
        words_Count = len(all_clause)  # 作品文字数
        # novel_name = f.split('\\')[-2:-1]#作品名称
        file_content = re.split('。|\n', all_clause)
        cf = pd.DataFrame(file_content, columns=['Clause'])
        cf['WorkName'] = cf.apply(lambda x: f.split('\\')[-1].replace('.txt', ''), axis=1)
        cf['Author'] = cf.apply(lambda x: f.split('\\')[-2], axis=1)
        cf['Category'] = cf.apply(lambda x: f.split('\\')[-3], axis=1)
        dl.append(cf)
        # print(dl)
        clause_count = len(file_content)  # 作品句子数
        # 显示Progress
        progress = len(dl) / file_count * 100
        print("%.2f%%" % progress)
    df = pd.concat(dl, axis=0)
    df['Clause'] = df.apply(lambda x: x.str.strip())
    # print(df)
    # print(dl[:100])
    # df.dropna(how='all',inplace=True)
    return df


content_range = input("请输入想要搜索的范围：")
df = get_content_from_txt(content_range)
df.reset_index(inplace=True)
df[1000001:].to_excel('result2.xlsx', )
print(df)

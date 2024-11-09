import os

def 创建文件(文件名):
    try:
        with open(文件名, 'w', encoding='utf-8') as f:
            pass
        print(f"文件 {文件名} 创建成功。")
    except IOError as e:
        print(f"文件操作出错：{e}")

def 删除文件(文件名):
    try:
        os.remove(文件名)
        print(f"文件 {文件名} 删除成功。")
    except OSError as e:
        print(f"文件操作出错：{e}")

def 写入文件(文件名, 内容):
    try:
        with open(文件名, 'a', encoding='utf-8') as f:
            f.write(内容 + '\n')
        print(f"内容已成功写入 {文件名}。")
    except IOError as e:
        print(f"文件操作出错：{e}")

def 读取文件(文件名):
    try:
        with open(文件名, 'r', encoding='utf-8') as f:
            内容 = f.read()
            print(f"文件 {文件名} 的内容为：")
            print(内容)
    except IOError as e:
        print(f"文件操作出错：{e}")

def 编辑文件(文件名):
    try:
        if not os.path.exists(文件名):
            print(f"文件 {文件名} 不存在，无法编辑。")
            return
        
        content = input("请输入要添加或修改的内容（输入'q'完成编辑）：")
        while content != 'q':
            写入文件(文件名, content)
            content = input("请输入要继续添加或修改的内容（输入'q'完成编辑）：")
        print(f"文件 {文件名} 编辑完成。")
    except IOError as e:
        print(f"文件操作出错：{e}")

def 显示帮助():
    print("""
    帮助信息：
    1. 创建文件：创建一个新文件。
    2. 删除文件：删除指定文件。
    3. 写入文件：向指定文件追加内容。
    4. 读取文件：显示指定文件的内容。
    5. 编辑文件：向指定文件添加或修改内容。
    6. 显示帮助：显示此帮助信息。
    7. 关于：显示程序相关信息。
    """)

def 关于():
    print("""
          欢迎使用文本编辑器！
    关于
                文本编辑器
    通过Python内置库OS模块，实现文本编辑器功能。
    通过简单易操作的命令行界面，采用数字指令进行操作。
    这是一个简单的文本编辑器，使用Python内置库实现。
    功能包括文件的创建、删除、写入、读取、编辑，以及帮助和关于信息的显示。
          作者：HYX 2024.11.9    版本：0.1
          联系方式：huang17345021577@outlook.com
          版权所有：HYX  感谢支持！
    """)

def 文本编辑器():
    while True:
        print("""
        请选择要执行的操作：
        1. 创建文件
        2. 删除文件
        3. 写入文件
        4. 读取文件
        5. 编辑文件
        6. 显示帮助
        7. 关于
        8. 退出程序
        """)
        操作 = input("请输入您的选择（1-8）：")
        if 操作 == "1":
            文件名 = input("请输入要创建的文件名：")
            创建文件(文件名)
        elif 操作 == "2":
            文件名 = input("请输入要删除的文件名：")
            删除文件(文件名)
        elif 操作 == "3":
            文件名 = input("请输入要写入的文件名：")
            内容 = input("请输入要写入的内容：")
            写入文件(文件名, 内容)
        elif 操作 == "4":
            文件名 = input("请输入要读取的文件名：")
            读取文件(文件名)
        elif 操作 == "5":
            文件名 = input("请输入要编辑的文件名：")
            编辑文件(文件名)
        elif 操作 == "6":
            显示帮助()
        elif 操作 == "7":
            关于()
        elif 操作 == "8":
            print("感谢使用文本编辑器，再见！")
            break
        else:
            print("无效的操作，请重新输入。")

if __name__ == "__main__":
    文本编辑器()
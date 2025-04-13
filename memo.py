import argparse
import json
import os
from datetime import datetime

DATA_FILE = 'memo.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_memo(content):
    data = load_data()
    memo = {
        "content": content,
        "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    data.append(memo)
    save_data(data)
    print("✅ 添加成功")

def list_memos():
    data = load_data()
    if not data:
        print("暂无备忘录")
    for i, memo in enumerate(data, 1):
        print(f"{i}. {memo['content']}  📅 {memo['time']}")

def delete_memo(index):
    data = load_data()
    if 0 < index <= len(data):
        removed = data.pop(index - 1)
        save_data(data)
        print(f"🗑️ 已删除：{removed}")
    else:
        print("❌ 无效编号")
        
def search_memos(keyword):
    data = load_data()
    found = False
    for i, memo in enumerate(data, 1):
        if keyword.lower() in memo['content'].lower():
            print(f"{i}. {memo['content']}  📅 {memo['time']}")
            found = True
    if not found:
        print("❌ 没有找到相关备忘录")

def main():
    parser = argparse.ArgumentParser(description="命令行备忘录工具")
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('list', help='查看所有备忘录')

    add_parser = subparsers.add_parser('add', help='添加备忘录')
    add_parser.add_argument('content', type=str, help='备忘内容')

    del_parser = subparsers.add_parser('delete', help='删除备忘录')
    del_parser.add_argument('index', type=int, help='要删除的编号')
    
    search_parser = subparsers.add_parser('search', help='搜索备忘录')
    search_parser.add_argument('keyword', type=str, help='关键词')

    args = parser.parse_args()

    if args.command == 'add':
        add_memo(args.content)
    elif args.command == 'list':
        list_memos()
    elif args.command == 'delete':
        delete_memo(args.index)
    elif args.command == 'search':
        search_memos(args.keyword)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
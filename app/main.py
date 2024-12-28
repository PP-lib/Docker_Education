import os

def process_files(directory):
    # ディレクトリ内のファイルを取得
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    for file in files:
        filepath = os.path.join(directory, file)
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
            print(f"Processing file: {file}")
            for line in lines:
                # 各行で文字を連結
                concatenated = ''.join(line.strip())
                print(concatenated)

if __name__ == "__main__":
    # データフォルダのパス
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        print("Data directory does not exist.")
    else:
        process_files(data_dir)

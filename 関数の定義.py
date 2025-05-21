# 関数の定義.py

def greet(name):
    if name == "tarou":
        print(f"こんにちは、{name}さん！")
    else:
        print(f"{name}さん、こんにちは！")

# ユーザーから名前を入力する
user_name = input("あなたの名前を入力してください: ")

# 関数を実行
greet(user_name)

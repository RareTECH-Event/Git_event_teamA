def main():
    while True:
        print("選択してください：")
        print("1: くぅ＠50期")
        print("2: Moemi@50期")
        print("3: おすし@50期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("変更しました")
        elif choice == "2":
            print("メンバー2のコメント")
        elif choice == "3":
            print("メンバー3のコメント")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()


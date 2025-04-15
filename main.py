def main():
    while True:
        print("選択してください：")
        print("1: メンバー1の1ゆーせー@53期")
        print("2: メンバー2のリョウ＠52期")
        print("3: メンバー3のたな@53期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("ハンズオン頑張ります！")
        elif choice == "2":
            print("よろしくお願いいたします！")
        elif choice == "3":
            print("時間かかってすみません")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

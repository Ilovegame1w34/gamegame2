from engine.game import Game


class MainMenu:

    def __init__(self):

        self.running = True

    # ---------------------------------
    # 메인 메뉴 실행
    # ---------------------------------
    def run(self):

        while self.running:

            self.clear()

            self.logo()

            print("1. 새 게임")
            print("2. 이어하기")
            print("3. 설정")
            print("4. 도움말")
            print("5. 크레딧")
            print("0. 종료")
            print()

            command = input("선택 > ")

            if command == "1":
                self.new_game()

            elif command == "2":
                self.load_game()

            elif command == "3":
                self.settings()

            elif command == "4":
                self.help()

            elif command == "5":
                self.credits()

            elif command == "0":
                self.running = False

            else:
                input("\n잘못된 입력입니다. 엔터를 누르세요...")

        print("\n게임을 종료합니다.")

    # ---------------------------------
    # 새 게임
    # ---------------------------------
    def new_game(self):

        game = Game()
        game.run()

    # ---------------------------------
    # 이어하기
    # ---------------------------------
    def load_game(self):

        print("\n💾 이어하기는 v0.5.0에서 구현 됩니다.")
        input("\n엔터를 누르세요...")

    # ---------------------------------
    # 설정
    # ---------------------------------
    def settings(self):

        while True:

            self.clear()

            print("========== 설정 ==========")
            print("1. (예정) 소리")
            print("2. (예정) 난이도")
            print("3. (예정) 화면")
            print("0. 뒤로가기")
            print("==========================")

            command = input("> ")

            if command == "0":
                return

    # ---------------------------------
    # 도움말
    # ---------------------------------
    def help(self):

        self.clear()

        print("========== 도움말 ==========\n")

        print("W A S D : 이동")
        print("I : 인벤토리")
        print("Q : 퀘스트")
        print("M : 미니맵 ON/OFF")
        print("X : 게임 종료")

        print("\n전투")
        print("1 : 공격")
        print("2 : 포션")
        print("3 : 도망")

        input("\n엔터를 누르세요...")

    # ---------------------------------
    # 크레딧
    # ---------------------------------
    def credits(self):

        self.clear()

        print("========== CREDITS ==========\n")

        print("TerminalLegends")
        print("Version : 0.4.1")
        print()
        print("Developer : hoyoon ki")
        print("Programming : hoyoon ki")
        print("Engine : Terminal")

        input("\n엔터를 누르세요...")

    # ---------------------------------
    # 로고
    # ---------------------------------
    def logo(self):

        print("=" * 50)
        print("        TerminalLegends v0.4.1")
        print("=" * 50)
        print()
        print("████████╗██████╗ ")
        print("╚══██╔══╝██╔══██╗")
        print("   ██║   ██████╔╝")
        print("   ██║   ██╔══██╗")
        print("   ██║   ██║  ██║")
        print("   ╚═╝   ╚═╝  ╚═╝")
        print()
        print("     A Terminal RPG Adventure")
        print()

    # ---------------------------------
    # 화면 지우기
    # ---------------------------------
    def clear(self):

        import os

        os.system("cls" if os.name == "nt" else "clear")
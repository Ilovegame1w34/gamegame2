import os


class UI:

    def __init__(self):
        pass

    # ----------------------------------
    # 화면 지우기
    # ----------------------------------
    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    # ----------------------------------
    # 타이틀
    # ----------------------------------
    def title(self):

        self.clear()

        print("=" * 60)
        print("          TERMINAL LEGENDS")
        print("            v0.3.3-1")
        print("         PRERELEASE")
        print("=" * 60)
        print()
        print("1. 새 게임")
        print("2. 이어하기")
        print("3. 설정")
        print("4. 종료")
        print()

    # ----------------------------------
    # 일시정지
    # ----------------------------------
    def pause(self):

        self.clear()

        print("========== PAUSE ==========")
        print("1. 게임 계속")
        print("2. 저장")
        print("3. 메인 메뉴")
        print("===========================")

    # ----------------------------------
    # 게임오버
    # ----------------------------------
    def game_over(self):

        self.clear()

        print()
        print("██████   █████  ███    ███ ███████")
        print("██       ██   ██ ████  ████ ██")
        print("██   ███ ███████ ██ ████ ██ █████")
        print("██    ██ ██   ██ ██  ██  ██ ██")
        print(" ██████  ██   ██ ██      ██ ███████")
        print()
        print("💀 GAME OVER 💀")
        print()

    # ----------------------------------
    # 승리
    # ----------------------------------
    def victory(self):

        self.clear()

        print()
        print("🏆 VICTORY!")
        print("축하합니다!")
        print()

    # ----------------------------------
    # 레벨업
    # ----------------------------------
    def level_up(self, player):

        print()
        print("========================")
        print("⭐ LEVEL UP!")
        print("========================")
        print(f"현재 레벨 : {player.level}")
        print(f"ATK : {player.atk}")
        print(f"DEF : {player.defense}")
        print(f"HP  : {player.max_hp}")
        print("========================")

    # ----------------------------------
    # 퀘스트 완료
    # ----------------------------------
    def quest_complete(self, quest_name):

        print()
        print("========================")
        print("📜 QUEST COMPLETE!")
        print(quest_name)
        print("========================")

    # ----------------------------------
    # 업적
    # ----------------------------------
    def achievement(self, name):

        print()
        print("========================")
        print("🏅 ACHIEVEMENT")
        print(name)
        print("========================")

    # ----------------------------------
    # 저장 완료
    # ----------------------------------
    def saved(self):

        print("💾 저장 완료!")

    # ----------------------------------
    # 불러오기 완료
    # ----------------------------------
    def loaded(self):

        print("📂 저장 데이터 불러오기 완료!")

    # ----------------------------------
    # 오류
    # ----------------------------------
    def error(self, text):

        print()
        print("❌ ERROR")
        print(text)

    # ----------------------------------
    # 안내
    # ----------------------------------
    def message(self, text):

        print(text)

    # ----------------------------------
    # 입력 대기
    # ----------------------------------
    def wait(self):

        input("\n엔터를 누르세요...")

    # ----------------------------------
    # 진행바
    # ----------------------------------
    def progress_bar(self, current, maximum, length=20):

        if maximum <= 0:
            maximum = 1

        filled = int((current / maximum) * length)

        if filled > length:
            filled = length

        return "█" * filled + "░" * (length - filled)

    # ----------------------------------
    # HP바
    # ----------------------------------
    def hp_bar(self, player):

        return self.progress_bar(
            player.hp,
            player.max_hp
        )

    # ----------------------------------
    # EXP바
    # ----------------------------------
    def exp_bar(self, player):

        return self.progress_bar(
            player.exp,
            player.need_exp
        )
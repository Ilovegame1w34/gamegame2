class QuestManager:

    def __init__(self):

        self.quests = {

            "first_kill": {
                "name": "첫 사냥",
                "description": "몬스터 1마리 처치",
                "target": 1,
                "progress": 0,
                "reward_exp": 20,
                "reward_gold": 50,
                "completed": False
            },

            "monster_hunter": {
                "name": "몬스터 헌터",
                "description": "몬스터 10마리 처치",
                "target": 10,
                "progress": 0,
                "reward_exp": 100,
                "reward_gold": 150,
                "completed": False
            },

            "slayer": {
                "name": "슬레이어",
                "description": "몬스터 50마리 처치",
                "target": 50,
                "progress": 0,
                "reward_exp": 500,
                "reward_gold": 500,
                "completed": False
            },

            "rich": {
                "name": "부자",
                "description": "골드 1000 모으기",
                "target": 1000,
                "progress": 0,
                "reward_exp": 300,
                "reward_gold": 100,
                "completed": False
            },

            "level5": {
                "name": "강해지는 중",
                "description": "레벨 5 달성",
                "target": 5,
                "progress": 1,
                "reward_exp": 300,
                "reward_gold": 200,
                "completed": False
            },

            "boss": {
                "name": "최후의 적",
                "description": "보스 처치",
                "target": 1,
                "progress": 0,
                "reward_exp": 1000,
                "reward_gold": 1000,
                "completed": False
            }

        }

    # -------------------------
    # 몬스터 처치
    # -------------------------
    def monster_killed(self, player):

        self.quests["first_kill"]["progress"] += 1
        self.quests["monster_hunter"]["progress"] += 1
        self.quests["slayer"]["progress"] += 1

        self.check(player)

    # -------------------------
    # 보스 처치
    # -------------------------
    def boss_killed(self, player):

        self.quests["boss"]["progress"] = 1

        self.check(player)

    # -------------------------
    # 골드 갱신
    # -------------------------
    def gold_update(self, player):

        self.quests["rich"]["progress"] = player.gold

        self.check(player)

    # -------------------------
    # 레벨 갱신
    # -------------------------
    def level_update(self, player):

        self.quests["level5"]["progress"] = player.level

        self.check(player)

    # -------------------------
    # 퀘스트 완료 확인
    # -------------------------
    def check(self, player):

        for quest in self.quests.values():

            if quest["completed"]:
                continue

            if quest["progress"] >= quest["target"]:

                quest["completed"] = True

                print("\n📜 QUEST COMPLETE!")
                print(f"▶ {quest['name']}")
                print(f"+{quest['reward_exp']} EXP")
                print(f"+{quest['reward_gold']} GOLD")

                player.add_exp(quest["reward_exp"])
                player.add_gold(quest["reward_gold"])

    # -------------------------
    # 진행도 출력
    # -------------------------
    def show(self):

        print("\n========== QUEST ==========")

        for quest in self.quests.values():

            status = "✅" if quest["completed"] else "⬜"

            print(f"{status} {quest['name']}")
            print(f"   {quest['description']}")
            print(f"   {quest['progress']} / {quest['target']}")
            print()

        print("===========================")

    # -------------------------
    # 완료 개수
    # -------------------------
    def completed_count(self):

        return sum(
            1
            for quest in self.quests.values()
            if quest["completed"]
        )

    # -------------------------
    # 전체 완료 여부
    # -------------------------
    def all_completed(self):

        return self.completed_count() == len(self.quests)

    # -------------------------
    # 저장용
    # -------------------------
    def get_save_data(self):

        return self.quests

    # -------------------------
    # 불러오기용
    # -------------------------
    def load_save_data(self, data):

        if data:
            self.quests = data
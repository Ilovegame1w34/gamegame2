import json
import os


class SaveSystem:

    def __init__(self):

        self.save_folder = "saves"
        self.save_file = os.path.join(self.save_folder, "save.json")

        if not os.path.exists(self.save_folder):
            os.makedirs(self.save_folder)

    # ----------------------------------
    # 저장
    # ----------------------------------
    def save(self, player, inventory, quests):

        data = {

            "player": {

                "name": player.name,

                "x": player.x,
                "y": player.y,

                "hp": player.hp,
                "max_hp": player.max_hp,

                "level": player.level,
                "exp": player.exp,
                "need_exp": player.need_exp,

                "gold": player.gold,

                "atk": player.atk,
                "defense": player.defense,

                "critical": player.critical,
                "dodge": player.dodge

            },

            "inventory": {

                "potions": inventory.potions,

                "weapon": inventory.weapon,

                "armor": inventory.armor,

                "items": inventory.items

            },

            "quests": quests.quests

        }

        with open(self.save_file, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("💾 게임 저장 완료!")

    # ----------------------------------
    # 불러오기
    # ----------------------------------
    def load(self, player, inventory, quests):

        if not os.path.exists(self.save_file):

            print("📂 저장 파일이 없습니다.")
            return False

        with open(self.save_file, "r", encoding="utf-8") as file:

            data = json.load(file)

        # ---------------- Player ----------------

        p = data["player"]

        player.name = p["name"]

        player.x = p["x"]
        player.y = p["y"]

        player.hp = p["hp"]
        player.max_hp = p["max_hp"]

        player.level = p["level"]
        player.exp = p["exp"]
        player.need_exp = p["need_exp"]

        player.gold = p["gold"]

        player.atk = p["atk"]
        player.defense = p["defense"]

        player.critical = p["critical"]
        player.dodge = p["dodge"]

        # ---------------- Inventory ----------------

        inv = data["inventory"]

        inventory.potions = inv["potions"]

        inventory.weapon = inv["weapon"]

        inventory.armor = inv["armor"]

        inventory.items = inv["items"]

        # ---------------- Quest ----------------

        quests.quests = data["quests"]

        print("📂 저장 데이터 불러오기 완료!")

        return True

    # ----------------------------------
    # 새 게임
    # ----------------------------------
    def new_game(self):

        if os.path.exists(self.save_file):

            os.remove(self.save_file)

            print("🗑️ 저장 데이터를 삭제했습니다.")

    # ----------------------------------
    # 저장 존재 여부
    # ----------------------------------
    def exists(self):

        return os.path.exists(self.save_file)

    # ----------------------------------
    # 자동 저장
    # ----------------------------------
    def auto_save(self, player, inventory, quests):

        self.save(player, inventory, quests)
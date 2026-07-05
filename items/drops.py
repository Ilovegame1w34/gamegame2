import random


class ItemDrops:

    def __init__(self):

        self.common = [
            "Small Potion",
            "Apple",
            "Wood",
            "Stone"
        ]

        self.uncommon = [
            "Potion",
            "Iron",
            "Leather",
            "Bone"
        ]

        self.rare = [
            "Iron Sword",
            "Iron Armor",
            "Gold Ingot",
            "Magic Scroll"
        ]

        self.epic = [
            "Diamond Sword",
            "Diamond Armor",
            "Phoenix Feather"
        ]

        self.legendary = [
            "Legendary Sword",
            "Dragon Armor",
            "Ancient Relic"
        ]

    # -------------------------
    # 일반 몬스터 드롭
    # -------------------------
    def get_drop(self):

        chance = random.randint(1, 100)

        if chance <= 45:
            return random.choice(self.common)

        elif chance <= 75:
            return random.choice(self.uncommon)

        elif chance <= 92:
            return random.choice(self.rare)

        elif chance <= 99:
            return random.choice(self.epic)

        else:
            return random.choice(self.legendary)

    # -------------------------
    # 보스 드롭
    # -------------------------
    def get_boss_drop(self):

        return random.choice([
            "Legendary Sword",
            "Dragon Armor",
            "Ancient Relic",
            "Boss Trophy",
            "Boss Chest Key"
        ])

    # -------------------------
    # 드롭 처리
    # -------------------------
    def drop(self, enemy, inventory):

        if enemy.name == "Demon King":

            item = self.get_boss_drop()

        else:

            item = self.get_drop()

        inventory.add_item(item)

        print(f"\n🎁 {enemy.name}이(가)")
        print(f"『{item}』을(를) 드롭했습니다!")

        return item
class Weapon:

    def __init__(self):

        self.weapons = {

            "Wooden Sword": {
                "atk": 5,
                "price": 50,
                "rarity": "Common"
            },

            "Stone Sword": {
                "atk": 10,
                "price": 120,
                "rarity": "Common"
            },

            "Iron Sword": {
                "atk": 18,
                "price": 300,
                "rarity": "Uncommon"
            },

            "Steel Sword": {
                "atk": 28,
                "price": 700,
                "rarity": "Rare"
            },

            "Diamond Sword": {
                "atk": 40,
                "price": 1500,
                "rarity": "Epic"
            },

            "Dragon Slayer": {
                "atk": 60,
                "price": 3000,
                "rarity": "Legendary"
            },

            "Legendary Sword": {
                "atk": 100,
                "price": 9999,
                "rarity": "Mythic"
            }

        }

    # -------------------------
    # 장착
    # -------------------------
    def equip(self, player, inventory, weapon_name):

        if weapon_name not in inventory.items:
            print("❌ 해당 무기가 없습니다.")
            return False

        if weapon_name not in self.weapons:
            print("❌ 장착할 수 없는 아이템입니다.")
            return False

        # 기존 무기 해제
        if inventory.weapon:

            old = inventory.weapon

            player.atk -= self.weapons[old]["atk"]

            inventory.add_item(old)

        inventory.weapon = weapon_name

        player.atk += self.weapons[weapon_name]["atk"]

        inventory.remove_item(weapon_name)

        print(f"⚔️ {weapon_name} 장착!")

        return True

    # -------------------------
    # 해제
    # -------------------------
    def unequip(self, player, inventory):

        if inventory.weapon is None:
            return

        player.atk -= self.weapons[inventory.weapon]["atk"]

        inventory.add_item(inventory.weapon)

        print(f"⚔️ {inventory.weapon} 해제")

        inventory.weapon = None

    # -------------------------
    # 가격
    # -------------------------
    def get_price(self, weapon_name):

        if weapon_name in self.weapons:
            return self.weapons[weapon_name]["price"]

        return 0

    # -------------------------
    # 판매 가격
    # -------------------------
    def sell_price(self, weapon_name):

        return self.get_price(weapon_name) // 2

    # -------------------------
    # 공격력
    # -------------------------
    def get_attack(self, weapon_name):

        if weapon_name in self.weapons:
            return self.weapons[weapon_name]["atk"]

        return 0

    # -------------------------
    # 목록
    # -------------------------
    def show(self):

        print("\n========== WEAPONS ==========")

        for name, data in self.weapons.items():

            print(f"{name}")
            print(f"공격력 : +{data['atk']}")
            print(f"등급   : {data['rarity']}")
            print(f"가격   : {data['price']} G")
            print()

        print("=============================")
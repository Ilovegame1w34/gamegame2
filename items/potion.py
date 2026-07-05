class Potion:

    def __init__(self):

        self.potions = {

            "Small Potion": {
                "heal": 30,
                "price": 30
            },

            "Potion": {
                "heal": 60,
                "price": 70
            },

            "Large Potion": {
                "heal": 120,
                "price": 150
            },

            "Super Potion": {
                "heal": 250,
                "price": 300
            },

            "Elixir": {
                "heal": 9999,
                "price": 1000
            }

        }

    # -------------------------
    # 사용
    # -------------------------
    def use(self, player, inventory, potion_name):

        if potion_name not in inventory.items:

            print("❌ 해당 포션이 없습니다.")
            return False

        if potion_name not in self.potions:

            print("❌ 사용할 수 없는 아이템입니다.")
            return False

        heal = self.potions[potion_name]["heal"]

        player.hp += heal

        if player.hp > player.max_hp:
            player.hp = player.max_hp

        inventory.remove_item(potion_name)

        print(f"🧪 {potion_name} 사용!")
        print(f"+{heal} HP")

        return True

    # -------------------------
    # 구매 가격
    # -------------------------
    def get_price(self, potion_name):

        if potion_name in self.potions:
            return self.potions[potion_name]["price"]

        return 0

    # -------------------------
    # 판매 가격
    # -------------------------
    def sell_price(self, potion_name):

        return self.get_price(potion_name) // 2

    # -------------------------
    # 포션 목록
    # -------------------------
    def show(self):

        print("\n====== POTIONS ======")

        for name, data in self.potions.items():

            print(f"{name}")
            print(f"회복 : {data['heal']} HP")
            print(f"가격 : {data['price']} G")
            print()

        print("=====================")
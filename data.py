# Credit to https://github.com/graphql-python/graphene/blob/master/examples/starwars/data.py
from schema import BahayKubo, Vegetable


mang_netong_bahay_kubo = BahayKubo(
    id="1001",
    name="Netong's Bahay Kubo",
    owner="Netong Santos",
    address="39 hardin st. Silang Cavite",
    has_parking=True,
    vegetables=["1001", "1002", "1003"],
)

aling_berta_bahay_kubo = BahayKubo(
    id="1002",
    name="Netong's Bahay Kubo",
    vegetables=["1004"],
)

mustard = Vegetable(
    id="1001",
    name="Mustard/Mustasa",
    picking_month="June",
    fee="35",
    is_organic=True,
)

eggplant = Vegetable(
    id="1002",
    name="Eggplant/Talong",
    picking_month="May",
    fee="65",
    is_organic=False,
)

tomato = Vegetable(
    id="1003",
    name="Tomato/Kamatis",
    picking_month="December",
    fee="35",
)

loofah = Vegetable(
    id="1004",
    name="Loofah/Patola",
    picking_month="September",
    fee="20",
    is_organic="False",
)

bahay_kubo_data = {
    "1001": mang_netong_bahay_kubo,
    "1002": aling_berta_bahay_kubo,
}

vegetable_data = {
    "1001": mustard,
    "1002": eggplant,
    "1003": tomato,
    "1004": loofah,
}


def get_bahay_kubo(id):
    return bahay_kubo_data.get(str(id))


def get_vegetable(id):
    return vegetable_data.get(str(id))

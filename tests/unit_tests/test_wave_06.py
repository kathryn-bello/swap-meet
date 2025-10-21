import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_get_items_by_category():
    item_a = Clothing()
    item_b = Electronics()
    item_c = Clothing()
    item_d = Decor()
    item_e = Item()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    items = vendor.get_by_category("Clothing")

    assert len(items) == 2
    assert item_a in items
    assert item_c in items

#@pytest.mark.skip
def test_get_no_matching_items_by_category():
    item_a = Clothing()
    item_b = Item()
    item_c = Decor()
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("Electronics")

    assert items == []

#@pytest.mark.skip
def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

#@pytest.mark.skip
def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

#@pytest.mark.skip
def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_category("Clothing")

    # Assert
    assert best_item.get_category() == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

#@pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_f]
    assert jesse.inventory == [item_d, item_e, item_c]

#@pytest.mark.skip
def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_a, item_f]
    assert jesse.inventory == [item_e, item_d, item_c]

#@pytest.mark.skip
def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

#@pytest.mark.skip
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

#@pytest.mark.skip
def test_swap_best_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    assert result is False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_c]
    assert jesse.inventory == [item_d, item_e, item_f]

#@pytest.mark.skip
def test_swap_best_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other_vendor=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    
    assert result is False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_c, item_b, item_a]
    assert jesse.inventory == [item_f, item_e, item_d]

#@pytest.mark.skip
def test_get_newest_item():
    item_a = Clothing(age=13)
    item_b = Electronics(age=2)
    item_c = Clothing(age=34)
    item_d = Decor(age=10)
    item_e = Item(age=46)
    test_inventory_1 = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = test_inventory_1.get_newest_item()
    
    assert newest_item == item_b

#@pytest.mark.skip
def test_swap_newest_item():
    # Arrange
    # me
    dress = Clothing(age=3)
    ipod = Electronics(age=10)
    coffee_table = Decor(age=4)
    video_card = Electronics(age=2)
    first_vendor = Vendor(
        inventory=[dress, ipod, coffee_table, video_card]
    )

    # them
    jacket = Clothing(age=5)
    desk = Decor(age=2)
    lamp = Decor(age=6)
    second_vendor = Vendor(
        inventory=[jacket, desk, lamp]
    )

    # Act
    result = first_vendor.swap_by_newest(second_vendor)

    assert result is True
    assert len(first_vendor.inventory) == 4
    assert len(second_vendor.inventory) == 3
    assert first_vendor.inventory == [dress, ipod, coffee_table, desk]
    assert second_vendor.inventory == [jacket, lamp, video_card]

#@pytest.mark.skip
def test_swap_newest_item_empty_vendor():
    # Arrange
    # me
    dress = Clothing(age=3)
    ipod = Electronics(age=10)
    coffee_table = Decor(age=4)
    video_card = Electronics(age=2)
    first_vendor = Vendor(
        inventory=[dress, ipod, coffee_table, video_card]
    )

    # them
    second_vendor = Vendor()

    # Act
    result = first_vendor.swap_by_newest(second_vendor)

    assert result is False
    assert len(first_vendor.inventory) == 4
    assert len(second_vendor.inventory) == 0
    assert first_vendor.inventory == [dress, ipod, coffee_table, video_card]
    assert second_vendor.inventory == []

#@pytest.mark.skip
def test_swap_newest_item_duplicate_age():
    # Arrange
    # me
    dress = Clothing(age=3)
    ipod = Electronics(age=3)
    coffee_table = Decor(age=4)
    video_card = Electronics(age=10)
    first_vendor = Vendor(
        inventory=[dress, ipod, coffee_table, video_card]
    )

    # them
    jacket = Clothing(age=5)
    desk = Decor(age=2)
    lamp = Decor(age=2)
    second_vendor = Vendor(
        inventory=[jacket, desk, lamp]
    )

    # Act
    result = first_vendor.swap_by_newest(second_vendor)

    assert result is True
    assert len(first_vendor.inventory) == 4
    assert len(second_vendor.inventory) == 3
    assert first_vendor.inventory == [ipod, coffee_table, video_card, desk]
    assert second_vendor.inventory == [jacket, lamp, dress]
def item_order(order):
    return "salad:{} hamburger:{} water:{}".format(order.count('salad'),\
                                                order.count('hamburger'),\
                                                order.count('water'))

def line_total(item):
    return item["price"]*item["qty"]

def subtotal(cart):
    sum=0
    for i in range(len(cart)):
        sum+=line_total(cart[i])
    return sum

def apply_discount(amount,percent=0):
    discount=amount*(percent/100)
    after_discount=amount-discount
    return after_discount

def gst(amount,rate=18):
    gst_amount=amount*(rate/100)
    return gst_amount

def category_totals(cart):
    categories={}
    #category:total value
    for i in range(len(cart)):
        total=line_total(cart[i])
        if cart[i]["category"] in categories:
            categories[cart[i]["category"]]+=total
        else:
            categories[cart[i]["category"]]=total
    for category,amount in categories.items():
        print(f"{category:<12}{amount:>5}")


def top_items(cart,n=2):
    sorted_cart=sorted(cart,key=line_total,reverse=True)
    top_list=[]
    for i in range(n):
        # print(f"{sorted_cart[i]["name"]:<12}{line_total(sorted_cart[i])}")
        top_list.append(sorted_cart[i]["name"])
    print(top_list)

def print_bill(cart):
    print(f"{"Item":<10}{"Price":>6}{"Qty":>5}{"Total":>8}")
    print('-'*29)
    for i in range(len(cart)):
        print(f"{cart[i]["name"]:<10}{cart[i]["price"]:>6}{cart[i]["qty"]:>5}{line_total(cart[i]):>8}")
    print('-'*29)
    total=subtotal(cart)
    print(f"{"Subtotal":<20}{total:>9.2f}")
    discount=total*.1
    print(f"{"Discount 10%":<20}{discount:>9.2f}")
    bill=total-discount
    gst=bill*.18
    print(f"{"GST 18%":<20}{gst:>9.2f}")
    final=bill+gst
    print(f"{"Grand Total":<20}{final:>9.2f}")

    
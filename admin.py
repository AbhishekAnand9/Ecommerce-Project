import additem
import purchase

def admin_options():
    print("\n")
    print("  E-commerce Admin Panel !!   ")
    print("\n")
    user_inp = input("Tell me Are you an Administrator or a Customer ?(Admin / Customer): ").lower()
    print("\n")
    if user_inp == "admin":
        additem.add_item()  
    elif user_inp == "customer":
        purchase.purchase_product() 
    else:
        print(" Invalid Request !")
if __name__ == "__main__":
    admin_options()
 
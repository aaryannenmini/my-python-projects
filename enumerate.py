sopping=[]
while True:
    print('Welcome to the shopping list app')
    print('1. Add to List')
    print('2. Remove from List')
    print('3. Show List')
    print('4. Exit App')

    choice= int(input("Pick number and Enter New Screen: "))

    if choice == 1:
        You_need = input("What do you want to add: ")
        print("Added")
        sopping.append(You_need)
    elif choice == 2:
        You_cut = input("What do you want to Remove: ")
        if You_cut in sopping:
            sopping.remove(You_cut)
            print("Item removed")
        else:
            print("item not found")

    elif choice == 3:
        for index, i in enumerate(sopping):
            
            print(f"{index+1}.{i}")
    elif choice == 4:
        print("GOOD BYE")
        break

    else:
        print("Invaled Input")

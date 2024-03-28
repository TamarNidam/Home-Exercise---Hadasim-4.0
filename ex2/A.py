import math

def PRINTER(Y , X):

    print((X//2) * " "+"*")

    i = 3
    z = 0

    while i < X:
        i += 2
        z += 1

    i = 3
    if z != 0:
        v = (Y - 2) % z
        if v > 0:
            for Q in range(v):
                print(((X-3)//2) * " "+"***")
    else:
        z = 1
        i = 1
 
    
    for P in range(z):
        for J in range((Y - 2) // z):
            print(((X-i)//2) * " " + i * "*")
        i += 2

    print(X * "*")

def calculate_triangle_perimeter(height, base):
    side = math.sqrt((base / 2)**2  + (height)**2) 
    perimeter = 2 * side + base  
    return perimeter

def main():
    while True:
        print("Menu:")
        print("1. Choose Rectangular Tower")
        print("2. Choose Triangular Tower")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            height = int(input("Enter the height of the tower: "))
            width = int(input("Enter the width of the tower: "))
            
            if height < 2:
                print("Tower height must be greater than or equal to 2.")
                continue
            
            if height == width or (max(height, width)-5)>(min(height, width)):
                print(f"Area of the tower: {height*width}")
            else:
                print(f"The perimeter of the tower is: {(height*2)+(2*width)}")
        
        elif choice == 2:
            height = int(input("Enter the height of the tower: "))
            width = int(input("Enter the width of the tower: "))
            
            if height < 2:
                print("Tower height must be greater than or equal to 2.")
                continue
            
            triangle_choice = int(input("1. Calculate Perimeter\n2. Print Triangle\nEnter your choice: "))
            
            if triangle_choice == 1:
                print(f"Perimeter of the triangle: {calculate_triangle_perimeter(height,width)}")
            
            elif triangle_choice == 2:
                if width % 2 == 0 or width > (2 * height):
                    print("The triangle cannot be printed.")
                else:
                    PRINTER(height, width)
        
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

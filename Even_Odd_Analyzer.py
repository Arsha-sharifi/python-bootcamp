def get_numbers():
    nums = []
    print(' ==== Even & Odd Number Analyser ==== ')
    while True:
        num = input("Enter a number (or 'q' to quit): ").strip()
        
        if not num:
            print("Please enter a valid number or 'q' to quit.")
            continue
        
        if num.lower() == 'q':
            print("Bye Bye")
            break
        
        try:
            nums.append(int(num))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    
    return nums


def analyze_even_odd(nums):
    if not nums:
        print('No numbers entered.')
    even=sum(1 for n in nums if n % 2==0)
    odd=len(nums)-even
    
    print("\n--- Analysis Result ---")
    print(f"Total numbers: {len(nums)}")
    print(f"Even numbers : {even}")
    print(f"Odd numbers  : {odd}")
    print(f"Even %       : {even / len(nums) * 100:.1f}%")
    print(f"Odd %        : {odd / len(nums) * 100:.1f}%")
    print("------------------------")


def Even_Odd_Analyser():    
    result = get_numbers()
    analyze_even_odd(result)
Even_Odd_Analyser()
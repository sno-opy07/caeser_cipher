import pyfiglet
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 1:
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
            else:
                result += char
    elif mode == 2:
        for char in text:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                result += chr((ord(char) - shift - shift_amount) % 26 + shift_amount)
            else:
                result += char
    return result
def main():
        banner = pyfiglet.figlet_format("Snoopy")
        print(banner)
        print("           By Usama Ishtiaq \n      ")
        print("[+] This tool helps you to Encrypt or Decrypt your Text.\n")
        while True:
             message = input("\nEnter the message: ")
             shift_value = int(input("\nEnter the shift value:"))
             action = int(input("\nPress[1] for Encrypt or press [2] for Decrypt? "))
             output = caesar_cipher(message, shift_value, action)
             print("\n",output)
    
             again = input("\nDo you want to continue ? [yes or No]: ")
             if again.lower() != "yes":
               break

if __name__ == "__main__":
    main()

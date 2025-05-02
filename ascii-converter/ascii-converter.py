def ascii_encoder(text):
    return [ord(letter) for letter in ascii_text]

def ascii_decoder(ascii_code):
    return ''.join(chr(num) for num in ascii_code )


if __name__ == "__main__":
    ascii_text = input("Enter ascii text: ")
    print(f"Converted ascii text {ascii_text} to integers: {ascii_encoder(ascii_text)}")
        
    ascii_code = input("Enter list of integers comma separated: ")
    integer_list = [int(x.strip()) for x in ascii_code.split(",")]
    print(f"Converted ascii code {ascii_code} to integers: {ascii_decoder(integer_list)}")

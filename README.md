You can use commands.txt for testing

-v stands for verbose. Helps to track typed commands.

Example
```bash
goit-pycore-hw-07 % python main.py -v < commands.txt
Welcome to the assistant bot!
Enter a command: Command: hello
How can I help you?
Enter a command: Command: add Jane 0501722625
Contact added.
Enter a command: Command: add Jane 0954909119
Contact added.
Enter a command: Command: add Jane 09549094119
09549094119 is not a valid phone number.
Enter a command: Command: birthday Jane 30.07.2024
Birthday added.
Enter a command: Command: birthday Jane 30.07.20242
Invalid date format. Use DD.MM.YYYY
Enter a command: Command: add John 0954456119
Contact added.
Enter a command: Command: birthday John 01.08.2024
Birthday added.
Enter a command: Command: add Jack 0954455119
Contact added.
Enter a command: Command: birthday Jack 01.07.2024
Birthday added.
Enter a command: Command: all
Contact name: Jane
        phones: 0501722625; 0954909119
        birthday: 2024-07-30
Contact name: John
        phones: 0954456119
        birthday: 2024-08-01
Contact name: Jack
        phones: 0954455119
        birthday: 2024-07-01
Enter a command: Command: greetings
name: Jane; Congratulation date: 2024.07.30
name: John; Congratulation date: 2024.08.01
Enter a command: Command: close
Good bye!
```

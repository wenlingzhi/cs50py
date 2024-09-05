import re


class Plugboard:
    def __init__(self):
        self._plugboard = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    @property
    def plugboard(self):
        return ''.join(self._plugboard)

    @plugboard.setter
    def plugboard(self, input_str):
        input_str = input_str.upper()
        if input_str == "":
            self._plugboard = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif re.match(r"^[A-Z]{2}$", input_str):
            char1, char2 = input_str[0], input_str[1]
            idx1, idx2 = ord(char1) - ord('A'), ord(char2) - ord('A')
            # Swap characters
            self._plugboard[idx1], self._plugboard[idx2] = self._plugboard[idx2], self._plugboard[idx1]
        else:
            raise ValueError("Invalid Format. Format: letter+letter. Example: AB")

    def __str__(self):
        return ''.join(self._plugboard)


class EnigmaMachine:
    def __init__(self, rotor_position="0,0,0"):
        self._plugboard = Plugboard()
        self.rotors = [
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            "BDFHJLCPRTXVZNYEIWGAKMUSQO"
        ]
        self.reflector = init_reflector(self.rotors[3])
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rotor_position = rotor_position

    @property
    def plugboard(self):
        return self._plugboard

    @property
    def rotor_position(self):
        return self._rotor_position

    @rotor_position.setter
    def rotor_position(self, input_str):
        if input_str == "":
            pass
        elif re.match(r"^\d,\d,\d$", input_str):
            str_list = input_str.split(",")
            int_list = [0] + [int(item) for item in str_list]
            self._rotor_position = int_list
        else:
            print("Invalid format. Expected format: digital,digital,digital. For example:0,0,0")

    @property
    def rotors(self):
        return self._rotors

    @rotors.setter
    def rotors(self, input_list):
        self._rotors = input_list

    def encode_process(self, letter):
        # plugboard -> three rotors -> reflector -> three rotors
        if letter in self.alphabet:
            after_plugboard = encode_mapping(letter, self._plugboard.plugboard, self.alphabet)
            after_rotor = self.encode_rotor(after_plugboard)
            after_reflector = encode_mapping(after_rotor, self.reflector, self.rotors[3])
            encoded_letter = self.encode_rotor_back(after_reflector)
            result = encode_mapping(encoded_letter,self.plugboard.plugboard,self.alphabet)
            self.rotation()
            return result
        else:
            return letter

    def encode_rotor(self, letter):
        for i in range(len(self.rotors) - 1):
            index = (self.rotors[i].find(letter) + self.rotor_position[i]) % 26
            letter = self.rotors[i + 1][index]
        return letter

    def encode_rotor_back(self, letter):
        for i in range(len(self.rotors) - 1, 0, -1):
            index = (self.rotors[i].find(letter) - self.rotor_position[i - 1]) % 26
            letter = self.rotors[i - 1][index]
        return letter

    def rotation(self):
        self._rotor_position[1] = (self._rotor_position[1] + 1) % 26
        if self._rotor_position[1] == 0:
            self._rotor_position[2] = (self._rotor_position[2] + 1) % 26
            if self._rotor_position[2] == 0:
                self._rotor_position[3] = (self._rotor_position[0] + 1) % 26

    def __str__(self):
        return (f"{"*" * 40}\nRotors Table: {self.rotors[1:]}\nRotors' Position:{self.rotor_position[1:]}"
                f"\nReflector Table: {self.reflector}\nPlugboard Table: {self.plugboard.plugboard}\n{"*" * 40}\n")


def init_reflector(input_str):
    input_str = list(input_str)
    pairs = [
        (19, 21), (11, 24), (6, 16), (1, 8), (3, 13), (2, 18), (12, 22), (5, 20), (0, 15), (4, 10), (7, 25), (9, 14),
        (17, 23)
    ]
    for i, j in pairs:
        input_str[i], input_str[j] = input_str[j], input_str[i]
    return "".join(input_str)


def set_plugboard(machine: EnigmaMachine, swap_str):
    try:
        machine.plugboard.plugboard = swap_str
    except ValueError as e:
        print(e)
    return machine.plugboard.plugboard


def set_rotors_position(machine: EnigmaMachine, position: str):
    machine.rotor_position = position


def swap_rotor(machine: EnigmaMachine, user_input: str):
    valid_permutations = {"123", "132", "213", "231", "312", "321"}
    rotors = [
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    ]
    if user_input in valid_permutations:
        int_list = [int(char) for char in user_input]
        i = 1
        for item in int_list:
            machine.rotors[i] = rotors[item]
            i = i + 1
    else:
        print("Please enter the valid format. (e.g. 123/231/213...)")


def user_encode(machine: EnigmaMachine):
    input_str = input("Please enter letters that you want to encode: ").upper()
    encoded_chars = [machine.encode_process(char) for char in input_str]
    print(''.join(encoded_chars))


def encode_mapping(letter, mapping_table, current_table):
    letter = letter.upper()
    index = current_table.find(letter)
    return mapping_table[index]


def display(machine: EnigmaMachine):
    print("--------Welcome to Enigma Simulator------------")
    print(f"Current Rotors Position = {machine.rotor_position[1::]}")
    print("-----------------------------------------------")
    print("1: Set plugboard")
    print("2: Set rotors")
    print("3: Encode/decode letters")
    print("4: swap rotors")
    print("5: display machine's info")
    print("6:exit")


def main():
    machine = EnigmaMachine()
    while True:
        display(machine)
        choice = input("Choice: ")
        match choice:
            case "1":
                swap_str = input("Plug Setting: Please enter the 2 letters you want to exchange (e.g., AB): ")
                set_plugboard(machine, swap_str)
            case "2":
                position = input("Rotors Setting: Please enter the 3 rotors' positions in format x,y,z (e.g., 0,0,0): ")
                set_rotors_position(machine, position)
            case "3":
                user_encode(machine)
            case "4":
                input_str = input("Swap Rotors: Please enter the new order of rotors. (e.g.,321)")
                swap_rotor(machine, input_str)
            case "5":
                print(machine)
            case "6":
                print("Exiting....")
                break
            case _:
                print("Please enter the correct number.")


if __name__ == "__main__":
    main()

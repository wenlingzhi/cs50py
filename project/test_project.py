from project import EnigmaMachine
from project import init_reflector, swap_rotor, set_plugboard, set_rotors_position, encode_mapping


def test_set_plugboard():
    machine = EnigmaMachine()
    set_rotors_position(machine, "1,0,0")
    assert (machine.rotor_position[1::] == [1, 0, 0])


def test_encode_mapping():
    mapping_table = "KDVIWNA"
    current_table = "ABCDEFG"
    result = encode_mapping("A", mapping_table, current_table)
    assert (result == "K")


def test_plugboard():
    machine = EnigmaMachine()
    set_plugboard(machine, "BC")
    assert (machine.plugboard.plugboard == "ACBDEFGHIJKLMNOPQRSTUVWXYZ")


def test_init_reflector():
    string = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    assert (init_reflector(string) == "ERGNXKIODYJQUHTBCSFMLAZWVP")


def test_swap_rotors():
    machine = EnigmaMachine()
    swap_rotor(machine, "321")
    assert (
        machine.rotors[1::] == "BDFHJLCPRTXVZNYEIWGAKMUSQO", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    )


basic_spectroscopy_text = """_\nbasic_spectroscopy_text\n_index     orbit_s    orbit_f    orbit_h    orbit_k\n"""
for index in range(0, 10800):
    if index <= 9:
        basic_spectroscopy_text += "0"
    if index <= 99:
        basic_spectroscopy_text += "0"
    if index <= 999:
        basic_spectroscopy_text += "0"
    if index <= 9999:
        basic_spectroscopy_text += "0"
    basic_spectroscopy_text += str(index)
    basic_spectroscopy_text += "      0          0          0          0\n"
    print(index)
basic_spectroscopy_text += "_\n"
basic_spectroscopy = open("spectroscopy_basic.txt", "w+")
basic_spectroscopy.write(basic_spectroscopy_text)
basic_spectroscopy.close()


import codecs

# String original
note = """# Obfuscated with PyObfuscate
# https://www.github.com/htr-tech
# Time : %s
# --------------------------------""" 

# Convertendo para hexadecimal
encoded_note = "".join(f"\\x{hex(ord(c))[2:].zfill(2)}" for c in note)

print(encoded_note)

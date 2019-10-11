def encrypt_vigerene(plaintext: str, keyword: str) -> str:
	"""
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
	ciphertext = ''
	shift = []
	for i in range(len(keyword)):
		if keyword[i].isupper():
			shift.append(ord(keyword[i] - 65))
		elif keyword[i].islower():
			shift.append(ord(keyword[i] - 97))
		else:
			print("Ошибка!")

	if len(keyword) < len(plaintext):
		shift *= len(plaintext) // len(keyword) + 1

	for i in range(len(plaintext)):
		if plaintext[i].isupper():
			if (ord(plaintext[i]) - 65) + shift[i] > 25:
				ciphertext += chr(ord(palintext[i]) + shift[i] - 26)
			else:
				ciphertext += chr(ord(palintext[i]) + shift[i])
		elif plaintext[i].islower():
			if (ord(plaintext[i]) - 97) + shift[i] > 25:
				ciphertext += chr(ord(palintext[i]) + shift[i] - 26)
			else:
				ciphertext += chr(ord(palintext[i]) + shift[i])
		else:
			ciphertext += plaintext[i]
	return ciphertext


def decrypt_vigerene(ciphertext: str, keyword: str) -> str:
	"""
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
	ciphertext = ""
	shift = []
	for i in range(len(keyword)):
		if keyword[i].isupper():
			shift.append(ord(keyword[i]))
		elif keyword[i].islower():
			shift.append(ord(keyword[i]))
		else:
			print("Ошибка!")

	if len(keyword) < len(ciphertext):
		shift *= len(ciphertext) // len(keyword) + 1

	for i in range(len(ciphertext)):
		if ciphertext[i].isupper():
			if (ord(ciphertext) - 65) - shift[i] < 0:
				plaintext += chr(ord(ciphertext[i]) - shift[i] + 26)
			else:
				plaintext += chr(ord(ciphertext[i]) - shift[i])
		elif ciphertext[i].islower():
			if (ord(ciphertext[i]) - 97) - shift[i] < 0:
				plaintext += chr(ord(ciphertext[i]) - shift[i] + 26)
			else:
				plaintext += chr(ord(ciphertext[i]) - shift[i])
		else:
			plaintext += ciphertext[i]
	return plaintext
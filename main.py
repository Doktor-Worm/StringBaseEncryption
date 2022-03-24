import base64

f = open('base64encrypted.txt', 'w')

fullstrig = input("Enter string")
encryptedp1 = fullstrig.encode("ascii")

encryptp2 = base64.b64encode(encryptedp1)
finalencrypt = encryptp2.decode("ascii")

f.write(finalencrypt)
print("All done!")
secondprotocol = input()

dc1 = finalencrypt.encode("ascii")
dc2 = base64.b64decode(dc1)
dcf = dc2.decode("ascii")
d = open('decryptedFile.txt', 'w')
d.write(dcf)

c = open('base32Encrpytion.txt', 'w')
cc1 = base64.b32encode(encryptedp1)
fcf = cc1.decode("ascii")
c.write(fcf)

e = open('Base85encrypt.txt', 'w')
ec1 = base64.b85encode(encryptedp1)
fef = ec1.decode("ascii")
e.write(fef)

h = open('HexadecimalEncrypt.txt', 'w')
hc1 = base64.b16encode(encryptedp1)
fhf = hc1.decode("ascii")
h.write(fhf)


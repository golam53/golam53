import hashlib

filename = "testfile.txt"

def get_file_hash(file):
    with open(file, "rb") as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

current_hash = get_file_hash(filename)

print("File:", filename)
print("SHA256:", current_hash)
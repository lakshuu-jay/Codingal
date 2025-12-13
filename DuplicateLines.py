outputFile = open("UpdatedFile.txt", "w")
inputFile = open("Repeated.txt", "r")

lines_seen_so_far = set()

print("Eliminating duplicate lines....")

for line in inputFile:
    clean = line.strip()
    if line not in lines_seen_so_far:
        outputFile.write(clean)
        lines_seen_so_far.add(clean)

inputFile.close()
outputFile.close()
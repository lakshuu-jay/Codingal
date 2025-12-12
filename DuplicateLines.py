outputFile = open("UpdatedFile.txt", "w")
inputFile = open("Repeated.txt", "r")

lines_seen = set()

print("Eliminating duplicate lines....")

for line in inputFile:
    clean = line.strip()
    if clean not in lines_seen:
        outputFile.write(line)
        lines_seen.add(clean)

inputFile.close()
outputFile.close()
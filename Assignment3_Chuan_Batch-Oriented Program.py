#Assignment_3 Batch-Oriented Program


def main():
    # gets the names of the file
    infileName = input("Enter a .dat file: ")
    outfileName = input("Enter a new .dat file: ")

    # opens the input file
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # processes each line of the input file (loop)
    for line in infile:

        # get the first and last names and also the score from line
        first, last, score = line.split()

        # converts the scores
        index = int(score)/10

        # grades is a list used as a look up table
        Agrade = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

        # gets the letter of the grade 
        grade = Agrade[int(index)]


        # creates the students names with their score and grade
        sname = (first + " " + last + " " + "receives a score of" + " " + score + " " + "for a grade of" + " " + grade + ".\n")
 
        # write it to the output file
        print(sname, file=outfile)

        print(sname)

    # close both files
    infile.close()
    outfile.close()

    print("New file have been written to", outfileName)

main()

# Assignment 3 - Boundary Analysis
# Given a text file that contains upper and lower limits, determine if all points
# within the text file are within the boundary
# Completed/Developed by Valerie Morin on November 16, 2021

import os.path


def main():

    # Get the file path from the user,
    # find the limits in the file,
    # and check if points are contained within bounds.
    while True:
        file_path = get_user_file()
        limits = get_limits(file_path)
        print_boundary_analysis(file_path, limits)

        # User can check as many files as they would like
        continue_flag = input("Would you like to continue? (YES or NO): ")
        if continue_flag[0].upper() == 'N':
            break


# This function prompts a user for an existing file
def get_user_file():
    while True:
        user_file = input("Please select a file to process: ")
        if os.path.isfile(user_file):
            return user_file
        else:
            print("The file entered does not exist.")


# returns limits in this order (LLX, LLY, ULX, ULY)
def get_limits(file_path):

    limits = []
    file = open(file_path, 'r')

    line1 = file.readline().split(",")
    line2 = file.readline().split(",")

    # Lower limit may be on either the first or second line of file
    if line1[0] == "Lower Limit":
        limits.append(float(line1[1].strip(" ").strip("\n")))
        limits.append(float(line1[2].strip(" ").strip("\n")))
        limits.append(float(line2[1].strip(" ").strip("\n")))
        limits.append(float(line2[2].strip(" ").strip("\n")))
    else:
        limits.append(float(line2[1].strip(" ").strip("\n")))
        limits.append(float(line2[2].strip(" ").strip("\n")))
        limits.append(float(line1[1].strip(" ").strip("\n")))
        limits.append(float(line1[2].strip(" ").strip("\n")))

    file.close()
    return limits


# This function performs, writes, and prints the boundary analysis done with the points in user-specified file
def print_boundary_analysis(file_path, limits):

    infile = open(file_path, 'r')
    outfile = open(file_path[:-4] + "_result" + file_path[-4:], 'w')

    lower_lim_x = limits[0]
    lower_lim_y = limits[1]
    upper_lim_x = limits[2]
    upper_lim_y = limits[3]

    point_count = 0
    valid_point_count = 0

    # Skipping the lower/upper limit lines
    infile.readline()
    infile.readline()

    print("\nProcessing file: %s" % file_path)
    print("Output will be written to %s" % (file_path[:-4] + "_result" + file_path[-4:]))
    print("\n------------------------------------------------------")
    print("coordinates (%5.1f, %5.1f) - are Lower Limits." % (lower_lim_x, lower_lim_y))
    print("coordinates (%5.1f, %5.1f) - are Upper Limits." % (upper_lim_x, upper_lim_y))
    print("------------------------------------------------------")

    outfile.write("Processing file: %s\n" % file_path)
    outfile.write("Output will be written to %s\n" % (file_path[:-4] + "_result" + file_path[-4:]))
    outfile.write("\n------------------------------------------------------\n")
    outfile.write("coordinates ( %5.1f,  %5.1f) - are Lower Limits.\n" % (lower_lim_x, lower_lim_y))
    outfile.write("coordinates ( %5.1f,  %5.1f) - are Upper Limits.\n" % (upper_lim_x, upper_lim_y))
    outfile.write("------------------------------------------------------\n")

    for line in infile:

        point_count += 1

        point_x = float(line.split(',')[1])
        point_y = float(line.split(',')[2])

        # Check if points are above or below boundaries

        if point_x < lower_lim_x:
            if point_y < lower_lim_y:
                boundary_check_string = "X value is LOW and Y value is LOW."
            elif point_y > upper_lim_y:
                boundary_check_string = "X value is LOW and Y value is HIGH."
            else:
                boundary_check_string = "X value is LOW."
        elif point_x > upper_lim_x:
            if point_y < lower_lim_y:
                boundary_check_string = "X value is HIGH and Y value is LOW."
            elif point_y > upper_lim_y:
                boundary_check_string = "X value is HIGH and Y value is HIGH."
            else:
                boundary_check_string = "X value is HIGH."
        else:
            if point_y < lower_lim_y:
                boundary_check_string = "Y Value is LOW."
            elif point_y > upper_lim_y:
                boundary_check_string = "Y Value is HIGH."
            else:
                boundary_check_string = "is okay."
                valid_point_count += 1

        print("Pair:( %5.1f, %5.1f) - %s" % (point_x, point_y, boundary_check_string))
        outfile.write("Pair: (%5.1f, %5.1f) - %s\n" % (point_x, point_y, boundary_check_string))

    print("\nSummary")
    print("======================================================")
    print("There were %d vertices in the data." % point_count)
    print("\t\t- %d points were inside the boundary." % valid_point_count)
    print("\t\t- %d points were outside the boundary.\n" % (point_count - valid_point_count))

    outfile.write("\nSummary\n")
    outfile.write("======================================================\n")
    outfile.write("There were %d vertices in the data.\n" % point_count)
    outfile.write("\t\t- %d points were inside the boundary.\n" % valid_point_count)
    outfile.write("\t\t- %d points were outside the boundary.\n" % (point_count - valid_point_count))

    infile.close()
    outfile.close()


main()

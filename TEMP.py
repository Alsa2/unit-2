# Thruth table generator

def get_truth():
    truth = []
    print("| A | B | C |")
    for i in range(8):
        truth.append([i//4, (i//2)%2, i%2])
        print("|", truth[i][0], "|", truth[i][1], "|", truth[i][2], "|")
get_truth()
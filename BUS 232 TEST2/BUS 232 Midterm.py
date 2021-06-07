total_shares = 0
all_shares = list()
index = 0

def holdShares():
    global total_shares,all_shares
    share = int(input("Please enter the number of shares: "))
    all_shares.append(share)

    while(share != 0):
        total_shares += share
        share = int(input("Please enter the number of shares: "))
        if share != 0:
            all_shares.append(share)

def reverseSortList(the_list):
    return list(sorted(the_list, reverse = True))

def findSupportedNumber():
    global index
    tmp_total_shares = 0
    tmp_total_shares += sorted_all_shares[index]
    while(tmp_total_shares < int(total_shares/2)+1):
        index += 1
        tmp_total_shares += sorted_all_shares[index]

def printResults(total,rank):
    print("Thank you, there is a total of " + str(total)+ " shares represented here.")
    print("Shared needed for majority vote is " + str(int(total/2)+1))
    print("You need the support of top "+ str(rank+1) + " shareholders for this number of votes.")

def writeResultsToTxt(total,rank):
    with open("copy.txt", "w") as file:
        file.write("Thank you, there is a total of " + str(total)+ " shares represented here.\n")
        file.write("Shared needed for majority vote is " + str(int(total/2)+1) + "\n")
        file.write("You need the support of top "+ str(rank+1) + " shareholders for this number of votes.")

holdShares()
sorted_all_shares = reverseSortList(all_shares)
findSupportedNumber()
printResults(total_shares,index)
writeResultsToTxt(total_shares,index)
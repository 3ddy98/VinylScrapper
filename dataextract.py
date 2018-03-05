import csv

def main():
    with open('Rock Vinyl - #.csv', 'a') as Rock:
        fieldnames = ['Artist','Vinyl','Date Checked','Condition','Catalogue #','Year Released','Label','Discog Link']
        writer= csv.writer(Rock, delimiter=',')
        data = ['test1','test2','test3','test4','test5','test6','test7','test8']
        writer.writerow(data)



if __name__ == "__main__":
    main()

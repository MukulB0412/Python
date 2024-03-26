questions = [   
    [
        'The International Literacy Day is observed on','Sep 8','Nov 28','May 2','Sep 22',1
    ],
    [
         'The language of Lakshadweep. a Union Territory of India, is','Tamil','Hindi','Malayalam','Telegu',3
    ],
    [
        ' Bahubali festival is related to','Islam','Hindusim','Buddhism','Jainsm',4
    ],
    [
        'Which day is observed as the World Standards  Day?','June 26','14 Oct', 'Nov 15', 'Dec 2',2
    ],
    [
        'September 27 is celebrated every year as','Teachers Day','National Integration Day','World Tourism','International Literacy Day',3
    ],
    [
        'Who is the author of "Manas Ka-Hans" ?','Khushwant Singh','Prem Chand','Jayashankar Prasad','Amrit Lal Nagar',4
    ],
    [
        'The death anniversary of which of the following leaders is observed as Martyrs Day?',' Smt. Indira Gandhi',' PI. Jawaharlal Nehru',' Mahatma Gandhi',' Lal Bahadur Shastri',3
    ],
    [
        'Who is the author of the epic "Meghdoot"?',' Vishakadatta',' Valmiki','Banabhatta','Kalidas',4
    ],
    [
         'Which of the following is observed as Sports Day every year?',' 22nd April',' 26th  july',' 29th August',' 2nd October',3
    ],
    [
        'World Health Day is observed on',' Apr 7',' Mar 6',' Mat I5',' Apr 28',1
    ],
]

levels = [1000,2000,5000,10000,20000,40000,80000,160000,320000,640000]
prizemoney = 0
for i in range(0 , len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f'c. {question[3]}     d. {question[4]}')
    reply = int(input(" Enter the correct answer (1-4) or 0 to quit:\n"))

    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 3):
            prizemoney = 10000
        elif( i == 8):
            prizemoney = 320000
        elif(i == 9):
           prizemoney = 640000       
    else:
        print("Wrong Answer")
        break
print(f"Your take home money is {prizemoney}")


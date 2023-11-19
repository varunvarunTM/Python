""" A word is said to be perfect if it satisfies all the following criteria:

    (1) All the vowels (a,e,i,o,u) should be present in the word.

    (2) Let the vowels be represented as 
                                     v(1) = a
                                     v(2) = e
                                     v(3) = i
                                     v(4) = o
                                     v(5) = u 
                                              in lexical order.
    If i < j, then the first appearance of v(i) in the word should come
    before the first appearance of v(j).
    If i < j , then the count of v(i) should be greater than or equal to the count of v(j).
    
    Accept a word as input and do the following:
    
    (1) If it is a perfect word, print It is a perfect word
    
    (2) If the word is not a perfect word, print It is not a perfect word """
 



x = input()
a = (x.find("a") >= 0) and (x.find("e") >= 0) and (x.find("i") >= 0) and (x.find("o") >= 0) and (x.find("u") >= 0) and (x.find("a") < x.find("e") < x.find("i") < x.find("o") < x.find("u")) and (x.count("a") >= x.count("e") >= x.count("i") >= x.count("o") >= x.count("u"))
if a == True:
    print("It is a perfect word")
else:
    print("It is not a perfect word")
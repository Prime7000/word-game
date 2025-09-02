import nltk
from nltk.corpus import wordnet
import random
from nltk.corpus import words
import math
import time

def random_func(num_of_letters = 4):
    while True:
        all_words = list(words.words())
        random_word = random.choice(all_words)
        length = len(random_word)
        if length <= num_of_letters:
            break
    random_word = random.sample(list(random_word),len(random_word))
    random_word = "".join(random_word)
    return random_word

def possible_combinations(word,fac,count):
    w = word
    # count = len(w)
    partial_bank = []
    main_bank = {}
    main_bank_count = 0
    # fac = math.factorial(count)
    
    while main_bank_count != fac:
        ran = random.sample(w,count)
        gen_word = "".join(ran).lower()
        # print(gen_word)
    
        partial_bank.append(gen_word)
        main_bank = set(partial_bank)
        unique_words = len(main_bank)
        # print(f'-----Unique words {unique_words}')
        main_bank_count = len(main_bank)
        # time.sleep(0.1)
    
    # print('number of unique words', main_bank_count)
    return list(main_bank)

# all possible combinations
def all_possible_combinations(w):
    word = w
    l = len(word)
    total_words = []
    num_of_words = 2 #start predicting from two letter words
    for i in range(num_of_words,l+1):
        perm = math.perm(len(word),i)
        # print(perm,f'perm of {i}')
        pc = possible_combinations(word,perm,i)
        total_words = total_words + pc
    return total_words
        

# function for checking if a word is present in the dic
def validator(x):
    the_list = x
    meaningful_words = []
    for i in the_list:
        if wordnet.synsets(i):
            meaningful_words.append(i)
    return meaningful_words
            

total_questions_asked = 1

while True:
    w = random_func()
    # print(f'random_word:{w}')
    combo = all_possible_combinations(w)
    # print(f'all possible combination: {combo}')
    meaningful_words = validator(combo)
    print('-------------------------------------------')
    # print(meaningful_words)
    
    #making sure the algorithm does not tell you
    # to insert more than the possible combination available
    
    count_meaningful_words = len(meaningful_words)
    print('''
    ''')
    human_ans = []
    num_of_predictions = 4 #number of words users must predict
    if count_meaningful_words >= num_of_predictions:
        print(f'Derive 4 words from this word {w}')
        questions_answered = 0
        while True:
            human_feedback = input('Insert derived words: ').lower()
            if human_feedback in meaningful_words and human_feedback not in human_ans:
                human_ans.append(human_feedback)
    
                questions_answered = questions_answered + 1
                print(f'--correct you have answered {questions_answered} out of {num_of_predictions}')
    
                if len(human_ans) == num_of_predictions:
                    break
            else:
                print('----wrong-----')
    else:
        # print(f'Derive {len(count_meaningful_words)} words from this word {w}')
        break

    end_ = input('Do you want to keep playing yes/no? ').lower()
    if end_ == 'yes':
        pass
    elif end_ == 'no':
        break
    else:
        print('invalid input')

    total_questions_asked = total_questions_asked + 1

print('______Game ended____')
print(f'you played {total_questions_asked} sections')
        
        
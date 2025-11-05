# #Excercise 1 Q1 - Q4
# # sets
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# set_length = len(it_companies)
# print(set_length)

# it_companies.add("Twitter")
# print(it_companies)

# it_companies.update(["Samsung", "Flipkart"])
# print(it_companies)

# it_companies.remove("Facebook")
# print(it_companies)

# #Q5
# it_companies.remove("Samsung")
# it_companies.discard("Samsung")
# print(it_companies)

# #Excercise 2 Q1 - Q7
# # sets
# A = {19, 22, 24, 20, 25, 26}
# B = {19, 22, 20, 25, 26, 24, 28, 27}
# A_and_B = A.union(B)
# print(A_and_B)

# A_inter_B = A.intersection(B)
# print(A_inter_B)

# is_subset = A.issubset(B)
# print(is_subset)

# is_disjoint_A = A.isdisjoint(B)
# print(is_disjoint_A)

# print(A_and_B)
# B_and_A = B.union(A)
# print(B_and_A)

# symm_diff = A.symmetric_difference(B)
# print(symm_diff)

# del A
# del B
# print(A)

# #Excercise 3 Q1
# # sets
# age = [22, 19, 24, 25, 26, 24, 25, 24]
# age_set = set(age)

# len_lst_age = len(age)
# len_lst_set = len(age_set)
# comparison = len_lst_age > len_lst_set
# print(comparison)

# #Q2
# string = "Hi"
# list = ["Hi", "Guys"]
# tuple = ("Hello", "Guys")
# set = {"Whatsup", "Guys"}

#Q3
# sentence = "I am a teacher and I love to inspire and teach people."
# print("Original Sentence:", sentence)

# # Step 2: Clean the sentence (lowercase and remove punctuation)
# cleaned_sentence = sentence.lower().replace('.', '')
# print("Cleaned Sentence:", cleaned_sentence)

# # Step 3: Split into a list of words
# words = cleaned_sentence.split(' ')
# print("List of all words:", words)

# # Step 4: Convert the list to a set to get unique words
# unique_words = set(words)
# print("Set of unique words:", unique_words)

# # Step 5: Count the number of unique words
# num_unique_words = len(unique_words)
# print(f"\nThe number of unique words used in the sentence is: {num_unique_words}")

sen = "I am a teacher and I love to inspire and teach people."
sen_slice = sen.split(" ")
print(sen_slice)
sen_set = set(sen_slice)
print(sen_set)
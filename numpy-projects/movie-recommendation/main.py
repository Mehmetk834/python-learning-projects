"""
NumPy Kullanarak Film Öneri Sistemi

Kullanıcılar sisteme kullanıcı adı ve şifre ile giriş yapar.
Giriş yapan kullanıcının film puanları diğer kullanıcılarla
kosinüs benzerliği kullanılarak karşılaştırılır.

En çok benzeyen kullanıcı bulunur ve onun izlediği fakat
giriş yapan kullanıcının izlemediği filmler önerilir.
"""

import numpy as np

movies = ["Titanic", "Matris", "Interstellar", "Batman", "Avatar"]

ratings = np.array([
    [5,4,0,0,3],
    [5,0,4,0,0],
    [0,4,5,3,0],
    [0,0,4,5,4]
])

users = ["Kullanıcı 1", "Kullanıcı 2", "Kullanıcı 3", "Kullanıcı 4"]

usernames = ["kullanici1", "kullanici2", "kullanici3", "kullanici4"]
passwords = ["123", "456", "789", "abc"]

print("=== Film Öneri Sistemine Hoş Geldiniz ===\n")

username_input = input("Kullanıcı adınızı girin: ")
password_input = input("Şifrenizi girin: ")

if username_input in usernames:

    user_index = usernames.index(username_input)

    if passwords[user_index] == password_input:
        print("\nGiriş başarılı!\n")
        target_user_index = user_index
        target_user = ratings[target_user_index]

    else:
        print("Şifre yanlış!")
        exit()

else:
    print("Kullanıcı bulunamadı!")
    exit()


def cosine_similarity(a, b):

    dot_product = np.dot(a, b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    similarity = dot_product / (norm_a * norm_b)

    return similarity


similarities = []

for user in ratings:
    result = cosine_similarity(target_user, user)
    similarities.append(result)

similarities = np.array(similarities)

similarities[target_user_index] = 0

most_similar_user = np.argmax(similarities)


recommended_movies = []

for i in range(len(movies)):
    if target_user[i] == 0 and ratings[most_similar_user][i] > 0:
        recommended_movies.append(movies[i])


print("Size en çok benzeyen kullanıcı:", users[most_similar_user])

print("\nÖnerilen filmler:")

if len(recommended_movies) == 0:
    print("Size önerilecek yeni film bulunamadı.")
else:
    for movie in recommended_movies:
        print("-", movie)

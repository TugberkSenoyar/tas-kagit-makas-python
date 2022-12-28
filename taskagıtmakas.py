import random

print(("-" * 30) + "\nTaş, Kağıt, Makas\n" + ("-" * 30))

user_score, computer_score = 0, 0

while True:
    print("\n1 - Taş \n2 - Kağıt \n3 - Makas")
    user_choice = input("Sizin Seçiminiz: ")
    computer_choice = random.choice(["1","2","3"])

    if user_choice =="1":
     if computer_choice =="1":
            print("-" * 30)
            print("Bilgisayarın Seçimi Taş \n Taş Taşa Eşittir. Berabere")

     elif computer_choice == "2":
            print("-" * 30)
            print("Bilgisayarın Seçimi Kağıt \n Kağıt Taşı Sarar. Kaybettin 😥")

            computer_score += 100

     elif computer_choice =="3":
             print("-" * 30)
             print("Bilgisayarın Seçimi Makas \nTaş Makası Kırar. Kazandın 🎉")

             user_score += 100

    elif user_choice =="2":
     if computer_choice =="1":
            print("-" * 30)
            print("Bilgisayarın Seçimi Taş  \nKağıt Taşı Sarar. Kazandın! 🎉")
            user_score += 100

     elif computer_choice == "2":
                print("-" * 30)
                print("Bilgisayarın Seçimi Kağıt \nKağıt Kağıt a eşit. Berabere")

     elif computer_choice =="3":
                print("-" * 30)
                print("Bilgisayar Seçimi Makas \n Makas Kağıdı Keser. Kaybettin 😥")
                computer_score += 100

    elif user_choice == "3":
     if computer_choice == "1":
                    print("-" * 30)
                    print("Bilgisayar Seçimi Taş \n Taş Makası Kırar Kaybetin 😥 ")
                    computer_score += 100

     elif computer_choice == "2":
                    print("Bilgisayar Seçimi Kağıt \n Makas Kağıdı Keser. Kazandın 🎉")
                    user_score +=100

     elif computer_choice == "3":
                  print("-" * 30)
                  print("Bilgisayar Seçimi Makas\n Makas Makasa Eşit Berabere")

    else:
                break

    print("\nKullanıcı Puanı : {}\nBilgisayar Puanı : {}".format(user_score, computer_score))
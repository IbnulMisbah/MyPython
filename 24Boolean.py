# Bismillahir Rahmanir Rahim.
# Now I will learn Boolean Operator.
# Jorge Bool made this Operator .
# (==) Equal-Equal,(and) And,(or) Or .
# it's used on Condition.

# Input Taking
i = input('What day is today : ')

# Condition
if i=='friday' or i=='Friday' or i=='satarday' or i=="Sataray" or i=='saturday' or i=='Saturday': 
	print("Today is a enjoyable day")

elif i=='sunday' or i=='Sunday' or i=='monday' or i=='Monday':
	print("\nONNO,Today you have to go to Madrasah.")
	print("Routin : Bangla,Arabic(i),English(ii),H.Math & Biology.\n")

elif i=='tuesday' or i=='Tuesday':
	print('\nONNO ,Today you have to go to Madrasah.')
	print("Routin : Bangla(ii),Chemistry(A),Quran,Physics(M) & Math.\n")

elif i=='wensday' or i=='wednesday' or i=='Wensday' or i=='Wednesday':
    print('\nONNO ,Today you have to go to Madrasah.')
    print("Routin : English(i),Aqaid,Arabic(ii),Physics(S) & Math.\n")

elif i=='thursday' or i=='Thursday':
    print('\nONNO ,Today you have to go to Madrasah.')
    print("Routin : English(i),Chemistry(F),Arabic(ii),Hadith & Math.\n")

else:
	print('Please,Write down with right spell')

score = {
    "Yashasvi_Jaiswal":4,
    "Rhit_Sharma":48,
    "Shubman_Gill":154,
    "Ishan_Kishan":125,
    "Shreyas_Iyer":26,
    "KL_Rahul":0,
    "Washington_Sundar":19,
    "Kuldeep_Yadav":3,
    "Gurnoor_Brar":3,
    "Arshdeep_Singh":3,
    "Prince_Yadav":5
}
max = 0 # 4
name = None 
for player in score:
    if max<score[player]:
        max = score[player]
        name  = player
print("maximum score ",max, " made by ",name)

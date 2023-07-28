import numpy as np
import random


#初期集団の生成
list1 = [0]*100
for i in range(0,100):
    list1[i] = random.randint(1,10)
list2 = np.array(list1).reshape(-1, 10).tolist()
print(f"The first is: {list2}")
print(f"(This is a test) component 0 of list2 is: {list2[0][0:10]}") #各配列の取得

#評価関数の前処理 (各ポケモンのsumを表示)
sum_0=0
for i in range(0, 10):
    sum_0 = sum_0 + list2[0][i]
list_sum_0 = [sum_0, 0]
sum_1=0
for i in range(0,10):
    sum_1 = sum_1 + list2[1][i]
list_sum_1 = [sum_1, 1]
sum_2=0
for i in range(0,10):
    sum_2 = sum_2 + list2[2][i]
list_sum_2 = [sum_2, 2]
sum_3=0
for i in range(0,10):
    sum_3 = sum_3 + list2[3][i]
list_sum_3 = [sum_3, 3]
sum_4=0
for i in range(0,10):
    sum_4 = sum_4 + list2[4][i]
list_sum_4 = [sum_4, 4]
sum_5=0
for i in range(0,10):
    sum_5 = sum_5 + list2[5][i]
list_sum_5 = [sum_5, 5]
sum_6=0
for i in range(0,10):
    sum_6 = sum_6 + list2[6][i]
list_sum_6 = [sum_6, 6]
sum_7=0
for i in range(0,10):
    sum_7 = sum_7 + list2[7][i]
list_sum_7 = [sum_7, 7]
sum_8=0
for i in range(0,10):
    sum_8 = sum_8 + list2[8][i]
list_sum_8 = [sum_8, 8]
sum_9=0
for i in range(0,10):
    sum_9 = sum_9 + list2[9][i]
list_sum_9 = [sum_9, 9]

data= [list_sum_0, list_sum_1, list_sum_2, list_sum_3, list_sum_4, list_sum_5, list_sum_6, list_sum_7, list_sum_8, list_sum_9]
print(f"data: {data}")

sorted_data = sorted(data, reverse=True)
print(f"sorted_data: {sorted_data}")

#選択
ranking_1 = sorted_data[1]
ranking_2 = sorted_data[2]
ranking_3 = sorted_data[3]
ranking_4 = sorted_data[4]

result = [ranking_1, ranking_2, ranking_3, ranking_4]
print(f"result: {result}")

#生き残ったポケモン
ranking_1_pokemon = list2[result[0][1]][0:10]
print(f"ranking_1_pokemon: {ranking_1_pokemon}")
ranking_2_pokemon = list2[result[1][1]][0:10]
print(f"ranking_2_pokemon: {ranking_2_pokemon}")
ranking_3_pokemon = list2[result[2][1]][0:10]
print(f"ranking_3_pokemon: {ranking_3_pokemon}")
ranking_4_pokemon = list2[result[3][1]][0:10]
print(f"ranking_4_pokemon: {ranking_4_pokemon}")

#突然変異
DNA_arr_1 = random.randint(0,9)
print(DNA_arr_1)
mutation_1 = random.randint(1,10)
ranking_1_pokemon[DNA_arr_1] = mutation_1
ranking_1_pokemon_changed = ranking_1_pokemon
print(f"mutated_ranking_1_pokemon: {ranking_1_pokemon_changed}")

DNA_arr_2 = random.randint(0,9)
print(DNA_arr_2)
mutation_2 = random.randint(1,10)
ranking_2_pokemon[DNA_arr_2] = mutation_2
ranking_2_pokemon_changed = ranking_2_pokemon
print(f"mutated_ranking_2_pokemon: {ranking_2_pokemon_changed}")

DNA_arr_3 = random.randint(0,9)
print(DNA_arr_3)
mutation_3 = random.randint(1,10)
ranking_3_pokemon[DNA_arr_3] = mutation_3
ranking_3_pokemon_changed = ranking_3_pokemon
print(f"mutated_ranking_3_pokemon: {ranking_3_pokemon_changed}")

DNA_arr_4 = random.randint(0,9)
print(DNA_arr_4)
mutation_4 = random.randint(1,10)
ranking_4_pokemon[DNA_arr_4] = mutation_4
ranking_4_pokemon_changed = ranking_4_pokemon
print(f"mutated_ranking_4_pokemon: {ranking_4_pokemon_changed}")

DNA_arr_11 = random.randint(0,9)
print(DNA_arr_11)
mutation_11 = random.randint(1,10)
ranking_1_pokemon_changed[DNA_arr_11] = mutation_11
ranking_11_pokemon_changed = ranking_1_pokemon
print(f"mutated_ranking_11_pokemon: {ranking_11_pokemon_changed}")

DNA_arr_12 = random.randint(0,9)
print(DNA_arr_12)
mutation_12 = random.randint(1,10)
ranking_2_pokemon_changed[DNA_arr_12] = mutation_12
ranking_12_pokemon_changed = ranking_2_pokemon_changed
print(f"mutated_ranking_12_pokemon: {ranking_12_pokemon_changed}")

result = [ranking_1_pokemon, ranking_2_pokemon, ranking_3_pokemon, ranking_4_pokemon, ranking_1_pokemon_changed, ranking_2_pokemon_changed, ranking_3_pokemon_changed, ranking_4_pokemon_changed, ranking_11_pokemon_changed, ranking_12_pokemon_changed]
print(f"result: {result}")
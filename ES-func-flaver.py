import numpy as np
import random
import matplotlib.pyplot as plt


def ES(list2):
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
    sorted_data = sorted(data, reverse=True)

    #選択
    ranking_1 = sorted_data[0]
    ranking_2 = sorted_data[1]
    ranking_3 = sorted_data[2]
    ranking_4 = sorted_data[3]

    selected_result = [ranking_1, ranking_2, ranking_3, ranking_4]

    #生き残ったポケモン
    ranking_1_pokemon = list2[selected_result[0][1]][0:10]
    ranking_2_pokemon = list2[selected_result[1][1]][0:10]
    ranking_3_pokemon = list2[selected_result[2][1]][0:10]
    ranking_4_pokemon = list2[selected_result[3][1]][0:10]


    ranking_1_pokemon_changed = []
    ranking_2_pokemon_changed = []
    ranking_3_pokemon_changed = []
    ranking_4_pokemon_changed = []
    ranking_11_pokemon_changed = []
    ranking_12_pokemon_changed = []
    #突然変異
    DNA_arr_1 = random.randint(0,9)
    mutation_1 = random.randint(1,10)
    ranking_1_pokemon_changed = ranking_1_pokemon[:]
    ranking_1_pokemon_changed[DNA_arr_1] = mutation_1

    DNA_arr_2 = random.randint(0,9)
    mutation_2 = random.randint(1,10)
    ranking_2_pokemon_changed = ranking_2_pokemon[:]
    ranking_2_pokemon_changed[DNA_arr_2] = mutation_2

    DNA_arr_3 = random.randint(0,9)
    mutation_3 = random.randint(1,10)
    ranking_3_pokemon_changed = ranking_3_pokemon[:]
    ranking_3_pokemon_changed[DNA_arr_3] = mutation_3

    DNA_arr_4 = random.randint(0,9)
    mutation_4 = random.randint(1,10)
    ranking_4_pokemon_changed = ranking_4_pokemon[:]
    ranking_4_pokemon_changed[DNA_arr_4] = mutation_4

    DNA_arr_11 = random.randint(0,9)
    mutation_11 = random.randint(1,10)
    ranking_11_pokemon_changed = ranking_1_pokemon[:]
    ranking_11_pokemon_changed[DNA_arr_11] = mutation_11

    DNA_arr_12 = random.randint(0,9)
    mutation_12 = random.randint(1,10)
    ranking_12_pokemon_changed = ranking_2_pokemon[:]
    ranking_12_pokemon_changed[DNA_arr_12] = mutation_12

    result = [ranking_1_pokemon, ranking_2_pokemon, ranking_3_pokemon, ranking_4_pokemon, ranking_1_pokemon_changed, ranking_2_pokemon_changed, ranking_3_pokemon_changed, ranking_4_pokemon_changed, ranking_11_pokemon_changed, ranking_12_pokemon_changed]
    return result


#初期集団の生成
list2 = [[random.randint(1, 10) for _ in range(10)] for _ in range(10)]


#Rank_1
def plot_graph_1(list2):
    sum_0=0
    for i in range(0, 10):
        sum_0 = sum_0 + list2[0][i]
    sum_1=0
    for i in range(0,10):
        sum_1 = sum_1 + list2[1][i]
    sum_2=0
    for i in range(0,10):
        sum_2 = sum_2 + list2[2][i]
    sum_3=0
    for i in range(0,10):
        sum_3 = sum_3 + list2[3][i]
    sum_4=0
    for i in range(0,10):
        sum_4 = sum_4 + list2[4][i]
    sum_5=0
    for i in range(0,10):
        sum_5 = sum_5 + list2[5][i]
    sum_6=0
    for i in range(0,10):
        sum_6 = sum_6 + list2[6][i]
    sum_7=0
    for i in range(0,10):
        sum_7 = sum_7 + list2[7][i]
    sum_8=0
    for i in range(0,10):
        sum_8 = sum_8 + list2[8][i]
    sum_9=0
    for i in range(0,10):
        sum_9 = sum_9 + list2[9][i]
    sum = [sum_0, sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9]
    sorted_sum_data = sorted(sum, reverse=True)
    ranking_1 = sorted_sum_data[0]
    return ranking_1

#Rank_2
def plot_graph_2(list2):
    sum_0=0
    for i in range(0, 10):
        sum_0 = sum_0 + list2[0][i]
    sum_1=0
    for i in range(0,10):
        sum_1 = sum_1 + list2[1][i]
    sum_2=0
    for i in range(0,10):
        sum_2 = sum_2 + list2[2][i]
    sum_3=0
    for i in range(0,10):
        sum_3 = sum_3 + list2[3][i]
    sum_4=0
    for i in range(0,10):
        sum_4 = sum_4 + list2[4][i]
    sum_5=0
    for i in range(0,10):
        sum_5 = sum_5 + list2[5][i]
    sum_6=0
    for i in range(0,10):
        sum_6 = sum_6 + list2[6][i]
    sum_7=0
    for i in range(0,10):
        sum_7 = sum_7 + list2[7][i]
    sum_8=0
    for i in range(0,10):
        sum_8 = sum_8 + list2[8][i]
    sum_9=0
    for i in range(0,10):
        sum_9 = sum_9 + list2[9][i]
    sum = [sum_0, sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9]
    sorted_sum_data = sorted(sum, reverse=True)
    ranking_2 = sorted_sum_data[1]
    return ranking_2

#Rank_3
def plot_graph_3(list2):
    sum_0=0
    for i in range(0, 10):
        sum_0 = sum_0 + list2[0][i]
    sum_1=0
    for i in range(0,10):
        sum_1 = sum_1 + list2[1][i]
    sum_2=0
    for i in range(0,10):
        sum_2 = sum_2 + list2[2][i]
    sum_3=0
    for i in range(0,10):
        sum_3 = sum_3 + list2[3][i]
    sum_4=0
    for i in range(0,10):
        sum_4 = sum_4 + list2[4][i]
    sum_5=0
    for i in range(0,10):
        sum_5 = sum_5 + list2[5][i]
    sum_6=0
    for i in range(0,10):
        sum_6 = sum_6 + list2[6][i]
    sum_7=0
    for i in range(0,10):
        sum_7 = sum_7 + list2[7][i]
    sum_8=0
    for i in range(0,10):
        sum_8 = sum_8 + list2[8][i]
    sum_9=0
    for i in range(0,10):
        sum_9 = sum_9 + list2[9][i]
    sum = [sum_0, sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9]
    sorted_sum_data = sorted(sum, reverse=True)
    ranking_3 = sorted_sum_data[2]
    return ranking_3

#Rank_4
def plot_graph_4(list2):
    sum_0=0
    for i in range(0, 10):
        sum_0 = sum_0 + list2[0][i]
    sum_1=0
    for i in range(0,10):
        sum_1 = sum_1 + list2[1][i]
    sum_2=0
    for i in range(0,10):
        sum_2 = sum_2 + list2[2][i]
    sum_3=0
    for i in range(0,10):
        sum_3 = sum_3 + list2[3][i]
    sum_4=0
    for i in range(0,10):
        sum_4 = sum_4 + list2[4][i]
    sum_5=0
    for i in range(0,10):
        sum_5 = sum_5 + list2[5][i]
    sum_6=0
    for i in range(0,10):
        sum_6 = sum_6 + list2[6][i]
    sum_7=0
    for i in range(0,10):
        sum_7 = sum_7 + list2[7][i]
    sum_8=0
    for i in range(0,10):
        sum_8 = sum_8 + list2[8][i]
    sum_9=0
    for i in range(0,10):
        sum_9 = sum_9 + list2[9][i]
    sum = [sum_0, sum_1, sum_2, sum_3, sum_4, sum_5, sum_6, sum_7, sum_8, sum_9]
    sorted_sum_data = sorted(sum, reverse=True)
    ranking_3 = sorted_sum_data[3]
    return ranking_3

gen = 1
lists = []
plot_lists_1 = []
plot_lists_2 = []
plot_lists_3 = []
plot_lists_4 = []

while gen <= 100:
    list2 = ES(list2)
    gen = gen + 1
    print(f"Generation_{gen}: {list2}")

    #グラフの描画
    plot_1 = plot_graph_1(list2)
    plot_lists_1.append(plot_1)
    print(f"lists_{gen}: {plot_lists_1}")

    plot_2 = plot_graph_2(list2)
    plot_lists_2.append(plot_2)
    print(f"lists_{gen}: {plot_lists_2}")

    plot_3 = plot_graph_3(list2)
    plot_lists_3.append(plot_3)
    print(f"lists_{gen}: {plot_lists_3}")

    plot_4 = plot_graph_4(list2)
    plot_lists_4.append(plot_4)
    print(f"lists_{gen}: {plot_lists_4}")

    print("End!")



gen_number = list(range(1,101,1))

fig, ax = plt.subplots()
ax.set_xlabel('Generation')
ax.set_ylabel('Total Score')
ax.set_title('Evolution Strategy')

ax.plot(gen_number, plot_lists_1, label="1st")
ax.plot(gen_number, plot_lists_2, label="2nd")
ax.plot(gen_number, plot_lists_3, label="3rd")
ax.plot(gen_number, plot_lists_4, label="4th")

ax.legend(loc=0)
fig.tight_layout()

plt.show()
import matplotlib.pyplot as plt

diabetes_file = open("diabetes.data", "r")
diabetes_list = [record.strip().split(";") for record in diabetes_file]

def plot1():
    dbp90_age_list = [item for item in diabetes_list if float(item[2]) >= 90]

    pregnancy_age = [int(i[0]) / int(i[7]) for i in dbp90_age_list]
    bodyMass_age = [float(i[5]) / int(i[7]) for i in dbp90_age_list]
    copy_pregnancy_age = [int(i[0]) / int(i[7]) for i in dbp90_age_list]
    copy_bodyMass_age = [float(i[5]) / int(i[7]) for i in dbp90_age_list]
    for i in copy_pregnancy_age:
        if i == 0.0:
            pregnancy_age.remove(i)
    for j in copy_bodyMass_age:
        if j == 0.0:
            bodyMass_age.remove(j)

    max_pregnancy_age, min_pregnancy_age = max(pregnancy_age), min(pregnancy_age)
    max_bodyMass_age, min_bodyMass_age = max(bodyMass_age), min(bodyMass_age)
    for i in copy_pregnancy_age:
        if i == max_pregnancy_age:
            max_p_index = copy_pregnancy_age.index(i)
        elif i == min_pregnancy_age:
            min_p_index = copy_pregnancy_age.index(i)
    max_p_age = int(dbp90_age_list[max_p_index][7])
    min_p_age = int(dbp90_age_list[min_p_index][7])
    print(min_p_index)
    print(min_p_age)
    for j in copy_bodyMass_age:
        if j == max_bodyMass_age:
            max_b_index = copy_bodyMass_age.index(j)
        elif j == min_bodyMass_age:
            min_b_index = copy_bodyMass_age.index(j)
    max_b_age = int(dbp90_age_list[max_b_index][7])
    min_b_age = int(dbp90_age_list[min_b_index][7])

    y_axis = [int(i[7]) for i in dbp90_age_list]
    min_age = min(y_axis) // 10 * 10
    max_age = max(y_axis)
    x_axis = [i for i in range(len(dbp90_age_list))]
    plt.plot(x_axis, y_axis, color='b')
    plt.xticks([i for i in range(1, len(dbp90_age_list), 5)])
    plt.yticks([i for i in range(min_age, max_age, 10)])
    plt.xlabel('Instances')
    plt.ylabel('Ages')

    plt.annotate('max(#pregnancy/age)',
                 xy=(max_p_index, max_p_age), xycoords='data',
                 xytext=(45, 5), textcoords='offset points',
                 arrowprops=dict(facecolor='red'),
                 horizontalalignment='left', verticalalignment='bottom')
    plt.annotate('min(#pregnancy/age)',
                 xy=(min_p_index, min_p_age), xycoords='data',
                 xytext=(20, 40), textcoords='offset points',
                 arrowprops=dict(facecolor='red'),
                 horizontalalignment='left', verticalalignment='bottom')
    plt.annotate('max(#Body mass index/age)',
                 xy=(max_b_index, max_b_age), xycoords='data',
                 xytext=(10, 15), textcoords='offset points',
                 arrowprops=dict(facecolor='green'),
                 horizontalalignment='center', verticalalignment='bottom')
    plt.annotate('min(#Body mass index/age)',
                 xy=(min_b_index, min_b_age), xycoords='data',
                 xytext=(-20, 10), textcoords='offset points',
                 arrowprops=dict(facecolor='green'),
                 horizontalalignment='left', verticalalignment='bottom')
    #plt.show()
    plt.savefig("Fig1.pdf")
    plt.close()

def plot2():
    xbirth_years = {2017 - int(i[7]) for i in diabetes_list}
    xbirth_years = sorted(xbirth_years)
    xyear_count = {i: [] for i in xbirth_years}
    deneme = [i for i in range(1, (len(xbirth_years) + 1))]
    denemeplus = [i + 0.20 for i in deneme]
    for i in diabetes_list:
        xyear_count[2017 - int(i[7])].append(i[8])

    diabetes = [xyear_count[i].count("1") for i in xyear_count]
    nondiabetes = [xyear_count[i].count("0") for i in xyear_count]

    plt.bar(deneme, diabetes, 0.20, color='b')
    plt.bar(denemeplus, nondiabetes, 0.20, color='r')
    plt.legend(['Diabete', 'Not-Diabete'])
    plt.xlabel('Years')
    plt.ylabel('# of patients')
    plt.xticks([i for i in deneme], xbirth_years, rotation=75, fontsize=6)
    #plt.show()
    plt.savefig("Fig2.pdf")
    plt.close()

plot1()
plot2()
diabetes_file.close()
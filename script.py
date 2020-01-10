import pandas as pd
import os

def read_ods(filename):
    return pd.read_excel(filename, engine="odf")

IELTS = read_ods("IELTS.ods")
IELTS.columns = ['student','Reading','Speaking','Writing','Listening']
IELTS = IELTS.drop([0, 1])
IELTS = IELTS.set_index(IELTS['student'])
IELTS = IELTS.drop('student', axis=1)
IELTS = IELTS.sum(axis=1)*30/100

term1 = read_ods("Data1.ods")
term1.columns = ['student', 'Algebra', 'Physics', 'PE', 'Chemistry', 'Geometry', 'Biology', 'Programming']
term1 = term1.drop([0, 1])
term1 = term1.set_index(term1['student'])
term1 = term1.drop('student', axis=1)
term1['Algebra'] = term1['Algebra']*2
term1['Geometry'] = term1['Geometry']*2
term1['Physics'] = term1['Physics']*2
term1 = term1.mean(axis=1)

term2 = read_ods("Data2.ods")
term2.columns = ['student', 'Algebra', 'Physics', 'PE', 'Chemistry', 'Geometry', 'Biology', 'Programming']
term2 = term2.drop([0, 1])
term2 = term2.set_index(term2['student'])
term2 = term2.drop('student', axis=1)
term2['Algebra'] = term2['Algebra']*2
term2['Geometry'] = term2['Geometry']*2
term2['Physics'] = term2['Physics']*2
term2 = term2.mean(axis=1)

term3 = read_ods("Data3.ods")
term3.columns = ['student', 'Algebra', 'Physics', 'PE', 'Chemistry', 'Geometry', 'Biology', 'Programming']
term3 = term3.drop([0, 1])
term3 = term3.set_index(term3['student'])
term3 = term3.drop('student', axis=1)
term3['Algebra'] = term3['Algebra']*2
term3['Geometry'] = term3['Geometry']*2
term3['Physics'] = term3['Physics']*2
term3 = term3.mean(axis=1)

term4 = read_ods("Data4.ods")
term4.columns = ['student', 'Algebra', 'Physics', 'PE', 'Chemistry', 'Geometry', 'Biology', 'Programming']
term4 = term4.drop([0, 1])
term4 = term4.set_index(term4['student'])
term4 = term4.drop('student', axis=1)
term4['Algebra'] = term4['Algebra']*2
term4['Geometry'] = term4['Geometry']*2
term4['Physics'] = term4['Physics']*2
term4 = term4.mean(axis=1)

academics = { 'Term 1': term1, 'Term 2': term2, 'Term 3' : term3, 'Term 4' : term4 }
academics = pd.DataFrame(academics)
academics = academics.sum(axis=1)*40/100

interview = read_ods("Interview.ods")
interview.columns = ['student', 'leadership', 'financial', 'Knowledge', 'Friendship', 'Teamwork']
interview = interview.drop([0, 1])
interview = interview.set_index(interview['student'])
interview = interview.drop('student', axis=1)
interview = interview.sum(axis=1)*30/100

total_score = {'academics':academics,'interview':interview,'IELTS':IELTS}
total_score = pd.DataFrame(total_score)
total_score = total_score.sum(axis=1)
total_score = {'Total Score':total_score}
total_score = pd.DataFrame(total_score)
total_score = total_score.sort_values("Total Score",ascending=False)
total_score.to_csv(os.getcwd()+'/'+'result.txt', sep='\t', index=True)
print(total_score)
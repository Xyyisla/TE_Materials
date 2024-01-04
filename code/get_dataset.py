# -*-coding:utf-8-*-

from mp_api.client import MPRester
import pandas as pd

with open('key.txt') as f:
    key = f.read()
'''
稀土元素
 ['Ho','La','Ce','Pr', 'Nd', 'Pm','Sm','Eu','Gd','Tb','Dy', 'Er', 'Tm', 'Yb', 'Lu', 'Y', 'Sc']

所有元素
'Ac', 'Ag', 'Al', 'Am', 'Ar', 'As', 'At', 'Au', 'B', 'Ba', 'Be', 'Bi', 'Bk', 'Br', 'C', 'Ca',
'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Co', 'Cr', 'Cs', 'Cu', 'Dy', 'Er', 'Es', 'Eu', 'F', 'Fe', 'Fm',
'Fr', 'Ga', 'Gd', 'Ge', 'H', 'He', 'Hf', 'Hg', 'Ho', 'I', 'In', 'Ir', 'K', 'Kr', 'La', 'Li',
'Lr', 'Lu', 'Md', 'Mg', 'Mn', 'Mo', 'N', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'No', 'Np', 'O', 'Os',
'P', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'Ra', 'Rb', 'Re', 'Rh', 'Rn', 'Ru', 'S',
'Sb', 'Sc', 'Se', 'Si', 'Sm', 'Sn', 'Sr', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm', 'U',
'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh',
'Fl', 'Mc', 'Lv', 'Ts', 'Og'

元素分布
'Sb','O','Te','Sn','Cu','Se','Bi', 'Ti', 'Co','Ba','Ca','Ge', 'Ag','Sr','Mn', 'Mg', 'Ga',
 'Ni', 'Fe', 'Pb','Zn','S','Si', 'In', 'Zr','Na','Al','Hf','Cd', 'Cr','Ta','Li', 'Br','K',
 'I','Mo','Tl','Cl','Pt', 'Au', 'B','V', 'Hg', 'W','P','Ru','Cs','Rh'

剩余元素
'Ac', 'Am', 'Ar', 'As', 'At', 'Be', 'Bk','C', 'Cf', 'Cm', 'Es', 'F', 'Fm','Fr', 'H', 'He', 'Ir', 'Kr','Lr',
 'Md', 'N', 'Nb', 'Ne', 'No', 'Np', 'Os''Pa', 'Pd', 'Po', 'Pu', 'Ra', 'Rb', 'Re', 'Rn',
'Tc', 'Th', 'U','Xe', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh','Fl', 'Mc', 'Lv', 'Ts', 'Og'
'''
with MPRester(api_key = key) as mpr:
    # 除去稀土元素和部分未出现的元素
    docs = mpr.summary.search(exclude_elements=['Ho', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu',
                                                'Gd', 'Tb', 'Dy', 'Er', 'Tm', 'Yb', 'Lu', 'Y',
                                                'Sc','Ac', 'Am', 'Ar', 'As', 'At', 'Be', 'Bk','C',
                                                'Cf', 'Cm', 'Es', 'F', 'Fm','Fr', 'H', 'He', 'Ir',
                                                'Kr','Lr', 'Md', 'N', 'Nb', 'Ne', 'No', 'Np', 'Os',
                                                'Pa', 'Pd', 'Po', 'Pu', 'Ra', 'Rb', 'Re', 'Rn','Tc',
                                                'Th', 'U','Xe', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt',
                                                'Ds', 'Rg', 'Cn', 'Nh','Fl', 'Mc', 'Lv', 'Ts', 'Og',
                                                # 'V', 'Hg', 'W', 'P', 'Ru', 'Cs', 'Rh',
                                                ],
                              fields=["material_id",
                                      "formula_pretty",
                                      "band_gap",
                                      "volume"
                                      ])
    id_list = []
    formula_list = []
    band_gap_list = []
    for doc in docs:
        id_list.append(doc.material_id)
        formula_list.append(doc.formula_pretty)
        band_gap_list.append(doc.band_gap)

    mpid_formula_dict = pd.DataFrame({
        'mp_id':id_list,
        'formula':formula_list,
        'band_gap':band_gap_list
    })
    print(mpid_formula_dict)

    mpid_formula_dict.to_csv('./e.csv', encoding='gbk',index=False)






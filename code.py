import numpy as np


def catch_probability(BCR, CPM, curve, berry, radius, medal):
    return 1 - (1 - BCR / (2 * CPM)) ** (curve * berry * radius * medal)


def expected_value(lambda_p, lambda_r, base_candy, n_balls, n_pinap, bonus_candy):
    return 2 * base_candy \
           - base_candy * (1 - lambda_p) ** n_pinap * (1 + (1 - lambda_r) ** (n_balls - n_pinap)) \
           + bonus_candy * (1 - (1 - lambda_p) ** n_pinap *(1 - lambda_r) ** (n_balls - n_pinap))

    
def strategy(BCR, CPM, curve, berry_p, berry_r, radius, medal, base_candy, n_balls, bonus_candy):
    
    lambda_p = catch_probability(BCR, CPM, curve, berry_p, radius, medal)
    lambda_r = catch_probability(BCR, CPM, curve, berry_r, radius, medal)
    
    res = []
    for n_pinap in range(n_balls + 1):
        res.append(expected_value(lambda_p, lambda_r, base_candy, n_balls, n_pinap, bonus_candy))
        
    return np.array(res)
	
	
	def table_to_latex(table):
    string = ""
    string += """\\begin{table}[H] \n"""
    string += """\\begin{footnotesize} \n"""
    string += """\\begin{changemargin}{-2cm}{-2cm} \n"""
    string += """\centering \n"""
    string += """\\begin{tabular}{*{14}{|c}|} \n"""
    string += """\hline  \n"""
    string += """{} &  \\textbf{6}  &     \\textbf{7}  & \\textbf{8}  &     \\textbf{9}  &     \\textbf{10} &   """
    string += """  \\textbf{11} &     \\textbf{12} &     \\textbf{13} &     \\textbf{14} &  \\textbf{15} &  \\textbf{16} & \\textbf{17} & \\textbf{18} \\\ \n"""
    string += """\hline  \n"""
    
    table = table.T
    maxi = np.nanmax(table, axis=0)
    for i in range(table.shape[0]):
        string += "\\textbf{" + str(i) + "}  & "
        for j in range(table.shape[1]):
            if np.isnan(table[i, j]):
                string += "\cellcolor[gray]{0.9} {} & "
            elif table[i, j] == maxi[j]:
                string += "\cellcolor{red!30} " + str(round(table[i, j], 2)) + " & "
            else:
                string += str(round(table[i, j], 2)) + " & "
        string = string[:-2]
        string += "\\\ \hline \n"

    string += """\end{tabular} \n"""
    string += """\end{changemargin} \n"""  
    string += """\end{footnotesize} \n"""  
    string += """\caption{Pinap vs Golden Razz Berries: Expected number of candies for each scenario. Each column is the number of Premier Balls and each row is the number of Pinap berries used before switching to Golden Razz Berries.} \n"""
    string += """\end{table}"""  
    return string

def timer_gen(n,source_brench, var_name, comment, frame_brench):
    mod_s_brench, line = split_path(source_brench)
    clean_line = line.replace("_"," ")
    mod_f_brench, machine = split_path(frame_brench)
    string = 'CTV,'+str(n)+',' + mod_s_brench + ','+var_name + ',,,,,,,,,,,"'+comment+'","",,,,,,E,0,0,0,2,0,1,0,0,0,0,,,1,'+mod_f_brench+',U,24,0,32,,,,,,,,,,,,,,,,,,,,,,,"dsec",0,-32767,32767,0,-32767,32767,"#.#",,,0,999,1,,,,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"","","",,,"","",,,,,,,,,,,,,,0,"","'+clean_line+'","'+comment+'","","",'+comment+'","","","","","","","","",,,,,,,,,,,,0,0,,,0,,,,,,,,,,,,,,0,-1,-2,-2,1,"0",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
    return string


def split_path(path):
    # Utilizza il metodo split della stringa per dividere il percorso in parti
    parts = path.split('.')

    # Rimuovi eventuali stringhe vuote risultanti da punti consecutivi
    parts = [part for part in parts if part]
    result = ','.join(parts)
    return result, parts[1]

def build_expression(expression_name,comment,source_path,scada_result,input_path,input_bit):
    # non è presente l'abilitazione
    expression = 'EXPRESSIONONVAR,"'+expression_name + '","'+ comment + '",0,0,"","",1,"","@'+source_path+'.'+ scada_result + '","","'+input_path + '>>' + input_bit + '",1'
    return expression

def command_level_gen(n, source_brench, var_name):
    mod_s_brench, line = split_path(source_brench)
    string = 'CTV,'+str(n)+','+mod_s_brench+','+var_name+'_L,,,,,,,,,,,"Impostazione Livello Comando","",,,,,,I,0,0,0,2,0,0,0,0,0,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"",0,0,10,0,0,65535,"#",,,0,10,0,,,,0,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"","","",,,"","",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0,0,,,0,,,,,,,,,,,,,,0,-1,-2,-2,1,"1",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
    return string

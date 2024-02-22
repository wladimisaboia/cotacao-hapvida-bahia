from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cotacao.html')

@app.route('/cotacao', methods=['POST'])
def cotar():
    idades_str = request.form['idade']
    idades = [int(age.strip()) for age in idades_str.split(',')]
    plano = request.form['plano'].strip()

    valores = {}
    total_valor = 0
    desconto_aplicado = False

    for idade in idades:
        valor = 0

        #if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'ambulatorial (pessoa física) - Com coparticipação' or plano == 'enfermaria com obstetrícia (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'enfermaria com obstetrícia (pessoa física) - Com coparticipação' or plano == 'enfermaria sem obstetrícia (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'enfermaria sem obstetrícia (pessoa física) - Com coparticipação' or plano == 'apartamento com obstetrícia (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'apartamento com obstetrícia (pessoa física) - Com coparticipação' or plano == 'apartamento sem obstetrícia (pessoa física) - Sem coparticipação, exceto terapias' or plano == 'apartamento sem obstetrícia (pessoa física) - Com coparticipação':
            #if len(idades) >= 2 and not desconto_aplicado:
                #valor = valor * 0.95
                #desconto_aplicado = True

        if plano == 'ambulatorial (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 205.34
            elif idade <= 23:
                valor = 270.49
            elif idade <= 28:
                valor = 308.38
            elif idade <= 33:
                valor = 344.03
            elif idade <= 38:
                valor = 362.07
            elif idade <= 43:
                valor = 406.51
            elif idade <= 48:
                valor = 497.15
            elif idade <= 53:
                valor = 689.62
            elif idade <= 58:
                valor = 929.71
            else:
                valor = 1207.53
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 131.74
            elif idade <= 23:
                valor = 173.11
            elif idade <= 28:
                valor = 197.17
            elif idade <= 33:
                valor = 219.81
            elif idade <= 38:
                valor = 231.27
            elif idade <= 43:
                valor = 259.49
            elif idade <= 48:
                valor = 317.05
            elif idade <= 53:
                valor = 439.28
            elif idade <= 58:
                valor = 591.75
            else:
                valor = 768.18
        elif plano == 'enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 259.09
            elif idade <= 23:
                valor = 340.83
            elif idade <= 28:
                valor = 391.41
            elif idade <= 33:
                valor = 437.94
            elif idade <= 38:
                valor = 459.65
            elif idade <= 43:
                valor = 518.93
            elif idade <= 48:
                valor = 632.29
            elif idade <= 53:
                valor = 871.17
            elif idade <= 58:
                valor = 1174.80
            else:
                valor = 1526.15
        elif plano == 'enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 212.93
            elif idade <= 23:
                valor = 279.90
            elif idade <= 28:
                valor = 321.34
            elif idade <= 33:
                valor = 359.46
            elif idade <= 38:
                valor = 377.25
            elif idade <= 43:
                valor = 425.82
            elif idade <= 48:
                valor = 518.70
            elif idade <= 53:
                valor = 714.42
            elif idade <= 58:
                valor = 963.19
            else:
                valor = 1251.05
        elif plano == 'apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 386.81
            elif idade <= 23:
                valor = 509.42
            elif idade <= 28:
                valor = 585.29
            elif idade <= 33:
                valor = 655.09
            elif idade <= 38:
                valor = 687.66
            elif idade <= 43:
                valor = 776.58
            elif idade <= 48:
                valor = 946.62
            elif idade <= 53:
                valor = 1304.95
            elif idade <= 58:
                valor = 1760.41
            else:
                valor = 2287.44
        elif plano == 'apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 317.57
            elif idade <= 23:
                valor = 418.02
            elif idade <= 28:
                valor = 480.18
            elif idade <= 33:
                valor = 537.36
            elif idade <= 38:
                valor = 564.05
            elif idade <= 43:
                valor = 636.90
            elif idade <= 48:
                valor = 776.22
            elif idade <= 53:
                valor = 1069.80
            elif idade <= 58:
                valor = 1442.95
            else:
                valor = 1874.74
        elif plano == 'ambulatorial (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 188.90
            elif idade <= 23:
                valor = 211.57
            elif idade <= 28:
                valor = 236.96
            elif idade <= 33:
                valor = 272.50
            elif idade <= 38:
                valor = 313.38
            elif idade <= 43:
                valor = 372.92
            elif idade <= 48:
                valor = 466.15
            elif idade <= 53:
                valor = 582.69
            elif idade <= 58:
                valor = 990.57
            else:
                valor = 1109.44
        elif plano == 'ambulatorial (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 121.05
            elif idade <= 23:
                valor = 135.58
            elif idade <= 28:
                valor = 151.85
            elif idade <= 33:
                valor = 174.63
            elif idade <= 38:
                valor = 200.82
            elif idade <= 43:
                valor = 238.98
            elif idade <= 48:
                valor = 298.73
            elif idade <= 53:
                valor = 373.41
            elif idade <= 58:
                valor = 634.80
            else:
                valor = 710.98
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 253.04
            elif idade <= 23:
                valor = 283.40
            elif idade <= 28:
                valor = 317.41
            elif idade <= 33:
                valor = 365.02
            elif idade <= 38:
                valor = 419.77
            elif idade <= 43:
                valor = 499.53
            elif idade <= 48:
                valor = 624.41
            elif idade <= 53:
                valor = 780.51
            elif idade <= 58:
                valor = 1326.87
            else:
                valor = 1486.09
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 175.73
            elif idade <= 23:
                valor = 196.82
            elif idade <= 28:
                valor = 220.44
            elif idade <= 33:
                valor = 253.51
            elif idade <= 38:
                valor = 291.54
            elif idade <= 43:
                valor = 346.93
            elif idade <= 48:
                valor = 433.66
            elif idade <= 53:
                valor = 542.08
            elif idade <= 58:
                valor = 921.54
            else:
                valor = 1032.12
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 378.90
            elif idade <= 23:
                valor = 424.37
            elif idade <= 28:
                valor = 475.29
            elif idade <= 33:
                valor = 546.58
            elif idade <= 38:
                valor = 628.57
            elif idade <= 43:
                valor = 748.00
            elif idade <= 48:
                valor = 935.00
            elif idade <= 53:
                valor = 1168.75
            elif idade <= 58:
                valor = 1986.88
            else:
                valor = 2225.31
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 262.92
            elif idade <= 23:
                valor = 294.47
            elif idade <= 28:
                valor = 329.81
            elif idade <= 33:
                valor = 379.28
            elif idade <= 38:
                valor = 436.17
            elif idade <= 43:
                valor = 519.04
            elif idade <= 48:
                valor = 648.80
            elif idade <= 53:
                valor = 811.00
            elif idade <= 58:
                valor = 1378.70
            else:
                valor = 1544.14
        else:
            return 'Plano inválido'

        if idade not in valores:
            valores[idade] = {'plano': [], 'qtd': 0}

        valores[idade]['plano'].append(valor)
        total_valor += valor
        valores[idade]['qtd'] += 1

    if desconto_aplicado:
        total_valor = total_valor * 0.95

    total_valor = '{:.2f}'.format(total_valor)

    return render_template('resposta.html', valores=valores, total_valor=total_valor, desconto_aplicado=desconto_aplicado, plano_selecionado=plano)

if __name__ == '__main__':
    app.run(debug=True)

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
                valor = 217.79
            elif idade <= 23:
                valor = 286.79
            elif idade <= 28:
                valor = 327.21
            elif idade <= 33:
                valor = 365.07
            elif idade <= 38:
                valor = 384.23
            elif idade <= 43:
                valor = 431.43
            elif idade <= 48:
                valor = 527.62
            elif idade <= 53:
                valor = 732.09
            elif idade <= 58:
                valor = 987.06
            else:
                valor = 1282.10
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 139.63
            elif idade <= 23:
                valor = 183.57
            elif idade <= 28:
                valor = 209.13
            elif idade <= 33:
                valor = 233.18
            elif idade <= 38:
                valor = 245.35
            elif idade <= 43:
                valor = 275.33
            elif idade <= 48:
                valor = 336.47
            elif idade <= 53:
                valor = 466.29
            elif idade <= 58:
                valor = 628.23
            else:
                valor = 815.62
        elif plano == 'enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 246.26
            elif idade <= 23:
                valor = 323.97
            elif idade <= 28:
                valor = 371.96
            elif idade <= 33:
                valor = 416.16
            elif idade <= 38:
                valor = 436.79
            elif idade <= 43:
                valor = 493.10
            elif idade <= 48:
                valor = 600.79
            elif idade <= 53:
                valor = 827.72
            elif idade <= 58:
                valor = 1116.16
            else:
                valor = 1449.93
        elif plano == 'enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 223.62
            elif idade <= 23:
                valor = 294.03
            elif idade <= 28:
                valor = 337.59
            elif idade <= 33:
                valor = 377.67
            elif idade <= 38:
                valor = 396.37
            elif idade <= 43:
                valor = 447.43
            elif idade <= 48:
                valor = 545.07
            elif idade <= 53:
                valor = 750.83
            elif idade <= 58:
                valor = 1012.36
            else:
                valor = 1314.99
        elif plano == 'apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 410.52
            elif idade <= 23:
                valor = 540.73
            elif idade <= 28:
                valor = 621.30
            elif idade <= 33:
                valor = 695.42
            elif idade <= 38:
                valor = 730.01
            elif idade <= 43:
                valor = 824.44
            elif idade <= 48:
                valor = 1005.02
            elif idade <= 53:
                valor = 1385.56
            elif idade <= 58:
                valor = 1869.25
            else:
                valor = 2428.95
        elif plano == 'apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 336.98
            elif idade <= 23:
                valor = 443.66
            elif idade <= 28:
                valor = 509.67
            elif idade <= 33:
                valor = 570.40
            elif idade <= 38:
                valor = 598.74
            elif idade <= 43:
                valor = 676.11
            elif idade <= 48:
                valor = 824.06
            elif idade <= 53:
                valor = 1135.83
            elif idade <= 58:
                valor = 1532.11
            else:
                valor = 1990.66
        elif plano == 'ambulatorial (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 200.54
            elif idade <= 23:
                valor = 224.60
            elif idade <= 28:
                valor = 251.55
            elif idade <= 33:
                valor = 289.28
            elif idade <= 38:
                valor = 332.67
            elif idade <= 43:
                valor = 395.88
            elif idade <= 48:
                valor = 494.85
            elif idade <= 53:
                valor = 618.56
            elif idade <= 58:
                valor = 1051.55
            else:
                valor = 1177.74
        elif plano == 'ambulatorial (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 128.47
            elif idade <= 23:
                valor = 143.89
            elif idade <= 28:
                valor = 161.16
            elif idade <= 33:
                valor = 185.33
            elif idade <= 38:
                valor = 213.13
            elif idade <= 43:
                valor = 253.62
            elif idade <= 48:
                valor = 317.03
            elif idade <= 53:
                valor = 396.29
            elif idade <= 58:
                valor = 673.69
            else:
                valor = 754.53
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 268.63
            elif idade <= 23:
                valor = 300.87
            elif idade <= 28:
                valor = 336.97
            elif idade <= 33:
                valor = 387.52
            elif idade <= 38:
                valor = 445.65
            elif idade <= 43:
                valor = 530.32
            elif idade <= 48:
                valor = 662.90
            elif idade <= 53:
                valor = 828.63
            elif idade <= 58:
                valor = 1408.67
            else:
                valor = 1577.71
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 135.82
            elif idade <= 23:
                valor = 152.11
            elif idade <= 28:
                valor = 170.37
            elif idade <= 33:
                valor = 195.92
            elif idade <= 38:
                valor = 225.31
            elif idade <= 43:
                valor = 268.12
            elif idade <= 48:
                valor = 335.15
            elif idade <= 53:
                valor = 418.94
            elif idade <= 58:
                valor = 712.20
            else:
                valor = 797.66
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 402.31
            elif idade <= 23:
                valor = 450.59
            elif idade <= 28:
                valor = 504.66
            elif idade <= 33:
                valor = 580.36
            elif idade <= 38:
                valor = 667.41
            elif idade <= 43:
                valor = 794.22
            elif idade <= 48:
                valor = 992.78
            elif idade <= 53:
                valor = 1240.98
            elif idade <= 58:
                valor = 2109.67
            else:
                valor = 2362.83
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 279.14
            elif idade <= 23:
                valor = 312.64
            elif idade <= 28:
                valor = 350.16
            elif idade <= 33:
                valor = 402.68
            elif idade <= 38:
                valor = 463.08
            elif idade <= 43:
                valor = 551.07
            elif idade <= 48:
                valor = 688.84
            elif idade <= 53:
                valor = 861.05
            elif idade <= 58:
                valor = 1463.79
            else:
                valor = 1639.44
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

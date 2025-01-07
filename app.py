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
                valor = 228.61
            elif idade <= 23:
                valor = 301.25
            elif idade <= 28:
                valor = 343.50
            elif idade <= 33:
                valor = 383.26
            elif idade <= 38:
                valor = 403.38
            elif idade <= 43:
                valor = 452.94
            elif idade <= 48:
                valor = 554.02
            elif idade <= 53:
                valor = 768.64
            elif idade <= 58:
                valor = 1036.37
            else:
                valor = 1346.17
        elif plano == 'ambulatorial (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 146.54
            elif idade <= 23:
                valor = 192.67
            elif idade <= 28:
                valor = 219.50
            elif idade <= 33:
                valor = 244.75
            elif idade <= 38:
                valor = 257.53
            elif idade <= 43:
                valor = 289.00
            elif idade <= 48:
                valor = 353.19
            elif idade <= 53:
                valor = 489.49
            elif idade <= 58:
                valor = 659.51
            else:
                valor = 856.25
        elif plano == 'enfermaria (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 248.31
            elif idade <= 23:
                valor = 326.58
            elif idade <= 28:
                valor = 375.01
            elif idade <= 33:
                valor = 419.57
            elif idade <= 38:
                valor = 440.36
            elif idade <= 43:
                valor = 497.12
            elif idade <= 48:
                valor = 605.67
            elif idade <= 53:
                valor = 834.41
            elif idade <= 58:
                valor = 1125.16
            else:
                valor = 1461.60
        elif plano == 'enfermaria (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 234.73
            elif idade <= 23:
                valor = 308.66
            elif idade <= 28:
                valor = 354.40
            elif idade <= 33:
                valor = 396.48
            elif idade <= 38:
                valor = 416.12
            elif idade <= 43:
                valor = 469.73
            elif idade <= 48:
                valor = 572.25
            elif idade <= 53:
                valor = 788.30
            elif idade <= 58:
                valor = 1062.91
            else:
                valor = 1380.67
        elif plano == 'apartamento (pessoa física) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 413.88
            elif idade <= 23:
                valor = 545.13
            elif idade <= 28:
                valor = 626.34
            elif idade <= 33:
                valor = 701.06
            elif idade <= 38:
                valor = 735.93
            elif idade <= 43:
                valor = 831.12
            elif idade <= 48:
                valor = 1013.15
            elif idade <= 53:
                valor = 1396.74
            elif idade <= 58:
                valor = 1884.30
            else:
                valor = 2448.48
        elif plano == 'apartamento (pessoa física) - Com coparticipação':
            if idade <= 18:
                valor = 353.76
            elif idade <= 23:
                valor = 465.78
            elif idade <= 28:
                valor = 535.09
            elif idade <= 33:
                valor = 598.86
            elif idade <= 38:
                valor = 628.62
            elif idade <= 43:
                valor = 709.86
            elif idade <= 48:
                valor = 865.21
            elif idade <= 53:
                valor = 1192.58
            elif idade <= 58:
                valor = 1608.68
            else:
                valor = 2090.17
        elif plano == 'ambulatorial (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 210.50
            elif idade <= 23:
                valor = 235.76
            elif idade <= 28:
                valor = 264.05
            elif idade <= 33:
                valor = 303.66
            elif idade <= 38:
                valor = 349.21
            elif idade <= 43:
                valor = 415.56
            elif idade <= 48:
                valor = 519.45
            elif idade <= 53:
                valor = 649.31
            elif idade <= 58:
                valor = 1103.83
            else:
                valor = 1236.29
        elif plano == 'ambulatorial (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 134.83
            elif idade <= 23:
                valor = 151.01
            elif idade <= 28:
                valor = 169.13
            elif idade <= 33:
                valor = 194.50
            elif idade <= 38:
                valor = 223.68
            elif idade <= 43:
                valor = 266.18
            elif idade <= 48:
                valor = 332.73
            elif idade <= 53:
                valor = 415.91
            elif idade <= 58:
                valor = 707.05
            else:
                valor = 791.90
        elif plano == 'enfermaria (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 282.01
            elif idade <= 23:
                valor = 315.85
            elif idade <= 28:
                valor = 353.75
            elif idade <= 33:
                valor = 406.81
            elif idade <= 38:
                valor = 467.83
            elif idade <= 43:
                valor = 556.72
            elif idade <= 48:
                valor = 695.90
            elif idade <= 53:
                valor = 869.88
            elif idade <= 58:
                valor = 1478.80
            else:
                valor = 1656.26
        elif plano == 'enfermaria (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 142.54
            elif idade <= 23:
                valor = 159.64
            elif idade <= 28:
                valor = 178.80
            elif idade <= 33:
                valor = 205.62
            elif idade <= 38:
                valor = 236.46
            elif idade <= 43:
                valor = 281.39
            elif idade <= 48:
                valor = 351.74
            elif idade <= 53:
                valor = 439.68
            elif idade <= 58:
                valor = 747.46
            else:
                valor = 837.16
        elif plano == 'apartamento (pessoa jurídica) - Sem coparticipação, exceto terapias':
            if idade <= 18:
                valor = 422.36
            elif idade <= 23:
                valor = 473.04
            elif idade <= 28:
                valor = 529.80
            elif idade <= 33:
                valor = 609.27
            elif idade <= 38:
                valor = 700.66
            elif idade <= 43:
                valor = 833.79
            elif idade <= 48:
                valor = 1042.24
            elif idade <= 53:
                valor = 1302.80
            elif idade <= 58:
                valor = 2214.76
            else:
                valor = 2480.53
        elif plano == 'apartamento (pessoa jurídica) - Com coparticipação':
            if idade <= 18:
                valor = 293.03
            elif idade <= 23:
                valor = 328.19
            elif idade <= 28:
                valor = 367.57
            elif idade <= 33:
                valor = 422.71
            elif idade <= 38:
                valor = 486.12
            elif idade <= 43:
                valor = 578.48
            elif idade <= 48:
                valor = 723.10
            elif idade <= 53:
                valor = 903.88
            elif idade <= 58:
                valor = 1536.60
            else:
                valor = 1720.99
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

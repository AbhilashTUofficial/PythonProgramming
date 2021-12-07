
txtMod = {

    'default': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'italics': '\033[3m',
    'underline': '\033[4m',
    'wordCrossed': '\033[9m',

    'dimBlack': '\033[30m',
    'dimRed': '\033[31m',
    'dimGreen': '\033[32m',
    'dimYellow': '\033[33m',
    'dimBlue': '\033[34m',
    'dimMagentha': '\033[35m',
    'dimCyan': '\033[36m',

    'grey': '\033[90m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',

    'invisible': '\033[8m',
    'invertClr': '\033[7m',  # * txt → bgd, bgd → txt

    'balckBGD': '\033[40m',
    'redBGD': '\033[41m',
    'greenBGD': '\033[42m',
    'yellowBGD': '\033[43m',
    'blueBGD': '\033[44m',
    'purpleBGD': '\033[45m',
    'cyanBGD': '\033[46m',
    'whiteBGD': '\033[47m',

    'dimBlackBGD': '\033[100m',
    'dimRedBGD': '\033[101m',
    'dimGreenBGD': '\033[102m',
    'dimYellowBGD': '\033[103m',
    'dimBlueBGD': '\033[104m',
    'dimPurpleBGD': '\033[105m',
    'dimCyanBGD': '\033[106m',
    'dimWhiteBGD': '\033[107m',
    'dimBlackBGD': '\033[100m'

}


def main():

    mod = list(txtMod.values())

    for i in range(1, len(mod)-1):
        x = int(mod[i][2:-1])

        print(f"{mod[i]}{x}{mod[0]}", end=' 'if i % 6 != 0 else'\n\n')
        # print(f"{mod[i]}%5.0f{mod[i]}"% x,end=' 'if i%6!=0 else'\n\n')


if __name__ == "__main__":
    main()

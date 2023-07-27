def main():
    age = int(input('Wie alt sind sie?'))
    income = int(input('Wie hoch ist ihr Jahresgehalt?'))

    if age >= 21 and income >= 48000:
        print('Wir sind in der Lage, Ihnen einen Kredit anzubieten.')
    else:
        print('Leider können wir Ihnen zur Zeit keinen Kredit anbieten.')


if __name__ == '__main__':
    main()

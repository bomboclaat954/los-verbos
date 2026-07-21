import json
import sys


def ar(v):
    v = v[:-2]
    print("yo                   ", v + "o")
    print("tú                   ", v + "as")
    print("el[la] / usted       ", v + "a")
    print("nosotr[os/as]        ", v + "amos")
    print("vosotr[os/as]        ", v + "áis")
    print("ell[os/as] / ustedes ", v + "an")


def er(v):
    v = v[:-2]
    print("yo                   ", v + "o")
    print("tú                   ", v + "es")
    print("el[la] / usted       ", v + "e")
    print("nosotr[os/as]        ", v + "emos")
    print("vosotr[os/as]        ", v + "éis")
    print("ell[os/as] / ustedes ", v + "en")


def ir(v):
    v = v[:-2]
    print("yo                   ", v + "o")
    print("tú                   ", v + "es")
    print("el[la] / usted       ", v + "e")
    print("nosotr[os/as]        ", v + "imos")
    print("vosotr[os/as]        ", v + "ís")
    print("ell[os/as] / ustedes ", v + "en")


def irreg(v):
    x = ""
    with open("irreg.json", "r") as f:
        x = f.read()
    y = json.loads(x)
    try:
        if y[v]:
            print("yo                   ", y[v]["1"])
            print("tú                   ", y[v]["2"])
            print("el[la] / usted       ", y[v]["3"])
            print("nosotr[os/as]        ", y[v]["4"])
            print("vosotr[os/as]        ", y[v]["5"])
            print("ell[os/as] / ustedes ", y[v]["6"])
            return 1
    except KeyError:
        return 0


def cmd_add():
    print("Añadir un verbo nuevo")
    inf = input("Infinitivo: ")
    form1 = input("yo: ")
    form2 = input("tú: ")
    form3 = input("el[la] / usted: ")
    form4 = input("nosotr[os/as]: ")
    form5 = input("vosotr[os/as]: ")
    form6 = input("ell[os/as] / ustedes: ")
    f_current = ""
    with open("irreg.json", "r") as f:
        f_current = f.read()

    if f_current[-1] == "}":
        f_current = f_current[:-2]
    else:
        f_current = f_current[:-3]

    j = json.dumps(
        {"1": form1, "2": form2, "3": form3, "4": form4, "5": form5, "6": form6},
        indent=4,
        ensure_ascii=False,
    ).replace("\n", "\n\t")
    f_current += f',\n\t"{inf}": {j}\t' + "\t\n}"
    with open("irreg.json", "w") as f:
        f.write(f_current)


def main(v):
    print("Los Verbos v1.1")
    if v == "\\a":
        cmd_add()
    elif irreg(v) == 0:
        if v[-2:] == "ar":
            ar(v)
        elif v[-2:] == "er":
            er(v)
        elif v[-2:] == "ir":
            ir(v)
    else:
        pass


if __name__ == "__main__":
    try:
        v = sys.argv[1]
        if not v:
            print("No se proporcionó ningún verbo!")
            exit()
        main(v)
    except KeyboardInterrupt:
        exit()

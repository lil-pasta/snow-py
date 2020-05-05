smallHouse=["  _____||____",
            " /^ ^ ^ ^ ^ ^\\",
            "/^_^_^_^_^_^_^\\",
            "[=[_]======_==]",
            "[=[_]=====|+|=]",
            "[=========|_|=]"]

moon=["         ___---___",
      "      .--         --.",
      "    ./   ()      .-. \.",
      "   /   o    .   (   )  \\",
      "  / .            '-'    \\",
      " | ()    .  O         .  |",
      "|                         |",
      "|    o           ()       |",
      "|       .--.          O   |",
      " | .   |    |            |",
      "  \    `.__.'    o   .  /",
      "   \                   /",
      "    `\  o    ()      /' JT/jgs",
      "      `--___   ___--'",
      "            ---"]


def dict_it(ascii):
    y = 0
    dict = {}
    for row in ascii:
        x = 0
        for ch in row:
            dict[(y,x)] = ch
            x += 1
        y +=1
    return dict

if __name__ == '__main__':
    moon_dict = dict_it(moon)
    smallHous_dict = dict_it(smallHouse)

    with open('ascii_dict.py', 'w+') as f:
        f.write('moon = {')
        for k, v in moon_dict.items():
            f.write("{}: \"{}\",\n".format(k, v))
        f.write('}\n')
        f.write('smallHouse = {')
        for k, v in smallHous_dict.items():
            f.write("{}: \"{}\",\n".format(k, v))
        f.write('}\n')


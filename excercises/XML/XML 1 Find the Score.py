import xml.etree.ElementTree as etree

score = 0


def iterate_through(node: etree.Element):
    global score

    for child in node:
        child: etree.Element

        score += len(child.attrib)

        if len(child) > 0:
            iterate_through(child)


def get_attr_number(node):
    iterate_through(node)

    return score + len(node.attrib)


if __name__ == '__main__':

    N = int(input())

    lines = []

    for _ in range(N):
        lines.append(input())

    xml = "".join(lines)
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

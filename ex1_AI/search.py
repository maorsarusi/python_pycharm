## תרגיל 1 סעיף 2
# search
from ex1_AI import state
from ex1_AI import frontier


def search(n):
    s = state.create(n)
    f = frontier.create(s)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[4]]  ##  f[4]בשביל הנוחות הוספנו את
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f, i)


## return 0


## תרגיל 1 סעיף 3
def avarage(n):
    depth = 0
    number = 0
    for i in range(0, 100):
        f = search(n)
        depth += f[1]
        number += f[2]
    print("Average depth ", float(depth / 100), "\nAverage number  ", float(number / 100))

##תרגיל 1 סעיף 4
## מהרצות אנחנו רואים
## שהאלגורתים dfs
##אינו טוב ממש לתרגיל זה
##מכיוון שעבור n=4 הוא נתקע

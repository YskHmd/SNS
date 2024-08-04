top = 5
a = [["", 0] for _ in range(10)]

a[0] = ["京都", 4]
a[1] = ["新横浜", 8]
a[3] = ["博多", -1]  # 終端記号（nil）は-1で表示
a[4] = ["新大阪", 6]
a[5] = ["品川", 1]
a[6] = ["広島", 3]
a[8] = ["名古屋", 0]

def search(a, t, x):  # a: リスト, t: top, x: 探したい駅名
    next = t
    while True:
        if a[next][0] == x:  # [0](駅名)がxと同じなら終了
            return next
        next = a[next][1]  # 同じじゃなければ次[1]に行く
        if next == -1:
            return -1

def insert(a, t, x):  # a: リスト, t: top, x: 追加したい駅名
    global top
    new_index = -1

    # 空いているインデックスを探す
    for i in range(len(a)):
        if a[i][1] == 0 and a[i][0] == "":
            new_index = i
            break

    if new_index == -1:
        print("リストが満杯です。")
        return t

    # 新しい要素を挿入
    a[new_index][0] = x
    a[new_index][1] = t
    top = new_index
    return top

def delete(a, t, x):  # a: リスト, t: top, x: 削除したい駅名
    global top
    current = t
    prev = -1

    while current != -1:
        if a[current][0] == x:
            if prev == -1:  # 削除対象が先頭要素の場合
                top = a[current][1]
            else:
                a[prev][1] = a[current][1]
            a[current] = ["", 0]  # 要素を初期化
            return top

        prev = current
        current = a[current][1]

    print(x, "はリストにありません。")
    return top

def Dtop(a, t):
    next= a[t][1]
    a[t][0] = "", 0
    return next

while True:
    command = input("コマンドを入力(search/insert/delete/Dtop):")
    if command == "search":
        data = input("探したい駅を入力：")
        ans = search(a, top, data)
        if ans == -1:
            print(data, "はありませんでした")
        else:
            print(data, "は a[", ans, "]にありました")
    elif command == "insert":
        data = input("追加したい駅を入力：")
        top = insert(a, top, data)
        print(data, "を追加しました")
        print("新しいリスト:", a)
    elif command == "delete":
        data = input("削除したい駅を入力：")
        top = delete(a, top, data)
        print(data, "を削除しました")
        print("新しいリスト:", a)
    elif command == "Dtop":
        top = Dtop(a, top)

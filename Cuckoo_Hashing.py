# upper bound on number of elements in our set
MAXN = 11

# choices for position
ver = 2
hashkeylist={}
collist = []
# Auxiliary space bounded by a small multiple
# of MAXN, minimizing wastage
hashtable = [[float('inf')] * MAXN for _ in range(ver)]

# Array to store possible positions for a key
pos = [0] * ver


def init_table():
    for i in range(ver):
        for j in range(MAXN):
            hashtable[i][j] = float('inf')


def hash(function, key):
    if function == 1:
        hashkeylist[key] = (key % MAXN)
        return key % MAXN

    elif function == 2:
        hashkeylist[key] = (hashkeylist[key], ((key // MAXN) % MAXN))
        return (key // MAXN) % MAXN


def place(key, table_id, cnt, n):
    if cnt == n:
        print(f"{key} unpositioned")
        print("REHASH")
        return
    for i in range(ver):
        pos[i] = hash(i + 1, key)
        if hashtable[i][pos[i]] == key:
            return

    # check if another key is already present at the position for the
    # new key in the table
    # If YES: place the new key in its position and place the older key
    # in an alternate position for it in the next table
    if hashtable[table_id][pos[table_id]] != float('inf'):
        dis = hashtable[table_id][pos[table_id]]
        hashtable[table_id][pos[table_id]] = key
        place(dis, (table_id + 1) % ver, cnt + 1, n)
    else:  # else: place the new key in its position
        hashtable[table_id][pos[table_id]] = key
        collist.append(key)


def print_table(keys):
    full=0
    empty=0
    for i in range(ver):
        print()
        for j in range(MAXN):
            if hashtable[i][j] == float('inf'):
                print("- ", end="")
                empty+=1
            else:
                print(f"{hashtable[i][j]} ", end="")
                full+=1
    print("load factor= " + str((len(keys)-full)/empty))
    print()


def cuckoo(keys, n):
    # initialize hash tables to a dummy value (float('inf'))
    # indicating empty position
    init_table()
    # start with placing every key at its position in the first
    # hash table according to first hash function
    for i in range(n):
        cnt = 0
        place(keys[i], 0, cnt, n)
        print_table(keys)
    print("collission amount = "+str(len(collist)))
    print("collissions by order in and out = " + str(collist))
    print("hashkeylist = "+ str(hashkeylist))
    # print the final hash tables



# driver function
def main():
    #insert any number of keys ranging from 10 - 30 and update the MAXN global value from above to calculate the cuckoo value

    keys_1 = [20, 50, 53, 75, 100, 67, 105, 3, 36, 39]
    cuckoo(keys_1, len(keys_1))



if __name__ == "__main__":
    main()
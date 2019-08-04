conn = []

with open('dataset_24465_4.txt','r') as f:
    for s in f:
        conn.append(s.strip())
conn.reverse()
with open('file2.txt', 'w') as f:
    f.write('\n'.join(conn))
print(conn)
import string
N = int(input())

alphabet = string.ascii_lowercase
rows = []
for i in range(N):
        # Create the string for the current row
        s = '-'.join(alphabet[N-1:i:-1] + alphabet[i:N])
        # Center align the row
        rows.append((s).center(4*N-3, '-'))
    
    # Print the rangoli
print('\n'.join(rows[:0:-1] + rows))
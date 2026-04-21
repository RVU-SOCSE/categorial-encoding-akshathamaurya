Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

================== RESTART: C:/Users/DELL/Desktop/python/35.py =================
Original Dataset:

   Brand Processor   Price
0   Dell        i5   50000
1     HP        i7   65000
2  Apple        M1  120000
3   Dell        i3   40000
4     HP        i5   52000

================== RESTART: C:/Users/DELL/Desktop/python/35.py =================
Traceback (most recent call last):
  File "C:/Users/DELL/Desktop/python/35.py", line 2, in <module>
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
ModuleNotFoundError: No module named 'sklearn'
>>> 
================== RESTART: C:/Users/DELL/Desktop/python/35.py =================
Original Dataset:

   Brand Processor   Price
0   Dell        i5   50000
1     HP        i7   65000
2  Apple        M1  120000
3   Dell        i3   40000
4     HP        i5   52000

After Label Encoding:

   Brand Processor   Price  Brand_Label  Processor_Label
0   Dell        i5   50000            1                2
1     HP        i7   65000            2                3
2  Apple        M1  120000            0                0
3   Dell        i3   40000            1                1
4     HP        i5   52000            2                2

One-Hot Encoded Data:

   Brand_Apple  Brand_Dell  Brand_HP  ...  Processor_i3  Processor_i5  Processor_i7
0          0.0         1.0       0.0  ...           0.0           1.0           0.0
1          0.0         0.0       1.0  ...           0.0           0.0           1.0
2          1.0         0.0       0.0  ...           0.0           0.0           0.0
3          0.0         1.0       0.0  ...           1.0           0.0           0.0
4          0.0         0.0       1.0  ...           0.0           1.0           0.0

[5 rows x 7 columns]

Final Combined Dataset:

   Brand Processor   Price  ...  Processor_i3  Processor_i5  Processor_i7
0   Dell        i5   50000  ...           0.0           1.0           0.0
1     HP        i7   65000  ...           0.0           0.0           1.0
2  Apple        M1  120000  ...           0.0           0.0           0.0
3   Dell        i3   40000  ...           1.0           0.0           0.0
4     HP        i5   52000  ...           0.0           1.0           0.0

[5 rows x 12 columns]


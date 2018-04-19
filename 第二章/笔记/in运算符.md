``````python
"""in运算符

    in运算符可以用于检查特定值是否在序列中


   # 字符串 #
   'x' in 'rwx' => True
   'd' in 'rwx' => False


   # 复杂的序列 #
   database = [
        [ 'urain39', '12345678'  ],
        [ 'admin', 'admin' ]
   ]

   ['urain', '123'] in databse => False
"""

database = [
    [
        'urain39',
        '12345678'
    ],
    [
        'admin',
        'admin'
    ]
]

print("['urain39', '123'] in database => %s" \
                     % (['urain39', '123'] in database))
print("'urain39', '12345678' in database => %s" \
                        %(['urain39', '12345678'] in database))

``````

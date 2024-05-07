

# 1.) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define
# funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100]

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# def squared(task1):
#     sqrts = [x for x in task1 if x == 0 or (x > 0 and (int(x ** 0.5)) ** 2 == x)]
#     for sqr in sqrts:
#         print(sqr)
# print(squared(mylist)) 

#  2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın:
#   input:[-1,1,2,2,6,7,7,'say']

# def rep(inp):
#     empty = [];
#     for des in inp:
#         if inp.count(des) == 1:
#             empty.append(des);
#     return empty;

# inp= [-1,1,2,2,6,7,7,]

# print(rep(inp))

# 3) Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın
# input = input("Hasili tapılacaq rəqəmləri daxil edin: ")
# def funcinp(input):
#     result = 1;
#     for numbers in input:
#         if numbers.isdigit():
#             result *= int(numbers);
#     return result;
# print("Rəqəmlərin hasili: ", funcinp(input))


# 4) verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın


# def  numbers(num): return [x for x in range(1, num + 1) if num % x == 0]
# num = int(input("Ədədi yaz böləni tapaq: "))
# print(f"{num} ədədinin bölənləri:", numbers(num)) 

# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary 
# yaradın və bunu comprehension ilə edin və alınan listi print etdirin.
# mənim listim
# mylist=['may','iyun','iyul']
# bu şəkildə olacaq
# {'may': 3, 'iyun': 4, 'iyul': 4}

# month = ['yanvar', 'noyabr', 'avqust']
# monthfind = dict((e, len(e)) for e in month)
# print(monthfind)
# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və 
# bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# def first(names):
#     onlyname = [i.split()[0].lower() for i in names]
#     return onlyname
# func = first(names)
# print(func)

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results=[ 2.5, 3.5, 4.5]

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
# print(results)
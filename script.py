#Task 1
customer_id = ['B818', 'A461', 'A092', 'A082', 'B341', 'A005', 'A092', 
                'A461','B219', 'B904', 'A901', 'A083', 'B904', 'A092', 
                'B341', 'B821','B341', 'B821', 'B904', 'B818', 'A901', 
                'A083', 'B818', 'A082','B219', 'B219', 'A083', 'A901', 
                'A082', 'B341', 'B341', 'A083','A082', 'B219', 'B439', 
                'A461', 'A005', 'A901', 'B341', 'A082','A083', 'A461', 
                'A083', 'A901', 'A461', 'A083', 'A082', 'A083','B341', 
                'A901', 'A082', 'A461', 'B219', 'A083', 'B818', 'B821',
                'A092', 'B341', 'A461', 'A092', 'A083', 'B821', 'A092']
uniqueids = set(customer_id)
totaluniqueids = len(uniqueids)
print(totaluniqueids)

#Task 2
Data = [1, 4, 9, 16, 25, 36, 49,  64, 81, 100]

#a.16
print (Data[3])

#b.[36, 49, 64, 81]
print (Data[5:9])

#c.[100, 81, 64, 49, 36, 25, 16, 9, 4, 1]
square=[x**2 for x in range (10,0,-1)]
print(square)

#Task 3
provinsi = {'Nanggroe Aceh Darussalam': 'Aceh','Sumatera Selatan': 'Palembang','Kalimantan Barat': 'Pontianak','Jawa Timur': 'Madiun','Sulawesi Selatan': 'Makassar','Maluku': 'Ambon'}

#a.get list of keys available in dictionary
print(provinsi.keys())

#b.Change 'Jawa Timur' value from 'Madiun'  to 'Surabaya'6
provinsi["Jawa Timur"] = "surabaya"
print(provinsi)
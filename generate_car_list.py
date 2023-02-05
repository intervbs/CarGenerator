'''Written by Jøran Lillegård 2023'''
import random
import pickle

def fileToDictionary(filename):
    '''Use the complete name with file extension (text.txt)'''
    passings = []
    with open(filename, 'r') as fp:
        for line in fp:
            key= line.split(',')
            passings.append(key[0])
    return passings

def generateCars(filename):
    car_list = {}
    # Change the name on the input file here
    v_dict = fileToDictionary(filename)
    cars = {'Volvo': {'car': {'S60', 'S90', 'V60'}, 'SUV': {'ZC40', 'XC60', 'XC90'},},
            'Volkswagen': {'truck': {'Amarok', 'Crafter Pickup', 'Transporter Pickup'}, 'car': {'Golf', 'Passat', 'Jetta'}, 'SUV': {'ID4', 'T-Cross', 'T-Roc'}},
            'Toyota': {'truck': {'Hilux', 'Tacoma', 'Tundra'}, 'car': {'Agya', 'Supra', 'Yaris'}, 'SUV': {'RAV 4', 'C-HR', 'Yaris Cross'}},
            'Ford': {'truck': {'F-150 Raptor', 'Maverick', 'Lobo'}, 'car': {'Fiesta', 'Focus', 'Kuga'}, 'SUV': {'Puma', 'Kuga', 'Explorer'}},
            'BMW': {'car': {'X1', '325', '318'}, 'SUV': {'X1', 'X2', 'X4'}},
            'Audi': {'car': {'A1', 'A3', 'A4'}, 'SUV': {'Q5', 'Q7', 'Q8'}},
            'Kia': {'car': {'Ceed', 'EV6', 'K8'}, 'SUV': {'Sorento', 'Seltos', 'Sonet'}},
            'Renault': {'truck': {'Alaskan'}, 'car': {'Clio', 'Espace', 'Kadjar'}, 'SUV': {'Austral', 'Koleos', 'Captur'}},
            'Mercedes-Benz': {'car': {'CLA', 'CLS', 'EQE'}, 'SUV': {'EQE SUV', 'EQA', 'EQB'}},
            'Peugeot': {'truck': {'Landtrek'}, 'car':{'208', '301', '308'}, 'SUV': {'3008', '2008', '5008'}}
            }
    no = 0
    for regno in v_dict:
        # Makes random choises for the brand, model and type
        brand = random.choice(list(cars))
        v_type = random.choice(list(cars[brand]))
        car = random.choice(list(cars[brand][v_type]))
        # Appending the choices into the correct class object
        if v_type == 'car':
            car_list[no] = {'brand': f'{brand} {car}', 'year': random.randint(2011, 2023), 
                        'km': random.randint(0, 200000), 'price': random.randint(15000, 900000), 
                        'special': random.choice([2, 4]), 'plate': regno, 'type': v_type}
        elif v_type == 'truck':
            car_list[no] = {'brand': f'{brand} {car}', 'year': random.randint(2011, 2023), 
                        'km': random.randint(0, 200000), 'price': random.randint(15000, 900000), 
                        'special': random.choice(['2WD', '4WD']), 'plate': regno, 'type': v_type}
        elif v_type == 'SUV':
            car_list[no] = {'brand': f'{brand} {car}', 'year': random.randint(2011, 2023), 
                        'km': random.randint(0, 200000), 'price': random.randint(15000, 900000), 
                        'special': random.choice([2, 3, 4]), 'plate': regno, 'type': v_type}
        else:
            pass
        no += 1
    return car_list
if __name__ == '__main__':        
    car_list = generateCars(input('Enter Filename >>> '))
    with open('car_list.txt', 'wb') as fp:
        pickle.dump(car_list, fp)

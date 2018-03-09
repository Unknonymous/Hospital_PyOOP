# Patient:
class Patient(object):
    # Attributes: Id number, Name, Allergies, Bed number: should be none by default
    def __init__(self, id_number, name, allergies):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = None
       

# Hospital
class Hospital(object):
# Attributes: 
    # Patients: an empty array
    # Name: hospital name
    # Capacity: an integer indicating the maximum number of patients the hospital can hold.
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.beds = []                  #assign bed availability by index
        for i in range ( 0, (capacity) ):
            self.beds.append(True)
    # Admit: 
    def admit(self, patient):
        # If the length of the list is >= the capacity do not admit the patient. 
        if len(self.patients) >= self.capacity:
            print 'It seems there is no room for {} at {}'.format(patient.name, self.hospital_name)
            return self
        else:
        # add a patient to the list of patients. 
            self.patients.append({patient.id_number : patient.name})
        # Assign the patient a bed number.
            for i in range (0, len(self.beds)):
                if self.beds[i] == True:
                    patient.bed_number = i
                    self.beds[i] = False  #make bed unavailable once assigned.
        # Return a message either confirming that admission is complete or say
        # ing the hospital is full.
                    print "{} has been admitted to {} and assigned bed number {}".format(patient.name, self.hospital_name, patient.bed_number)
                    return self
    
    # Discharge: 
    def discharge(self, patient):
        # look up and remove a patient from the list of patients.
        for person in self.patients:
            if person == {patient.id_number : patient.name}:
                self.patients.pop(self.patients.index(person))
                self.beds[patient.bed_number] = True
                patient.bednumber = None
                print "{} has been dicharged from {}.  All Better!".format(patient.name, self.hospital_name)
        return self
        # Change bed number for that patient back to none.













# #Test Cases:

# create patient 1
JoAnne = Patient(3201, 'JoAnne', ('peanuts', 'shell-fish', 'pennicillin') )
# create patient 2
Clarence = Patient(1468, 'Clarence', ('alcohol'))
# create patient 3
Studemeyer = Patient(5468, 'Studemeyer', ('none'))

# create hospitals
Ninja_Medical = Hospital('Ninja_Medical', 2)  #insufficient capacity
NinMed = Hospital('NinMed', 4)  #sufficient capacity


#admit patients until overflow
Ninja_Medical.admit(JoAnne).admit(Clarence).admit(Studemeyer)

#print patient list
print Ninja_Medical.patients
print '*'*100

#admit all patients, discharge patient
NinMed.admit(Clarence).admit(Studemeyer).admit(JoAnne).discharge(Clarence)

#print patient list
print NinMed.patients

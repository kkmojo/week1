"""
lab1 extra exercise
"""


class PatientRoster:
    """
     an appointment system for a doctor's office.
     ===Attributes==
     @type patients:list
        each elements in this list represents
        a single patient,with information stores
        in
    @type limit: int
        limit of patients this doctor could stand.
    @type gender_rule: bool
        this checks if this doctor enables
        gender rule.
    @type gender_limit:tuple(int,int)
        first element is the max number for male,
        second is for female
    @type current_num: list
    first element is the current number of male
    patient this doctor have, second is female.

    """
    def __init__(self, limit, rule=False):
        """
        initialize a new doctor with <limit>
        and if gender rule is applied, ,<rule>
        should be True, otherwise, it's default
        as False.

        @type limit: int
        @type rule: bool
        @type self: Doctor
        @rtype: None
        """
        self.gender_rule = rule
        self.patients = []
        self.limit = limit
        self.gender_limit = ()
        self.current_num = [0, 0]

    def set_rule(self, male_ratio):
        """set up the gender ratio rule for this
        doctor, this may not be changed once set.
        <male_ratio> is a number between
        1 and 0

        @type self: Doctor
        @type male_ratio: float
        @rtype None

        >>> new = PatientRoster(100,True)
        >>> new.set_rule(0.6)
        >>> new.gender_limit
        (60, 40)
        """
        if self.gender_rule is True:
            if 0 <= male_ratio < 1:
                male = int(self.limit * male_ratio)
                female = self.limit - male
                self.gender_limit = (male, female)

    def patient_register(self, ohip_number, name, gender):
        """
        @type self: Doctor
        @type ohip_number: int
        @type name: list
        @type gender str
        @rtype: None
        >>> new = PatientRoster(100,True)
        >>> new.set_rule(0.6)
        >>> new.patient_register(1234,['mike','lee'],'male')
        >>> new.patients
        [[1234, 'mike', 'lee', 'male']]
        >>> new.current_num
        [1, 0]
        """
        total = self.current_num[0] + self.current_num[1]
        if self.gender_rule is True:
            if gender == "male":
                if total < self.limit and self.current_num[0] < self.gender_limit[0]:
                    self.patients.append([ohip_number, name[0], name[1], gender])
                    self.current_num[0] += 1
            elif gender == "female":
                if total < self.limit and self.current_num[1] < self.gender_limit[1]:
                    self.patients.append([ohip_number, name[0], name[1], gender])
                    self.current_num[1] += 1

    def delete_patient(self, ohip_num):
        """
        delete a patient from the patient list if
        that <ohip_num> is in the list.

        @type self: Doctor
        @type ohip_num: int
        @rtype: None

        >>> new = PatientRoster(100)
        >>> new.set_rule(0.6)
        >>> new.patient_register(1234,['mike','lee'],'male')
        >>> new.delete_patient(1234)
        >>> new.patients
        []
        """
        for patient in self.patients:
            if patient[0] == ohip_num:
                self.patients.remove(patient)
                break


class ClassList:
    """
     a student records system like ROSI

     ===Attributes===
     @type students: list
        a list keeps track of all students in this course,
        each identified by student number.
     @type limit: int
        a limit of how many students this course holds.

    """
    def __init__(self, limit):
        """
        create a new course with <limit>.

        @type limit: int
        @rtype: None
        """
        self.limit = limit
        self.students = []

    def register(self, student_num):
        """
        register a student to this course if it won't
        break the course limit, students are identified
        by <student_num>.

        @type student_num: int
        @rtype: None

        >>> csc148 = ClassList(140)
        >>> csc148.register(1234)
        >>> csc148.students
        [1234]
        """
        if student_num not in self.students and len(self.students) < self.limit:
            self.students.append(student_num)

    def drop(self, student_num):
        """
        delete a student from the course with its
        <student_num>

        @type student_num: int
        @rtype: none

        >>> csc148 = ClassList(140)
        >>> csc148.register(1234)
        >>> csc148.students
        [1234]
        >>> csc148.drop(1234)
        >>> csc148.students
        []
        """
        if student_num in self.students:
            self.students.remove(student_num)


class Player:
    """
    an app for a game like 2048 or PacMan, where players get
    a score each time they play.

    ===Attributes===
    @type scores: list
        a list keeps track of the last 100 games's score
        of a player
    @type average: int
        this is the average score of this player over n
        games

    """
    def __init__(self):
        """
        initilize a new player.

        @type self: Player
        @rtype: None
        """
        self.scores = []
        self.average = 0

    def record(self, score):
        """
        record a game with <score> for this player.
        the 100-th game record will be deleted if
        it existes.

        @type self: Player
        @type score: int
        @rtype: none

        >>> new = Player()
        >>> new.record(1000)
        >>> new.scores
        [1000]
        >>> 1000 in new.scores
        True
        >>> for each in range(1,100): new.record(each)
        >>> 1000 in new.scores
        False

        """
        self.scores.append(score)
        if len(self.scores) >= 100:
            self.scores.pop(0)
        self.average = self.avg_helper(self.scores)

    def avg_helper(self, lst):
        """
        A helper function for calculating the average
        score of a player.

        @type self: Player
        @type lst: list
        @rtype: int
        """
        total = 0
        for each in lst:
            total += each
        avg = int(total/len(lst))
        return avg


class InventoryItem:
    """
     an inventory system

     ===Attirubutes===
     @type products = []
        a list storing all the info of products
     @type categories: dict
        this dictionaries stores all the products
        with its categories

    """
    def __init__(self):
        """
        Create a new inventoryItem

        @type self: InventoryItem
        @rtype: None
        """
        self.products = []
        self.categories = {}

    def add_product(self, num, name, _type, price):
        """
        add a new product to this inventory

        @type self: InventoryItem
        @type num: int
        @type name: str
        @type _type: str
        @type price: int
        @rtype: none

        >>> new = InventoryItem()
        >>> new.add_product(1234,'coke','beverage',10)

        """
        product = [num, name, price]
        self.products.append(product)
        if _type not in self.categories:
            self.categories[_type] = [product]
        else:
            self.categories[_type].append(product)

    def get_price(self, num):
        """
        given the number of a product, return a
        str that indicates the price of the product,
        return None if there's no such product.

        @type self: InventoryItem
        @type num: int
        @rrtype: int|none

        >>> new = InventoryItem()
        >>> new.add_product(1234,'coke','beverage',10)
        >>> new.get_price(1234)
        10
        >>> new.get_price(2345)

        """
        for each in self.products:
            if num == each[0]:
                return each[2]

    def discount(self, num, percent):
        """
        given the number of a product, discount its
        price by <percent>, if that number is in this
        system.

        @type self: InventoryItem
        @type num: int
        @type percent: float
        @rtype: none

        >>> new = InventoryItem()
        >>> new.add_product(1234,'coke','beverage',10)
        >>> new.discount(1234,0.5)
        """
        new_rate = 1 - percent
        for each in self.products:
            if num == each[0]:
                each[2] *= new_rate
                break

    def compare(self, num1, num2):
        """
        givne two number of two products, compares
        the price of them by return their prices in
        a string if and only if num1 and num2 are in
        this system

        @type num1: int
        @type num2: int
        @rtype: none
        >>> new = InventoryItem()
        >>> new.add_product(1234,'coke','beverage',10)
        >>> new.add_product(4321,'dry','beverage',20)
        >>> new.compare(1234,4321)
        price of first product: 10 ,price of second product: 20
        """
        price1 = None
        price2 = None
        for each in self.products:
            if num1 == each[0]:
                price1 = each[2]
            elif num2 == each[0]:
                price2 = each[2]
            if price1 is int and price2 is int:
                break
        if type(price1) is not None and type(price2) is not None:
            print('price of first product:', price1,
                  ',price of second product:', price2)

from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=50)

class Canton(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
# Create your models here.
class LostPet(models.Model):
    class Province(models.TextChoices):
        ALAJUELA = "ALA", "Alajuela"
        CARTAGO = "CAR", "Cartago"
        GUANACASTE = "GUA", "Guanacaste"
        HEREDIA = "HER", "Heredia"
        LIMON = "LIM", "Limón"
        SAN_JOSE = "SAN", "San José"

    class PetType(models.TextChoices):
        DOG = "DOG", "Dog"
        CAT = "CAT", "Cat"
        BIRD = "BRD", "Bird"
        RABBIT = "RAB", "Rabbit"
        TURTLE = "TUR", "Turtle"
        HAMSTER = "HAM", "Hamster"
        GUINEA_PIG = "GPI", "Guinea Pig"
        FISH = "FSH", "Fish"
        FERRET = "FER", "Ferret"
        PARROT = "PAR", "Parrot"
        COCKATIEL = "CKT", "Cockatiel"
        BUDGIE = "BDG", "Budgie (Parakeet)"
        LIZARD = "LIZ", "Lizard"
        SNAKE = "SNK", "Snake"
        MOUSE = "MOU", "Mouse"
        RAT = "RAT", "Rat"
        CHINCHILLA = "CHI", "Chinchilla"
        HEDGEHOG = "HED", "Hedgehog"
        SUGAR_GLIDER = "SGL", "Sugar Glider"
        OTHER = "OTH", "Other"
    class Sex(models.TextChoices):
        MALE = "M", "Male" 
        FEMALE = "F", "Female"
        UNKNOWN = "U", "Unknown"
    class Size(models.TextChoices):
        SMALL = "S", "Male" 
        MEDIUM = "M", "Medium"
        LARGE = "L", "Large"
        GIANT = "G", "Giant"
    
    pet_name = models.CharField(max_length=200)
    pet_type = models.CharField(max_length=3,choices=PetType.choices, default = PetType.DOG)
    sex = models.CharField(max_length=1, choices=Sex.choices, default=Sex.MALE)
    when_was_pet_seen_for_last_time = models.DateField("When was the last time, the pet was seen")
    at_what_time_pet_was_seen_last_time = models.DateTimeField("At what time the pet was seen last time")
    size = models.CharField(max_length=1,choices=Size.choices, default=Size.MEDIUM)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    address_or_nearby = models.CharField(max_length=255)
    reward = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    additional_notes = models.TextField()
     

class PetColor(models.Model):
    class ColorPriority(models.TextChoices):
        PRIMARY = "PRI", "Primary"
        SECONDARY = "SEC", "Secondary"
        TERTIARY = "TER", "Tertiary"
    color = models.CharField(max_length=255)
    priority = models.CharField(max_length=3, choices = ColorPriority.choices)
    lost_pet = models.ForeignKey(LostPet, on_delete=models.CASCADE)
    

class PetPhoto(models.Model):
    lost_pet = models.ForeignKey(LostPet, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="photos/lost-pets")
    upload_at = models.DateTimeField()    




    